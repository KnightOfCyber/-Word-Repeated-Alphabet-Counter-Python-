def count_words(text):
    return len(text.split())

def count_repeated_letters(text):
    letter_count = {}

    for char in text.lower():
        if char.isalpha():   # ignore spaces, numbers, symbols
            letter_count[char] = letter_count.get(char, 0) + 1

    # keep only repeated letters
    repeated_letters = {
        letter: count
        for letter, count in letter_count.items()
        if count > 1
    }

    return repeated_letters

def main():
    print("Word Count + Automatic Repeated Alphabet Counter")

    text = input("\nEnter a sentence or paragraph:\n")

    if not text.strip():
        print("Empty input. Nothing to analyze.")
        return

    total_words = count_words(text)
    repeated_letters = count_repeated_letters(text)

    print("\nResults:")
    print(f"Total words: {total_words}")

    if repeated_letters:
        print("\nRepeated alphabets:")
        for letter, count in sorted(repeated_letters.items()):
            print(f"{letter} : {count}")
    else:
        print("\nNo repeated alphabets found.")

if __name__ == "__main__":
    main()
