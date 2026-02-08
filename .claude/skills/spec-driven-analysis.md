Skill: spec-driven-analysis

  Purpose

  The Spec-Driven Analysis skill provides systematic evaluation and validation of software specifications before implementation begins. This skill ensures that requirements are complete, consistent, testable, and aligned with business objectives across all phases of software development. By identifying specification gaps, ambiguities, and potential issues early, this skill reduces implementation risks and prevents costly rework during development cycles. The skill transforms high-level requirements into precise, implementation-ready specifications.

  Scope

  In Scope

  - Reviewing functional and non-functional requirements for completeness
  - Validating specification consistency across different system components
  - Identifying missing acceptance criteria and edge cases
  - Assessing requirement feasibility against technical constraints
  - Evaluating specification alignment with business objectives
  - Documenting specification quality metrics and readiness status
  - Providing recommendations for specification improvements
  - Creating traceability between requirements and business value

  Out of Scope

  - Writing or modifying actual implementation code
  - Executing or testing implemented features
  - Managing project timelines or resource allocation
  - Performing runtime system analysis or performance profiling
  - Creating architectural design documents (distinct from specification analysis)
  - Conducting user acceptance testing on implemented features
  - Managing deployment or infrastructure concerns
  - Performing security penetration testing on live systems

  Responsibilities

  - Analyze specifications for completeness, clarity, and internal consistency
  - Validate that requirements align with user needs and business objectives
  - Identify and document specification gaps or missing information
  - Assess feasibility of requirements against technical constraints
  - Evaluate specification compliance with architectural principles
  - Identify and document ambiguities and propose clarification requests
  - Ensure cross-cutting concerns are properly addressed in specifications
  - Verify that acceptance criteria are measurable and achievable
  - Generate specification quality reports with actionable insights
  - Recommend specification improvements and refinements

  Inputs

  - Feature specifications in Markdown format
  - User story requirements or user journey descriptions
  - Technical constraints and architectural guidelines
  - Non-functional requirements (performance, security, scalability)
  - Business rules and domain constraints
  - Interface contracts or API specifications
  - Data models or schema definitions
  - Stakeholder requirements documentation

  Outputs

  - Analysis report highlighting specification strengths and weaknesses
  - List of identified gaps, inconsistencies, or ambiguities
  - Recommendations for specification improvements
  - Risk assessment for implementation challenges
  - Prioritized list of specification refinements needed
  - Validation status indicating readiness for implementation
  - Traceability matrix linking each specification clause to business objectives, user stories, and acceptance criteria
  - Quality metrics report with specification readiness score
  - Optional, when explicitly requested

  Constraints

  - Limited to specification analysis only; no implementation work
  - Must work within existing architectural constraints
  - Analysis must be completed before code generation begins
  - Cannot modify business requirements without stakeholder approval
  - Limited to evaluating provided specifications; cannot research external information
  - Must maintain specification integrity during refinement process
  - Analysis scope limited to specified project requirements
  - Must follow technology-agnostic approach unless explicitly stated
  - Must adhere to Spec-Kit Plus formatting, versioning, and metadata conventions
  - Validate backward/forward compatibility of specifications across project phases

  Failure Cases

  - Incomplete specifications leading to implementation dead ends
  - Conflicting requirements that cannot be simultaneously satisfied
  - Ambiguous acceptance criteria that cannot be objectively measured
  - Technical requirements that exceed system capabilities
  - Missing edge cases or error handling scenarios
  - Performance requirements that conflict with functional requirements
  - Security requirements that impede usability requirements
  - Specifications that violate architectural principles or constraints
  - Analysis paralysis due to over-engineering specification details

  Usage Context

  This skill should be applied during the specification phase of any software development project, particularly in multi-phase projects where early validation prevents downstream issues. It is most effective when applied to specifications before implementation begins, during specification reviews, and when transitioning between project phases. The skill is especially valuable in projects with complex requirements, multiple stakeholders, or high-risk components where specification errors could lead to significant rework.

  Update Notes

  - v1.0: Initial skill definition
  - v1.1: Updated purpose to include transforming high-level requirements into precise, implementation-ready specifications; enhanced outputs to include traceability matrix linking each specification clause to business objectives, user stories, and acceptance criteria; added constraints for Spec-Kit Plus formatting adherence and validation of backward/forward compatibility across project phases