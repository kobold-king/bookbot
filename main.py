def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(text)
    print(f" Total words =", word_count)
    print("Specific character counts:")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(book):
    words = book.split()
    return len(words)

def get_character_count(text):
# My original solution
   # lowered_string = text.lower()

    #final_count = {
        #"p": 0,
        #"c": 0,
        #" ": 0
    #}

   # for char in lowered_string:
       # if char == "p":
            #final_count["p"] += 1
        #elif char == "c":
            #final_count["c"] += 1
        #elif char == " ":
            #final_count[" "] += 1
# Correct solution that prints all letters and symbols
    final_count = {}

    for char in text:
        lowered_string = char.lower()
        if lowered_string in final_count:
            final_count[lowered_string] += 1
        else:
            final_count[lowered_string] = 1
    return final_count

main()
