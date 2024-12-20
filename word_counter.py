
def word_counter():
    text = input("Enter a text: ")
    word_count = len(text.split())
    char_count = len(text)
    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")

word_counter()
