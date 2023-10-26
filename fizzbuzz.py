# add your code here
for number in range(1,101):
    if number % 3 == 0 and number % 4 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 4 == 0:
        print("Buzz")
    else:
        print(str(number))
