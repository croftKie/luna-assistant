import json

print("Welcome to Luna Assistant Setup")
print("In here you can set your name, and other related settings")

user_name = input("What is your name:")
ai_name = input("What is your assistant's name:")

dictionary = {
    "user_name" : user_name,
    "ai_name" : ai_name
}

json_obj = json.dumps(dictionary, indent=4)

with open("vars.json", "w") as outfile:
    outfile.write(json_obj)