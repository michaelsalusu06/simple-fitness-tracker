name = input("name: ")
age = int(input("age: "))
weight = int(input("weight: "))
height = int(input("height: "))
options = 0
workouts = []

def bmi(weight, height):
   res = weight / ((height / 100) * (height / 100))
   if res < 18.5:
       print("Your BMI score is ", res, "Underweight")

   elif res >= 18.5 and res <= 24.9:
       print("Your BMI score is ", res, "Healthy Weight")

   elif res >= 25.0 and res <= 29.9:
       print("Your BMI score is ", res, "Overweight")

   elif res >= 30.0:
       print("Your BMI score is ", res, "Obese")
   
while options != 4:
    print("1.Count your BMI")
    print("2.Add workouts to workout list")
    print("3.See your workout list")
    print("4.Exit")
    options = int(input("select options: "))

    if options == 1:
        bmi(weight, height)

    elif options == 2:
        wo = input("Input your workout here: ")
        workouts.append(wo)

    elif options == 3:
        print(workouts)

    elif options == 4:
        print("Have a good day!")

    else:
        print("Invalid option")