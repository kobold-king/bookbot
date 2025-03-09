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

def sort_on(d):
    return d["num"]

def list_dict(character_count):
    sorted_list = []

    for char in character_count:
        sorted_list.append({"letters": char, "num": character_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
