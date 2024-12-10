Feature: Alten Search

  Scenario Outline: User searches for a "<term>" on Ofertas de empleo in Alten
    Given I open the Alten homepage
    When I go to Unete a nosotros
    When I go to Nuestras ofertas de empleo
    When I seek by "<term>" in ofertas de empleo
    Then I found only results with "<results>" in ofertas de empleo


    Examples:
      | term      | results |
      | Diseñador       | diseñador         |
      | Programador   | programador        |
