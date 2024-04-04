# from single_human_generator import generate_human

# print(generate_human())
import random

world_num = random.randint(0, 12)
addition = ""
if world_num == 4:
    addition += "(angel " + str(random.randint(1, 4)) + ")"
print("Daddy, Please tell me the story of world: " + str(world_num) + " " + addition)
