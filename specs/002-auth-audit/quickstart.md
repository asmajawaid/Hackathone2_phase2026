# Backend Authentication Audit Quickstart

## Purpose
This quickstart guide enables developers to run the backend authentication audit for the Evolution of Todo Phase 2 application.

## Prerequisites
- Python 3.12+
- Node.js and npm
- PostgreSQL client (psql)
- Access to Neon PostgreSQL database
- Backend and frontend services running

## Setup
1. Ensure both backend (port 8000) and frontend (port 3000) services are running
2. Verify environment variables are set:
   - `DATABASE_URL` in backend/.env
   - `BETTER_AUTH_SECRET` matching in both frontend and backend
   - `NEXT_PUBLIC_API_URL` pointing to backend

## Execution Steps
1. Run environment verification:
   ```bash
   curl http://localhost:8000/health
   ```
2. Check database connection:
   ```bash
   psql $DATABASE_URL -c "SELECT version();"
   ```
3. Verify authentication tables exist:
   ```bash
   psql $DATABASE_URL -c "\dt"
   ```
4. Test authentication endpoints:
   ```bash
   curl -X POST http://localhost:8000/api/auth/signup \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"Test123!@#"}'
   ```

## Expected Outcomes
- All environment variables properly configured
- Database connection successful
- Authentication tables present with correct schema
- API endpoints accessible and returning proper responses
- JWT secret consistency verified between frontend and backend

## Troubleshooting
- If database connection fails, verify `DATABASE_URL` in backend/.env
- If tables don't exist, ensure `create_db_and_tables()` is called on startup
- If endpoints return 404, verify Better Auth configuration
- If JWT errors occur, check that secrets match between frontend and backend