# from single_human_generator import generate_human

# print(generate_human())
import random

print("age of kid: " + str(random.randint(6, 16)))
print("sex of kid: " + str(random.choice(["Male", "Female"])))
print("how much does the kid read hours?: " + str(random.randint(0, 4)))
print(
    "what does they mainly read?: " + str(random.choice(["Fun", "learning", "other"]))
)
