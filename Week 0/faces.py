def convert(text):
    converted_text = text.replace(":)", "🙂")
    converted_text = converted_text.replace(":(", "🙁")
    return converted_text

def main():
    text = input("Input here: ")
    print(convert(text))

main()
