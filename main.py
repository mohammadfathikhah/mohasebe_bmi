# ورودی از کاربر 
name = str (input("what is your name:"))
age = int(input("how old are you:"))
weight = int(input("How much do you weigh?:"))
may = float(input("how tall are you:"))
# محاسبه داده کاربر
may = may ** 2
bmi = weight / may
# نمایش نتایج محاسبات
print(f"hello sir  {name} ,your age  {age} ,your weight  {weight} ,your height  {may}")

bmi = bmi * 10000
print(f"your bmi {bmi}")
#نشاندادن وضعیت bmi کاربر
if bmi <= 18:
    print("low")
if bmi >= 18 and bmi <= 23: 
    print("ideal")
if bmi >= 23 and bmi <= 29:
    print("high")
if bmi >= 29 and bmi <= 39:
    print("very high!")
if bmi >= 39 and bmi <= 59:
    print("ektremely high!!!!")
