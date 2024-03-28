# A game about an explorer
import time

# Add a delay of 5 seconds
time.sleep(5)

def biodata():
    name = input("what is your names")
    age  = input("what is your age:")
    height = input("what is your height in meters:")
    height = float(height)
    while height>2.3:
        height = input("what is your height in meters (please confirm your answer):")
    weight = input("what is your weight in Kg")
    weight = float(weight)
    bmi = weight/height**2
    return name,age, height,weight,bmi

print("welcome explorer to our BMI game")
print('loading!!!')
time.sleep(5)
print("we shall ask you afew questions to get to know you")
time.sleep(5)
print('loading!!!')
print("please aswer the questions as truthfully as possible!!")
print('loading!!!')
time.sleep(5)
name,age,height,weight,bmi = biodata()

def table(name,age,height,weight,bmi):
    print("+-------------+-------------------+")
    print(f"| BIO DATA    |  VALUE            |")
    print("+-------------+-------------------+")
    print(f"| Your name:  |{name}")
    print("+-------------+-------------------+")
    print(f"|Your age is  |{age}")
    print("+-------------+-------------------+")
    print(f"|Your height is  |{height}")
    print("+-------------+-------------------+")
    print(f"|Your weight is  |{weight}")
    print("+-------------+-------------------+")
    print(f"|Your bmi is  |{bmi}")
    print("+-------------+-------------------+")
print(table(name,age,height,weight,bmi))

if bmi<18:
    print("Hi skinny: here are some fruits and food you can try")
    print('loading!!!')
    time.sleep(5)
    print("a banana, and pizza")
    
elif bmi<26:
    print('loading!!!')
    time.sleep(5)
    print("Yah! you are healthy keep on keeping on!")
else:
    print("you are quite fat")
    print('loading!!!')
    time.sleep(5)
    print("have you ever considered taking a walk")