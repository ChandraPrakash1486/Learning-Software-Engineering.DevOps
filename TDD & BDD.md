## TDD and BDD Methodologies: ##
TDD stands for Test-Driven-Development, is a software development methodology in which tests or unit tests are written before the actual code is implemented.The main focus of TDD is to verify that ***each unit of code*** behaves as expected by writing automated tests upfront.

## Key Concepts:
**Red-Green-Refactor cycle**

**Red:** we write test for the new feature or functionality. this test will definitely fail because the feature is not yet implemented.

**Green:** we write just enough code to make the test pass. no error is occured.

**Refactor(optional):** we modify the code to improve its internal structure and its quality and to make it more readable.

BDD stands for Behavior-Driven-Development, is an extension of TDD methodology, which focuses on the behavior of the system or software from the ***user's perspective***, therefor it uses natural language, like Gherkin, to describe the behavior of the system or the software, which makes it more accessible for non-technical stakeholders. 

***BDD follows a given-when-then syntax***
Given-When-Then Syntax:

**Given**: Describes the initial state of the system (preconditions).
**When**: Describes the action or event that triggers the behavior.
**Then**: Describes the expected outcome or result.