# !/usr/bin/env python
# -*- coding: utf-8 -*-

from my_message_module import message

#
print
print
print("Example  #1 -  Якщо .. то (if)")
#
address = "Kudryachova, 18"
if (address == "Kudryachova, 18"):
   print ("Wellcome to the class!")

print
print
print("Example  #2 - якщо ... то  ... інакше ...(if..else)")
#
fruit = "Orange"
if (fruit == "Orange"):
   print ("You like orange")
else:
   print ("You do not like orange")
print("")

# Вкладені умовні оператори

print
print
print("Example  #3 - Вкладені умовні оператори -  (if ..elif ..else)")
#
month = "November"
day = 30
if (month == "December"):
   if (day == 31):
       print ("Tonight is New Year")
   elif (day == 30):
       print ("Tomorrow is a New Year")
   else:
       print ("New Year is very soon")
else:
   print ("It is still autumn")
print("")
