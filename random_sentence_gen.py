import random

subjects = [
    "john",
    "sam",
    "ram",
    "monkey",
    "cat",
    "minister",
    "dog",
]

action = [
    "launches",
    "cancels",
    "destroys",
    "orders",
    "celebrates",
    "dances with",
    "eats",
]

place_or_things = [
    "the moon",
    "the sun",
    "the earth",
    "the sky",
    "new york",
    "the white house",
    "mumbai",
    "india",
]

while True:
    subject = random.choice(subjects)
    act = random.choice(action)
    place_or_thing = random.choice(place_or_things)

    sentence = f"NEWS: {subject} {act} {place_or_thing}"
    print("\n"+ sentence)

    user_input = input("\n Do you want another sentence? (yes/no)").strip().lower()
    if user_input == "yes":
        continue
    elif user_input == "no":
        break

print("\n Thanks for using random sentence generator")