# !/usr/bin/env python
# -*- coding: utf-8 -*-


#
# Check that variable is type string

def message(message):
    print
    print
    print message


#   int(some_text_here)  -- конвертація в ціле число
#   float(text_here)  -- конвертація в число з плаваючою точкою
#   str(some_number)  -- конвертація в текст
#   type (current_year) is str  -- перевірити що змінна - типу строка
#   type (current_year) is int  -- перевірити що змінна - типу число


# Check that variable is type string
message("Example #1")

current_year = "2018"
if (type (current_year) is str ):
    print ("That '2018' was a type string")



# Check that variable is a number
message ("Example #2      type(month) is int")

month = 12
if (type (month) is int ):
    print ("That '12' was a type int")


#########       int --> string    ###########
message("Example #3     int --> string")

zoo_ticket_price = 100
print ("2 ice creams metro ticket's costs: " + str(zoo_ticket_price*2))


message("Example #4     int --> string --> int ")

price = 8
priceAsNumber = int(price)
two_tickets_number = priceAsNumber * 2
two_tickets_string = str(two_tickets_number)
print ("2 metro ticket's costs: " + two_tickets_string)
print


message("Example #5     float --> string")

weight = 35.3
print ("2 students weight: " + str(weight*2))
print


message("Example #6     string --> int --> string")

metro_ticket_price = raw_input("Please input metro ticket price: ")
price_int = int(metro_ticket_price)
two_tickets_costs = price_int * 2
# Конвертація результату (числа) в строчку
print ("Two tickets costs: " + str(two_tickets_costs))

