# Created by felix at 3/15/2025
Feature: Target User Test Cases
  # Enter feature description here

# HW-3 Number 3
# HW-7 Number 1
  Scenario: New User can sign-in Target.com
    # Enter steps here
    Given Open Target Main Page
    When Click on Sign-In icon
    And Click on Second Sign-In icon
    Then Verify “Sign in or create account” message is shown
