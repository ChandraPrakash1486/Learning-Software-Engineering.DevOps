# SDLC and SD Workflow:

**SDLC:** The Software Development Life Cycle (SDLC) is a higher-level conceptual framework that defines the stages involved in developing a software product. It's a more **_abstract_** representation of the overall phases of a software project.

**SD Workflow:** The software development workflow refers to the **_specific steps, tasks, and processes that a development team follows to take a software project from concept to deployment and maintenance._**
so, SDLC is an absract framework, that outlines the steps to develop a software, while the SDLC Workflow is the Application of SDLC Model.

**SDLC (Framework):** Think of "cooking a meal" as the overall process of preparing food. It's the concept. It doesn't specify the exact steps or ingredients, just the idea of the stages involved, and it is a framework to follow.

**SDLC Model:** Think of a specific type of recipe (Italian, Indian, Mexican). Each type has its own steps, techniques, and ingredients, and specifies a different way to approach cooking. These are the different types of approaches, and methods to create a meal.

**Software Development Workflow:** Think of the exact process of cooking a specific dish from a given recipe (e.g., cooking lasagna using the Italian recipe). This is the detailed list of steps and actions that the chef will take, it is the how.

**now, before moving on to the SDLC model, you should have the understanding of two key terms, given below:**
**1. Model:** refers to a specific approach to the SDLC (e.g., Waterfall, Scrum).

**2. Type:** refers to a broader categorization of those models based on shared characteristics (e.g., Sequential, Iterative, Agile).

we'll cover both Models and their Types.

## SDLC Models and Their Types:

**1. Sequential Type:**
Description: Characterized by a linear, sequential flow where each phase is completed entirely before the next one starts.

**_SDLC Models that Fall Under the Sequential Type:_**
**Waterfall Model:** A classic, rigid model with distinct sequential phases (Requirements, Design, Implementation, Testing, Deployment, Maintenance).

**V-Model:** A variant of Waterfall that emphasizes testing and aligns testing phases with corresponding development phases.

**2. Iterative Type**
**Description**: Characterized by repeating cycles of development, where each cycle delivers a working version of the product.

**_SDLC Models that Fall Under the Iterative Type:_**
**Iterative Model (also called Incremental):** Involves planning for an entire software development project, then dividing it into iterations that deliver increasingly functional versions of the software.

**Agile Model (Umbrella term):** An iterative and incremental approach focusing on flexibility, collaboration, and responsiveness to change. This includes several specific Agile implementations:

**Scrum:** A lightweight framework with short sprints, daily stand-ups, and iterative planning.

**Kanban:** A methodology focusing on visualizing the workflow, limiting work-in-progress (WIP), and continuous flow.

**Extreme Programming (XP):** Agile model emphasizing practices such as pair programming, test-driven development (TDD) and continuous integration.

**Lean:** Agile model emphasizing continuous learning and efficiency through reduction of waste and continuous improvement.

**3. Risk-Driven Type**

**Description:** Characterized by a strong emphasis on identifying, analyzing, and mitigating risks throughout the development process.

**_SDLC Models that Fall Under the Risk-Driven Type:_**
Spiral Model: Combines elements of Waterfall and Iterative approaches and focuses on risk assessment and prototyping in each cycle (spiral).

**4. Collaborative Type**

**Description:** Characterized by a focus on close collaboration, cross-functional teams, fast feedback cycles and shared responsibility.

**_SDLC Models that Fall Under the Collaborative Type:_**

**Agile Model:** (as discussed above, but emphasized for collaborative aspects.)

**DevOps Model:** Focuses on integrating development and operations teams for faster and more reliable software delivery through collaboration and automation.

so keep in mind, that-
**SDLC (Software Development Life Cycle):** Is the broad concept of the various stages of a software project.

**SDLC Model:** Is a specific approach or method chosen to manage the development process, and these are of different types.

**Examples of SDLC Models:** Waterfall, Agile, Spiral, Iterative, V-Model, and DevOps are all different **types of SDLC models**.

It's common to see teams adopting hybrid approaches combining different aspects of various models.

# What is DevOps?

Ans. DevOps is a set of practices that integrates the development and operation team, that enhance the collaboration and efficiency in delivering applications and services.
Traditional software development practices and methods often involves soiled teams and sequential workflow, whereas DevOps emphasizes continuous integration, continuous delivery, and automation.This approach enables organizations to release software updates more frequently and reliably, respond swiftly to user feedback, and maintain system stability.

## Important DevOps practices and concepts for Software Engineering:

**1.Version Control:** Version Control is a practice to keep track of and manage software code changes.
Version Control System(VCS), like Git, is a software tool that helps to track and manage software code or file changes.Even for simple programs, maintaining a history of modifications allows you to revert to previous versions if needed and facilitates collaboration if you decide to work woth others.

**2.Continuous Integration:** CI is a software development practice that involves merging code changes into a pre-existing shared repository and running automated tests.

Automated tests in CI are sets of pre-written instructions (code) that are executed automatically by the CI server or runner,like Github Actions, during or immediately after the build process to validate new code changes and the overall integrity of the application against predefined expectations and requirements.

CI/CD is a specific whole topic that I'll cover in this journey.
