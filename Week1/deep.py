# prompts the user for the answer to the Great Question of Life, the Universe and Everything?

ans = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two

match ans:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

# Else output no
