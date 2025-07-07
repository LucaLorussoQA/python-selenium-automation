@cart
Feature: Cart tests

  @smoke
  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main pages
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown
    Then Verify Cart page opened

  @smoke
  Scenario: User can add a product to cart
    Given Open target main pages
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart pages
    Then Verify cart has 1 item(s)
    And Verify cart has correct product