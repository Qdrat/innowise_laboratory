def generate_profile(current_age):
    if  0 < current_age <= 12:
        return 'Child'
    elif 13 <= current_age <= 19:
        return 'Teenager'
    elif 20 <= current_age :
        return 'Adult'
    else:
        return None

user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = int(2025 - birth_year)

hobbies = []
while True:
    value = input("Enter a favorite hobby or type 'stop' to finish: ")
    if value == 'stop':
        break
    hobbies.append(value)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "birth_year": birth_year,
    "current_age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies
}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['current_age']}")
print(f"Life Stage: {user_profile['life_stage']}")

if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])})")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby.capitalize()}")
print("---")

