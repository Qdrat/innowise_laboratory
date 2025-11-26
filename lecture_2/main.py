"""
User Profile Generator

This script collects user information including name, birth year, and hobbies,
then generates and displays a profile summary including their life stage.
"""


def generate_profile(age):
    """
        Determine life stage based on age.

        Args:
            age (int): The current age of the user

        Returns:
            str: Life stage category or None for invalid ages
        """
    if  0 < age <= 12:
        return 'Child'
    if 13 <= age <= 19:
        return 'Teenager'
    if 20 <= age :
        return 'Adult'
    return 'Unknown'

def main():
    """Main function to run the user profile generator."""
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

if __name__ == "__main__":
    main()
