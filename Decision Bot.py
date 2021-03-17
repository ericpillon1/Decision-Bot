#Decision Bot 
import random 
import statistics
from statistics import mode
lst = [] 
n = int(input("How many options do you have? "))
print("List your options")
for i in range (0, n): 
    ele = (input())
    lst.append(ele)
print("Your options are:", lst)

lst2 = []
draws = int(input("How many times should I pick with replacement? "))
i=0
while len(lst2) < draws :
    lst2.append(random.choice(lst))
    i += 1
    if i == draws:
        break
print(lst2)
print("The winner is", mode(lst2).capitalize(), "it was picked", lst2.count(mode(lst2)), "times out of", draws,".")

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()
elif ans.lower() == "y":
    lst3 = []
    i=0
    while len(lst3) < draws :
        lst3.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst3)
    print("The new winner is", mode(lst3).capitalize(), "it was picked", lst3.count(mode(lst3)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst4 = []
    i=0
    while len(lst4) < draws :
        lst4.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst4)
    print("The new winner is", mode(lst4).capitalize(), "it was picked", lst4.count(mode(lst4)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst5 = []
    i=0
    while len(lst5) < draws :
        lst5.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst5)
    print("The new winner is", mode(lst5).capitalize(), "it was picked", lst5.count(mode(lst5)), "times out of", draws)


ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst6 = []
    i=0
    while len(lst6) < draws :
        lst6.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst6)
    print("The new winner is", mode(lst6).capitalize(), "it was picked", lst6.count(mode(lst6)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst7 = []
    i=0
    while len(lst7) < draws :
        lst7.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst7)
    print("The new winner is", mode(lst7).capitalize(), "it was picked", lst7.count(mode(lst7)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst8 = []
    i=0
    while len(lst8) < draws :
        lst8.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst8)
    print("The new winner is", mode(lst8).capitalize(), "it was picked", lst8.count(mode(lst8)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst9 = []
    i=0
    while len(lst9) < draws :
        lst9.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst9)
    print("The new winner is", mode(lst9).capitalize(), "it was picked", lst9.count(mode(lst9)), "times out of", draws)
    
ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst10 = []
    i=0
    while len(lst10) < draws :
        lst10.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst10)
    print("The new winner is", mode(lst10).capitalize(), "it was picked", lst10.count(mode(lst10)), "times out of", draws)


ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst11 = []
    i=0
    while len(lst11) < draws :
        lst11.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst11)
    print("The new winner is", mode(lst11).capitalize(), "it was picked", lst11.count(mode(lst11)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst12 = []
    i=0
    while len(lst12) < draws :
        lst12.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst12)
    print("The new winner is", mode(lst12).capitalize(), "it was picked", lst12.count(mode(lst12)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst13 = []
    i=0
    while len(lst13) < draws :
        lst13.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst13)
    print("The new winner is", mode(lst13).capitalize(), "it was picked", lst13.count(mode(lst13)), "times out of", draws)

ans = input("Would you like to redo (Y or N)? ")
if ans.lower() == "n":
    print ("Enjoy your results!")
    exit()

elif ans.lower() == "y":
    lst14 = []
    i=0
    while len(lst14) < draws :
        lst14.append(random.choice(lst))
        i += 1
        if i == draws:
            break
    print(lst14)
    print("The new winner is", mode(lst14).capitalize(), "it was picked", lst14.count(mode(lst14)), "times out of", draws)