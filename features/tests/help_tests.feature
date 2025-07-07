Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Orders & Purchases
    Then Verify help Print a receipt page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Partner Programs
    Then Verify help Ulta Beauty at Target page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Delivery & Pickup
    Then Verify help Drive Up & Order Pickup page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Payment Options
    Then Verify help SNAP EBT page opened