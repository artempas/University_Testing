# Created by artem_pas at 09.11.2022
Feature: My completely awesome and unique ultra pro mega max plus calculator
  # Enter feature description here

  Scenario Outline: Sum
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

  Scenario Outline: Multiply
    Given I opened calc app
    When I entered <first_value>
    When I pressed multiply button
    When I entered <second_value>
    When I pressed calculate button
    Then I get <result>
    Examples:
    |first_value|second_value|result|
    |1          |2           |2     |
    |10         |21          |210   |
    |73         |54          |3942  |
    |500        |500         |250000|
    |-20        |32          |-640  |
    |-1         |3           |-3    |
    |-1         |-1          |1     |
    |0          |0           |0     |
    |0          |5           |0     |


  Scenario Outline: Subtract
    Given I opened calc app
    When I entered <first_value>
    When I pressed minus button
    When I entered <second_value>
    When I pressed calculate button
    Then I get <result>
    Examples:
    |first_value|second_value| result |
    |500        |500         |0       |
    |1          |2           |-1      |
    |10         |21          |-11     |
    |73         |54          |19      |
    |-20        |32          |-52     |
    |-1         |3           |-4      |
    |-1         |-1          |0       |
    |0          |0           |0       |
    |0          |5           |-5      |
  Scenario Outline: divide  
    Given I opened calc app
    When I entered <first_value>
    When I pressed divide button
    When I entered <second_value>
    When I pressed calculate button
    Then I get <result>
    Examples:
    |first_value|second_value| result |
    |500        |500         |1       |
    |1          |2           |0.5     |
    |-20        |32          |-0.625  |
    |-1         |-1          |1       |
    |0          |5           |0       |

  Scenario: Wrong Input
    Given I opened calc app
    When I entered text
    Then I get nothing


  Scenario Outline: Mixed input
    Given I opened calc app
    When I entered <first_value_mixed>
    When I pressed <Operation> button
    #noinspection CucumberUndefinedStep
    When I entered <second_value_mixed>
    When I pressed calculate button
    Then I get <result>
    Examples:
    |first_value_mixed|second_value_mixed| result |Operation|
    |1                |asd2              |3       |plus     |
    |5d0d0            |50dsa0            |1       |divide   |
    |-20              |32das             |-52     |minus    |
    |-sa1             |-1                |1       |multiply |
    |0                |a5a               |5       |plus     |

  Scenario Outline: Consecutive operations
    Given I opened calc app
    When I entered <first_value>
    When I pressed <first_operation> button
    When I entered <second_value>
    When I pressed <second_operation> button
    When I entered <third_value>
    When I pressed calculate button
    Then I get <result>
    Examples:
      | first_value | first_operation | second_value | second_operation | third_value | result |
      |2            |plus             |2             |multiply          |2            |8       |
      |2            |plus             |2             |minus             |2            |2       |
      |2            |plus             |1             |divide            |3            |1       |
      |2            |plus             |2             |plus              |2            |6       |
      |4            |minus            |2             |multiply          |2            |4       |
      |4            |minus            |2             |minus             |2            |0       |
      |4            |minus            |1             |divide            |3            |1       |
      |4            |minus            |2             |plus              |2            |4       |
      |1            |multiply         |2             |multiply          |2            |4       |
      |1            |multiply         |2             |minus             |2            |0       |
      |1            |multiply         |3             |divide            |3            |1       |
      |1            |multiply         |2             |plus              |2            |4       |
      |12           |divide           |6             |multiply          |2            |4       |
      |12           |divide           |6             |minus             |2            |0       |
      |12           |divide           |4             |divide            |3            |1       |
      |12           |divide           |6             |plus              |2            |4       |

  Scenario Outline: Zero division
    Given I opened calc app
    When I entered <first_value>
    When I pressed divide button
    When I entered 0
    When I pressed calculate button
    Then I get error
    Examples:
    |first_value|
    |500        |
    |1.2        |
    |-20.2      |
    |-1         |
    |0          |

  Scenario: Just press equal
    Given I opened calc app
    When I pressed calculate button
    Then I get nothing
    
  Scenario: Enter value and press equal
    Given I opened calc app
    When I entered 123
    When I pressed calculate button
    Then I get 123

  Scenario Outline: Consecutive zero division
    Given I opened calc app
    When I entered <first_value>
    When I pressed <first_operation> button
    When I entered <second_value>
    When I pressed divide button
    When I entered 0
    When I pressed calculate button
    Then I get error
    Examples:
      | first_value | first_operation | second_value |
      |2            |plus             |1             |
      |4            |minus            |1             |
      |1            |multiply         |3             |
      |12           |divide           |4             |
  Scenario Outline: Zero division with other operation
    Given I opened calc app
    When I entered <first_value>
    When I pressed divide button
    When I entered 0
    When I pressed <operation> button
    Then I get error
    Examples:
      | first_value | operation |
      |2            |plus       |
      |4            |minus      |
      |1            |multiply   |
      |12           |divide     |