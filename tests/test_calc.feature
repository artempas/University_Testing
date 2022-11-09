# Created by artem_pas at 09.11.2022
Feature: My completely awesome and unique ultra pro mega max plus calculator
  # Enter feature description here

  Scenario Outline: Add one number to another
    Given I opened calc app
    When I entered <first_value>
    When I pressed plus button
    When I entered <second_value>
    When I pressed calculate button
    Then I get <result>
    Examples:
    |first_value|second_value|result|
    |1          |2           |3     |
    |10         |21          |31    |
    |73         |54          |127   |
    |500        |500         |1000  |

