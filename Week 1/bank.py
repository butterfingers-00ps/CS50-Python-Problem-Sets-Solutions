# prompts the user for a greeting
ans = input("Greeting: ").strip().lower()
# If the greeting starts with “hello”, output $0.
if ans.startswith("hello"):
    print("$0")
# If the greeting starts with an “h” (but not “hello”), output $20.
elif ans.startswith("h"):
    print("$20")
#Otherwise, output $100
else:
    print("$100")
