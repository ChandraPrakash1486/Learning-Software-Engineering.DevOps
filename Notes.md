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

**3.Continuous Delivery/Deployment (CD):** Continuous Delivery (often abbreviated as CD) is a software development practice where changes to code are automatically built, tested, and prepared for release to a production environment. The core idea is to make software releases more frequent, reliable, and less risky.(it invloves human intervention for deployment)
on the other hand,**Continuous Deployment (also often abbreviated as CD)** is an **_extension_** of Continuous Delivery. In Continuous Deployment, every change that passes automated tests is automatically deployed to the production environment, without any manual intervention.(it does not require human intervention for deployment of the code changes)

**Continuous Delivery is a prerequisite for Continuous Deployment**

**4.Automated Tests:** Automated tests verify that our code behaves as expected and help catch bugs early in the development process. we write Automated Tests for our code, using frameworks appropriate for the programming, we are writing code in,like JUnit for Java or pytest for Python.
Generally, you do not write your tests directly within the same file as your main application code. Keeping tests separate from application code promotes better organization and separation of concerns. This makes the codebase cleaner, easier to understand, and easier to maintain.

**5. Infrastructure as Code (IaC):** Instead of manually configuring servers or using a web interface to provision resources, you describe your infrastructure using code in definition files.
This allows you to treat your infrastructure in the same way you treat your application code. You can version, review, and reuse it, promoting repeatability and automation.

**6. Monitoring and Logging:** Monitoring is the process of actively collecting, analyzing, and visualizing real-time or near real-time data about the performance, availability, and overall health of your systems and applications. It's about proactively observing your systems and identifying potential issues before they impact users.

**What to Monitor:**

**Infrastructure Metrics:** CPU utilization, memory usage, disk I/O, network traffic, load balancer performance, etc.

**Application Metrics:** Request latency, error rates, response times, transaction volume, API performance, database performance, etc.

**Business Metrics:** Number of active users, revenue generated, number of transactions, etc.

**Custom Metrics:** Application-specific metrics relevant to business goals.

Logging is the process of recording events, activities, and errors within your applications and systems. Logs are structured text records that provide a historical record of what has happened in the system.

**What to Log:**

**Application Events:** User actions, API requests, database queries, errors, exceptions, warnings.

**System Events:** Startups, shutdowns, system errors, authentication attempts, resource allocation.

**Security Events:**Login attempts, authorization failures, suspicious activity.

**Audit Logs:** Tracking changes made by users to critical systems.

**Application Errors:** Detailed information when the applications are not behaving normally.

**7. Agile Project Management:** In essence, Agile is a way of approaching project management and software development that emphasizes flexibility, collaboration, and iterative progress. It's a departure from traditional, rigid approaches like Waterfall, and it's widely used in modern software development and other industries.

### Cloud-Native Microservices and Containerization

to understand, Microservice Architecture we should understand the Monolithic Architecture.

Monothlithic is a Traditional Software Architecture, that is used in small organizations. in this architecture the complete application is developed as a single unit. All the functions and components are tightly coupled and packaged into one single deployable unit or codebase or repository. it is suitable for personal projects and small organizations.

Microservice Architecture is a Modern Approach to software development. in this architecture the complete application is divided into multiple parts and units. these units or functions are independent to each other. i.e. each part of the application in developed individualy and thus it provided scaling and techology flexibility as the parts of the application can be developed in different technologies regardless of other part's tech stack.
each part also has its independent codebase. each service or part is developed by separate team. each part of the application has a single job or function.
the microservice archtecture is used for complex projects, where team is larger.

### What is Cloud-Native Microservice
Cloud-native microservices is the modern ***evolution*** of microservice architecture, designed specifically to thrive in cloud environments. they are built as small, independent services, packaged into containers, like Docker, and deployed onto cloud platforms, and leveraging container orchestration, like Kubernetes for dynamic scaling and management.
xtends the microservice concept by embracing cloud computing platforms and practices to build scalable, resilient, and agile applications.

