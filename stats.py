def count_words(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count +=1

    return word_count

def count_characters(text):
    character_count = 0
    dict_of_characters = {}

    for character in text:
        lc_character = character.lower()
        if lc_character in dict_of_characters:
            dict_of_characters[lc_character] += 1
        else:
            dict_of_characters[lc_character] = 1

    return dict_of_characters

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    sorted_list=[]

    for character in dictionary.keys():
        sorted_list.append(dict(name=character, num=dictionary[character]))

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list