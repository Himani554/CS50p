from validator_collection import validators

email = input("What's your email address? ").strip()

try:
    isvalid = validators.email(email)
    print("Valid")
except:
    print("Invalid")



