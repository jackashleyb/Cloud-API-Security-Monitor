# Cloud API Security Monitor


user_input = input("Enter text: ")

if "password" in user_input:
    print("Possible secret leak")
else:
    print("No obvious threat")