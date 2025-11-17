import datetime


def get_valid_name():
    while True:
        user_name = input('Enter your full name: ').strip()
        if not user_name:
            print("Error: Name cannot be empty! Please try again.")
        elif any(char.isdigit() for char in user_name):
            print("Error: Name cannot contain numbers! Please try again.")
        elif len(user_name) < 2:
            print("Error: Name is too short! Please try again.")
        elif len(user_name) > 50:
            print("Error: Name is too long! Please try again.")
        else:
            return user_name

def get_valid_birth_year():
    while True:
        birth_year_str = input('Enter your birth year: ')
        try:
            birth_year = int(birth_year_str)
            current_year = datetime.datetime.now().year

            # Проверяем, что год рождения не в будущем и не слишком старый
            if birth_year > current_year:
                print("Error: Birth year cannot be in the future! Please try again.")
            elif birth_year < current_year - 120:  # Предполагаем максимальный возраст 120 лет
                print("Error: Please enter a valid birth year! Please try again.")
            else:
                return birth_year
        except ValueError:
            print("Error: Please enter a valid number for birth year! Please try again.")

def generate_profile(current_age):
    if  0 < current_age <= 12:
        return 'Child'
    elif 13 <= current_age <= 19:
        return 'Teenager'
    elif 20 <= current_age :
        return 'Adult'
    else:
        return None

def list_of_hobbies():
    hobbies = []
    while True:
        value = input("Enter a favorite hobby or type 'stop' to finish: ")
        if value.lower() == 'stop':
            break
        if not value:
            print("Error: Hobby cannot be empty! Please try again.")
            continue
        if value in hobbies:
            print(f"Error: You already added '{value}'! Please enter a different hobby.")
            continue

        hobbies.append(value)
    return hobbies

def print_profile_summary(user_profile):
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
            print(f"- {hobby}")
    print("---")

def main():
    try:
        user_name = get_valid_name()
        birth_year = get_valid_birth_year()
        current_age = datetime.datetime.now().year - birth_year

        hobbies = list_of_hobbies()

        life_stage = generate_profile(current_age)

        user_profile = {
            "name": user_name,
            "birth_year": birth_year,
            "current_age": current_age,
            "life_stage": life_stage,
            "hobbies": hobbies
        }

        print_profile_summary(user_profile)

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")

    except Exception as e:
        error_msg = f"Unexpected error in main: {e}"
        print(f"\n{error_msg}")
        print("Please try running the program again.")


if __name__ == "__main__":
    main()
