# -*- coding: utf-8 -*-
"""while loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PfhjnNqhPX4AFOqyPz-NOaTcFM5AlDB5

#### While.py
"""

# Creating initial variables
Total = 0
Count = 0

# To continuously ask user to enter a number

while True:

    user_input = input('Enter a number(enter -1 to stop):')

    # entry to stop the code

    if user_input == '-1':
      break

    # converting the input to a float and handling invalid inputs
    try:
        user2 = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Update total and count
    Total += user2
    Count += 1

# Calculating the average (excluding -1)
if Count > 0:
    average = Total / Count
    print(f"\nThe average of the entered numbers (excluding -1) is: {average:.2f}")
else:
    print("\nNo valid numbers were entered.")