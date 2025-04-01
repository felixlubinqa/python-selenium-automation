# Created by felix at 3/15/2025
Feature: Target User Test Cases
  # Enter feature description here

# HW-3 Number 3
  Scenario: New User can sign-in Target.com
    # Enter steps here
    Given Open Target Main Page
    When Click on Sign-In icon
    And Click on Second Sign-In icon
    Then Verify “Sign into your Target account” message is shown
