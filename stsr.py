#Question.1
# int("5")
# a =float(input("Enter same value:"))
# print(type(a),a)

#Question.2
# a =int(input("enter the first number:"))
# b =int(input("enter the second number:"))
# print("sum",a+b)

#Question.3
# a =int(input("Enter the square:"))
# print("your square",a*a*a)

#Question.4
# num1 =float(input("enter the first number:"))
# num2 =float(input("Enter the second number:"))

# print("this is a average",(num1+num2)/2)

#Question.5
# a =int(input("Enter the first number:"))
# b =int(input("Enter the second number:"))

# if(a>b):
#     print("True")

# elif(a<=b):
#     print("false")

#Question.6
# name =(input("Enter the name:"))
# age =(input("Enter the age:"))
# state =(input("Enter the state:"))

# print("my name is",name,"I am",age,"year old and I from",state)

#Question.7
# name =input("Enter the name:")
# age =int(input("Enter the age:"))
# state =(input("Enter the state:"))

# print(type(name))
# print(type(age))
# print(type(state))

#Question.8
# age=int(input("enter the age:"))
# old=input("enter the old:")
# a = None
# print(type(age))
# print(type(old))
# print(type(a))

#Question.9
       #trafic light code
# light =input("Enter the light color:")

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look") 
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")
    
#Question.9
     #grades of student

# marks = int(input("enter the marks:"))
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B") 
# elif(marks >= 70 and marks < 80):
#     print("C")
# elif(marks >= 60 and marks <70):
#     print("D")
# else:
#     print("marks is faild") 



















 
# import time
# count =int(input("Enter the counter num: "))
# print("\n countdown starts now: ")

# for i in range(1,0,-1):
#     print(i)
#     time.sleep(1)
#     print("\n whohoooo! happy new year")




# EXPENSE TRACKER PROJECT
expensesList=[] #list of expenses in form of dictionary
print("Welcome to Expense Tracker: ")
while True:
    print("___________MENU____________")
    print("1.Add Expenses")
    print("2.View all expenses")
    print("3.View total khrcha")
    print("2.exit")
    choice=int(input("please Enter your choice:"))

    # add expense
    if(choice == 1):
        date =input("kis date par khrcha kiya tha: ")
        category=input("kis type ka khrcha(food,travel,market,books)")
        decription=input("aur detail date:")
        amount =float(input("enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "decription":decription,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n done bro, expends is added successfull")

    # VIEW ALL EXPENSEN
    if(choice ==2):
        if(len(expensesList)==0):
            print("no expenses added.jao pehle khrcha karo")
        else:
            print("=====ye apka sara expense=====")
            count=1
            for eachkhrcha in expensesList:

                print(f"khrcha no{count}->{eachkhrcha['date']},{eachkhrcha['decription']},{eachkhrcha['amount']}")
                count=count+1

# 3.View total spending.
    elif(choice ==3):
        total=0
        for eachkrcha in expensesList:
            total =total + eachkrcha["amount"]
            print("\n total khrcha =",total)
# EXIT
    elif(choice ==4):
        print("thank you Mere System pe aneke liye")
        break
    else:
        print("INVALID CHOICE ,TRY AGAIN")

            






                



