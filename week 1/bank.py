greet=input("Greeting:")
greet=greet.lower().strip()
if greet.startswith("h") and greet.startswith("hello"):
    print("$0")
elif greet.startswith("h") and not greet.startswith("hello"):
    print("$20")
else:
    print("$100")