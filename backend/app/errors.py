from typing import Optional, Dict, Any
from datetime import datetime
from fastapi import HTTPException, status


class APIError(Exception):
    """Base API exception class"""
    def __init__(
        self,
        detail: str,
        code: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        additional_data: Optional[Dict[str, Any]] = None
    ):
        self.detail = detail
        self.code = code
        self.status_code = status_code
        self.additional_data = additional_data or {}
        super().__init__(detail)


class ValidationError(APIError):
    """Raised when validation fails"""
    def __init__(self, detail: str, additional_data: Optional[Dict[str, Any]] = None):
        super().__init__(
            detail=detail,
            code="VALIDATION_ERROR",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            additional_data=additional_data
        )


class AuthenticationError(APIError):
    """Raised when authentication fails"""
    def __init__(self, detail: str = "Authentication failed", additional_data: Optional[Dict[str, Any]] = None):
        super().__init__(
            detail=detail,
            code="AUTHENTICATION_ERROR",
            status_code=status.HTTP_401_UNAUTHORIZED,
            additional_data=additional_data
        )


class AuthorizationError(APIError):
    """Raised when authorization fails"""
    def __init__(self, detail: str = "Not authorized", additional_data: Optional[Dict[str, Any]] = None):
        super().__init__(
            detail=detail,
            code="AUTHORIZATION_ERROR",
            status_code=status.HTTP_403_FORBIDDEN,
            additional_data=additional_data
        )


class ResourceNotFoundError(APIError):
    """Raised when a resource is not found"""
    def __init__(self, detail: str = "Resource not found", additional_data: Optional[Dict[str, Any]] = None):
        super().__init__(
            detail=detail,
            code="RESOURCE_NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND,
            additional_data=additional_data
        )


def create_error_response(
    error: str,
    code: str,
    status_code: int,
    path: str,
    method: str,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a standardized error response"""
    response = {
        "success": False,
        "error": error,
        "code": code,
        "details": {
            "timestamp": datetime.utcnow().isoformat(),
            "path": path,
            "method": method
        }
    }

    if details:
        response["details"].update(details)

    return response


def handle_exception(exc: Exception, path: str, method: str) -> Dict[str, Any]:
    """Handle exceptions and return standardized error response"""
    if isinstance(exc, APIError):
        return create_error_response(
            error=exc.detail,
            code=exc.code,
            status_code=exc.status_code,
            path=path,
            method=method,
            details=exc.additional_data
        )
    elif isinstance(exc, HTTPException):
        return create_error_response(
            error=str(exc.detail),
            code=f"HTTP_{exc.status_code}",
            status_code=exc.status_code,
            path=path,
            method=method
        )
    else:
        # For unexpected errors, return a generic 500 response
        return create_error_response(
            error="An internal server error occurred",
            code="INTERNAL_ERROR",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            path=path,
            method=method
        )