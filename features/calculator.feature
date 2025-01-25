Feature: Basic Calculator

  Scenario: Addition
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Subtraction
    Given I have a calculator
    When I subtract 5 from 10
    Then the result should be 5

  Scenario: Multiplication
    Given I have a calculator
    When I multiply 4 by 3
    Then the result should be 12

  Scenario: Division
    Given I have a calculator
    When I divide 10 by 2
    Then the result should be 5
