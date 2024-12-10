Feature: Alten Search

  Scenario Outline: User searches for a "<term>" on Alten header
    Given I open the Alten homepage
    When I search for "<term>" in the header
    Then I should see "<results>" search results for "<term>" in the header

    Examples:
      | term      | results |
      | spain       | 72         |
      | compromiso   | 71        |
