Feature: Renfe Ticker
  Scenario: Comprar billetes
    Given Lanzar chrome
    When Abrir pagina renfe
    And Introducir origen "MADRID-PUERTA DE ATOCHA" y destino "BARCELONA-SANTS"
    And Wait "5" seconds
    And Clickar en comprar
    Then Verificar correcto


