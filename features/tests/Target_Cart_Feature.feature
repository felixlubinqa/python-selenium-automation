# Created by felix at 3/20/2025
Feature: Target Cart Related Features
  # Used for functionality of Cart on Target.com

#Scenario: User verify if Cart Page is active on Target.com
#  # Enter steps here
#  Given Open Target Main Page
#  When Click on cart icon
#  Then Verify “Your cart is empty” message is shown


Scenario: Target Cart Functionality
  # Enter steps here
  Given Open Target Main Page
  When Click on Add to cart icon
  When Click on Add to cart icon on side
  Then Verify “Added to Cart” message is shown on side page
  When Click on View Cart icon
  Then Verify item added to cart
