# Target is the number up to which we count
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            number = rint("Fizz")
        if number % 5 == 0:
            number = print("Buzz")
        else:
            print(number)

        

print(fizz_buzz(50))