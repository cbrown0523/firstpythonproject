students = ["Angel", "Brandon", "Claire", "Mona", "Alfredo"]
print("Are you a student/ Lets find out ...")
user_response = input("Are you a student? (yes/no)")
user_response_lower = user_response.lower().strip()
if user_response_lower == "n" or user_response_lower == "no":
    exit()
if user_response_lower == "y" or user_response_lower == "yes":
    user_response_name = input("What is your name ? ")
    if user_response_name in students:
        print("Welcome to the class")
    else:
        print("Your not suppose to be here")