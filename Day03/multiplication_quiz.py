import random


first_number = random.randint(1, 5)
second_number = random.randint(1, 5)

try:
    answer = int(input(f"What is {first_number} x {second_number}? "))
except ValueError:
    print("Please enter a whole number.")
else:
    correct_answer = first_number * second_number
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Not quite. The answer is {correct_answer}.")
