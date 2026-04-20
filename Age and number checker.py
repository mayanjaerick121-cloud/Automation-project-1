# Age and Number Checker Program
# This program checks a person's age category and performs number checks

def check_age(age):
    """
    Takes an age and returns the age category
    """
    if age < 0:
        return "Invalid age (negative)"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


def check_number(num):
    """
    Checks if a number is even, odd, positive, or negative
    """
    if num == 0:
        return "Zero"
    elif num > 0:
        if num % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    else:
        if num % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"


def main():
    print("=" * 50)
    print("Welcome to Age and Number Checker!")
    print("=" * 50)
    
    # Age checker
    print("\n--- Age Checker ---")
    try:
        age = int(input("Enter your age: "))
        age_category = check_age(age)
        print(f"You are a {age_category}")
    except ValueError:
        print("Please enter a valid number for age!")
    
    # Number checker
    print("\n--- Number Checker ---")
    try:
        number = int(input("Enter a number: "))
        number_type = check_number(number)
        print(f"Your number is: {number_type}")
    except ValueError:
        print("Please enter a valid number!")
    
    print("\n" + "=" * 50)
    print("Thank you for using the checker!")
    print("=" * 50)


if __name__ == "__main__":
    main()
