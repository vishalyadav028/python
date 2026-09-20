secret = 7

num = int(input("Guess the number: "))

if num == secret:
    print("Correct! 🎉")
elif num > secret:
    print("Too high!")
else:
    print("Too low!")