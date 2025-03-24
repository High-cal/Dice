import random

dice_types = {
        "d6": [1, 2, 3, 4, 5, 6],
        "d8": [1, 2, 3, 4, 5, 6, 7, 8],
        "d10": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "d12": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "d20": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
}

dice = input("Which dice do you wanna roll (d6-d20): ").lower().strip()

if dice in dice_types:
    result = random.choice(dice_types[dice])
    print(f"You Rolled: {result}")
else:
    print("Invalid dice type. Please choose from d6, d10, d20")
