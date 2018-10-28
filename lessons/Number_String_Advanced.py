# !/usr/bin/env python
# -*- coding: utf-8 -*-


# Спосіб №1 -  .isdigit()
#
print
print "Example #1 (zoo ticket,  .isdigit)"
print
zoo_ticket_price = raw_input("Enter zoo ticket price: ")
if not zoo_ticket_price.isdigit():
   print ("You entered wrong price: '" + zoo_ticket_price + "'")
else:
   three_tickets_price = int(zoo_ticket_price) * 3
   print ("3 Zoo tickets costs: " + str(three_tickets_price))



# Спосіб №2 -  try..expept  для методу  int(..)
#
print
print "Example #2 (metro,  try..except)"
print
metro_ticket_price_str = raw_input("Input metro ticket price: ")
try:
    metro_ticket_price = int(metro_ticket_price_str)
    two_tickets_price = metro_ticket_price * 2;
    print("2 metro tickets costs: " + str(two_tickets_price))
except:
    print("You entered wrong metro price : '" + metro_ticket_price_str + "'")



###### Конвертація строк в числа - ускладнення логіки: Перепитати, якщо ввели неправильні дані
# Спосіб №1 + ускладнення логіки

print
print "Example #3 (zoo ticket,  .isdigit, repeat)"
print
zoo_ticket_price = raw_input("Input metro ticket price: ")
while (not zoo_ticket_price.isdigit()):
    print("Please, try again. You entered wrong temperature. Please, try again")
    zoo_ticket_price = raw_input("Input metro ticket price: ")
three_zoo_tickets_price = int(zoo_ticket_price) * 3
print("Three tickets to the ZOO costs " + str(three_zoo_tickets_price))


###### Конвертація строк в числа - ускладнення логіки: Перепитати, якщо ввели неправильні дані
# Спосіб №2 + ускладнення логіки

print
print "Example #4 (metro,  try..except,  repeat)"
print
metro_ticket_price = 0
while (metro_ticket_price <= 0):
    try:
        metro_ticket_price_str = raw_input("Input ZOO ticket price: ")
        metro_ticket_price = int(metro_ticket_price_str)

        three_tickets_price = metro_ticket_price * 3;
        print("Three ZOO tickets costs: " + str(three_tickets_price))
    except:
        print("Please, try again. You entered wrong number: ' " + metro_ticket_price_str + "'")

