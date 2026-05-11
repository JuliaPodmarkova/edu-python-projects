from xmlrpc.client import DateTime

import datetime

name = input("Привет, давай познакомимся!\nКак тебя зовут: ");
print("Рад познаклмится, " + name + ", меня зовут Питон");
print (name + ", напиши ниже в каком году вы родились: ");
dateOfBirth = int(input());

currentYear = 2024;
age = currentYear - dateOfBirth;
print("А сейчас я скажу сколько лет Вам будет в этом году: ", age);
if age > 0 and age <= 10:
    print(name + ", твой возраст такой классный! Играй сколько хочешь :)");
elif age > 10 and age < 18:
    print(name + ", твой возраст очень захватывающий, скоро будешь совсем взрослым!");
elif age >= 18 and age < 40:
    print(name + ", этот возраст по моему мнению прекрасен.");
else:
    print(name + ", тот возраст, когда можно все!");