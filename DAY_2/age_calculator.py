
from datetime import date

print("===== Age Calculator =====")

name = input("Enter your name: ")

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
    age = age - 1

print("\nHello", name)
print("You are", age, "years old")
print("Current Year is", today.year)