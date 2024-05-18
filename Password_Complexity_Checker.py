import re

#Define criteria for password strength
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.match(r'^[a-zA-Z0-9]*[!@#$%^&*()_+}{":?><,./;\'\[\]]', password))

    # Calculate strength score based on criteria met
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback based on strength score
    if strength_score == 5:
        return "Very Strong: Your password meets all criteria."
    elif strength_score >= 3:
        return "Strong: Your password meets most criteria."
    elif strength_score >= 2:
        return "Moderate: Your password meets some criteria."
    elif strength_score == 1:
        return "Weak: Your password meets minimal criteria. Consider adding more characters, numbers, or special characters."
    else:
        return "Very Weak: Your password does not meet any of the criteria. Please choose a stronger password."

#This function checks the length of a password and returns True if it is greater than or equal to 8 characters, and False otherwise.
def check_password_length(password):
    if len(password) >= 8:
        return True
    else:
        return False
    
#This function run the whole program
def main():
    print("\n---------------------------------------*Password Complexity Checker And Give Feedback Of Your Password*---------------------------------------")
    print("\n------------------------------------------------------------ By Birju Kansara ----------------------------------------------------------------")

    print("\nWelcome to the Password Strength Assessment Tool!")
    while True:
        password = input("\nEnter your password to assess its strength (or type exit): ")
        if check_password_length:
            result = assess_password_strength(password)
        
        if password.lower() == 'exit':
            print("Goodbye!")
            break
        strength_feedback = assess_password_strength(password)
        print("\nStrength Assessment:\n", strength_feedback)

# this code checks if the script is being run directly, and if so, it calls the main() function.
if __name__ == "__main__":
    main()
