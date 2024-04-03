# A game about an explorer
import time

# Add a delay of 5 seconds
time.sleep(5)

def biodata():
    name = input("what is your name")
    age  = input("what is your age:")
    gender = input("Are you male, female or prefer not to say?")
    exercise = input("Do you exercise regularly?")
    diet = input("Do you maintain a healthy diet?")
    meals = input("How many meals do you have in a day?")
    meals = float(meals)
    while meals<=2:
        meals = input("Which meals are a must have?")
    height = input("what is your height in meters:")
    height = float(height)
    while height>2.3:
        height = input("what is your height in meters (please confirm your answer):")
    weight = input("what is your weight in Kg")
    weight = float(weight)
    bmi = weight/height**2
    return name,age, gender,exercise,diet,meals,height,weight,bmi

print("Welcome explorer to our BMI game")
print("Let's get to know a little about you")
print('loading!!!')
time.sleep(5)
print("Are you excited, cause here we go; let's get to ask you some questions")
time.sleep(5)
print('loading!!!')
print("And remember, honesty pays dividends!!")
print('loading!!!')
time.sleep(5)
name,age, gender,exercise,diet,meals,height,weight,bmi = biodata()

def table(name,age, gender,exercise,diet,meals,height,weight,bmi):
    print("+-------------+-------------------+")
    print(f"| BIO DATA    |  VALUE            |")
    print("+-------------+-------------------+")
    print(f"| Your name:  |{name}")
    print("+-------------+-------------------+")
    print(f"|Your age is  |{age}")
    print("+-------------+-------------------+")
    print(f"|Your are a  |{gender}")
    print("+-------------+-------------------+")
    print(f"|Your exercise regimen is  |{exercise}")
    print("+-------------+-------------------+")
    print(f"|Your diet regimen is  |{diet}")
    print("+-------------+-------------------+")
    print(f"|The number of meals you eat is  |{meals}")
    print("+-------------+-------------------+")
    print(f"|Your height is  |{height}")
    print("+-------------+-------------------+")
    print(f"|Your weight is  |{weight}")
    print("+-------------+-------------------+")
    print(f"|Your bmi is  |{bmi}")
    print("+-------------+-------------------+")
print(table(name,age, gender,exercise,diet,meals,height,weight,bmi))

print("Great, now that we have some information, how's about some recommendations")

if bmi<18 and gender == "female" or "f" and meals<2:
    print("Dear Madam, you need to improve on diet: here are some fruits and food you can try")
    print('loading!!!')
    time.sleep(5)
    print("a banana, and pizza")
    
elif bmi<18 and gender == "male" or "m" and meals<2:
    print("Dude, you need to improve on diet: here are some fruits and food you can try")
    print('loading!!!')
    time.sleep(5)
    print("an apple and burger")

elif bmi<26 and exercise == "yes" or "y":
    print('loading!!!')
    time.sleep(5)
    print("Well done!! You are quite healthy keep on keeping on!")

elif bmi>26 and exercise == "no" or "n" and meals>2:
    print('loading!!!')
    time.sleep(5)
    print("Stop!! You are heading down a slippery slope, start exercising!")

else:
    print("you are quite fat")
    print('loading!!!')
    time.sleep(5)
    print("have you ever considered taking a walk")