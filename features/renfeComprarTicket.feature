Feature: Renfe Ticker
  Scenario: Comprar billetes
    Given Lanzar chrome
    When Abrir pagina renfe
    Then Comprobar precio
    And Cerrar navegador

