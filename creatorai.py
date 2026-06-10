# CreatorAI Dashboard (Vulnerable Version)

OPENAI_API_KEY = "sk-test-key"

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    print("\nLogin Successful")
else:
    print("\nAccess Denied")

thumbnail = input("\nEnter thumbnail filename: ")

print("\nThumbnail uploaded:", thumbnail)

email = input("\nEnter your email: ")

print("User email:", email)