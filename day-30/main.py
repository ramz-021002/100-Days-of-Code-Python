height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilograms: "))
if height > 3.0:
    raise ValueError("Your height is too high! A regular human height does not exceed 3.0 metres.")
bmi = weight / (height * height)
print("Your BMI is:", bmi)

file = None
try:
    file = open("a_file.txt")
    # dict_1 = {"1": "One"}
    # dict_1 = {"1": "One", "2": "Two"}
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Starting data into the file')
except KeyError as error_message:
    print(f"The key {error_message} was not found")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("I made this up lol")