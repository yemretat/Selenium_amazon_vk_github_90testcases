Feature: Test that pages have correct content
  #4 + | + |        2
  #5 + +  |   |     2
  #6 + + +  ++ | + + +  |   8
  #7 + + + | + + +  | + +     8
  #8 + + + | + +  +  + + + + +  | +    12
  #9 + + +  ++  |  + + + + +  | + + + + 14
  #10  + | +  + + +  | + + + + + +  11
  #11  ++ + | + + +  | + ++ +  +++  13
  #12 + + | +  | + + + +  7
  #13 + + | + | +  + + 6
  #14 +  + | + |    3
  #15   |   | + +   2
  # 18  |   | +   1
  #19  + |   |   1
#am1 : 123.01
  # 4-8    |||   9-11   || 12 -

# 8
#Scenario: Try to make comment unpurchased product
#  Given I am on the Amazon entrance page
#  When I click the accept_cookies
#  When I press the Cok Satanlar Button
#  Then I am on the Amazon cok satanlar page
#  When I add the products
#  When Make a comment
#  When I enter "yemretat99@gmail.com" in the "email" field
#  When I enter "Amazon1999" in the "password" field
#  When I press the "signInSubmit" idli button

#5

#Scenario: Make a list
#  Given I am on the Amazon entrance page
#  When I select the Account and Lists to Login
#  When I enter "yemretat99@gmail.com" in the "email" field
#  When I press the "continue" idli button
#  When I enter "Amazon1999" in the "password" field
#  When I press the "signInSubmit" idli button
#  When I select the Account and Lists to Make a list
#  When I make a list

 #0
#  Scenario: Account Information Control and some changes
#   Given I am on the Amazon entrance page
#   When I select the Account and Lists to Login
#   When I enter "yemretat99@gmail.com" in the "email" field
#   When I press the "continue" idli button
#   When I enter "Amazon1999" in the "password" field
#   When I press the "signInSubmit" idli button
#   Then User name is displayed after Login
#   When I select the Account and Lists to my Account
#   When Login and Security open
#   When Update Buttons Enter
#   When New Name Change "Yunus Emre"



#5
# Scenario: Login page has a correct title
#    Given I am on the Amazon entrance page
#    When I click the accept_cookies
#    Then There is a Teslimat Adres button
#    When I press the Cok Satanlar Button
#    Then I am on the Amazon cok satanlar page
#    When I add the products
#    When I click the Card Button
#    When Click the Card Image
#    When Complete the shopping
#    When I enter "yemretat99@gmail.com" in the "email" field
#    When I press the "continue" idli button
#    When I enter "Amazon1999" in the "password" field
#    When I press the "signInSubmit" idli button


#0 sn
# Scenario: Login and Display the Orders
#  Given I am on the Amazon entrance page
#  When I select the Account and Lists to Login
#  When I enter "yemretat99@gmail.com" in the "email" field
#  When I press the "continue" idli button
#  When I enter "Amazon1999" in the "password" field
#  When I press the "signInSubmit" idli button
#  Then User name is displayed after Login
#  When I select the Account and Lists to Siparislerim
#  Then Orders "sipariş vermediniz" message is displayed


# 3  + 4 = 7
#Scenario: Search Bar and Filtering
#  Given I am on the Amazon entrance page
#  When I click the accept_cookies
#  When I enter the "dell bilgisayar" in the search bar field
#  When I press the search button
#  When I press the min value "5000"
#  When Go to the min value
#  Then The min value is "5000"
#  Then Searched product "dell bilgisayar"

#0 sn

#Scenario: Login and Logout
#  Given I am on the Amazon entrance page
#  When I select the Account and Lists to Login
#  When I enter "yemretat99@gmail.com" in the "email" field
#  When I press the "continue" idli button
#  When I enter "Amazon1999" in the "password" field
#  When I press the "signInSubmit" idli button
#  Then User name is displayed after Login
#  Then I am on the Amazon entrance page
#  When I logout from the hidden

#2

# Scenario: Register the Amazon
#   Given I am on the Amazon entrance page
#   When I select the Account and Lists to Register
#   When I enter "Yunus Emre Tat" in the "customerName" field
#   When I enter "ahmethaciyatmaz141@gmail.com" in the "email" field
#   When I enter "Amazon1999" in the "password" field
#   When I enter "Amazon1999" in the "password" field
#   When I press the "continue" idli button





# 1sn
 # Scenario: Login page has a correct title
 #   Given I am on the Amazon entrance page
 #   Then There is a Teslimat Adres button
 #   When I click the Teslimat Adresini Secin
 #   When I click the Address Content
 #   When I enter "yemretat99@gmail.com" in the "email" field
 #   When I press the "continue" idli button
 #   When I enter "Amazon1999" in the "password" field
 #   When I press the "signInSubmit" idli button
 #   Then User name is displayed after Login

  #15
 # Scenario: Login page has a correct title
 #   Given I am on the Amazon entrance page
 #   When I click the accept_cookies
 #   Then There is a Teslimat Adres button
 #   When I press the Cok Satanlar Button
 #   Then I am on the Amazon cok satanlar page
 #   When I add the products
 #   When I press the buy now button Satin Al
 #   When I enter "yemretat99@gmail.com" in the "email" field
 #   When I press the "continue" idli button
 #   When I enter "Amazon1999" in the "password" field
 #   When I press the "signInSubmit" idli button
 #   When I enter the "Yunus Emre Tat" "address-ui-widgets-enterAddressFullName" idli text
 #   When I enter the "İstanbul" "address-ui-widgets-enterAddressCity" idli text
 #   When I enter the "Pendik" "address-ui-widgets-enterAddressStateOrRegion" idli text
 #   When I enter the "Yenişehir Mh." "address-ui-widgets-enterAddressDistrictOrCounty" idli text
 #   When I enter the "Yenişehir mah dedepaşa cad" "address-ui-widgets-enterAddressLine1" idli text
 #   When I enter the "parklife sitesi c blok daire 16" "address-ui-widgets-enterAddressLine2" idli text
 #   When I enter the "5079791728" "address-ui-widgets-enterAddressPhoneNumber" idli text
 #   Then I click the checkbox

  #5sn
  #Scenario: Login page has a correct title
  #  Given I am on the Amazon entrance page
  #  When I click the accept_cookies
  #  Then There is a Teslimat Adres button
  #  When I press the Cok Satanlar Button
  #  Then I am on the Amazon cok satanlar page
  #  When I add the products
  #  When I press the buy now button Satin Al
  #  When I enter "yemretat99@gmail.com" in the "email" field
  #  When I press the "continue" idli button
  #  When I enter "Amazon1999" in the "password" field
  #  When I press the "signInSubmit" idli button
