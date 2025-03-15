# Created by felix at 3/8/2025
Feature: Target Search Test Cases
  # Enter feature description here

  Scenario: User can search for a product on Target.com
    # Enter steps here
    Given Open Target Main Page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown
