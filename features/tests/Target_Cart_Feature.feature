# Created by felix at 3/20/2025
Feature: Target Cart Related Features
  # Used for functionality of Cart on Target.com

  #HW-7
Scenario: Target Cart Functionality
  # Enter steps here
  Given Open Target Main Page
  When Click on Add to cart icon
  When Click on Add to cart icon on side
  Then Verify “Added to Cart” message is shown on side page
  When Click on View Cart icon
  Then Verify item added to cart

# HW-6 Updated
Scenario: Verify “Your cart is empty” message is shown
  # Enter Steps Here
  Given Open Target Main Page
  When Click on cart icon
  Then Verify “Your cart is empty” message is shown