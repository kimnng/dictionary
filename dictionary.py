import json # JavaScript Object Notation
import difflib # difflib for comparing sequences.

data = json.load(open("data.json"))

def translate(word):
    """
    An interactive dictionary:
    Input  -  A word
    Output -  Returns meaning of the input word or suggest
              the closest match of the input word.
    """
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: # string.title() changes all 1st letter of each word in string to upppercase
        return data[w.title()]
    elif word.upper() in data: # string.upper() changes all letters of string to upppercase
        return data[w.upper()]
    else:
        list_of_keys = data.keys()
        filtered_list = difflib.get_close_matches(word, list_of_keys, n=3, cutoff=0.6)
        # difflib.get_close_matches(word, list_of_keys, n=3, cutoff=0.6) helps calculating
        # the similarity of word with every word in list_of_keys and return a list
        # of most matched words (default 3)
        if filtered_list == []:
            return "No such word. Please try again"
        else:
            suggested_word = filtered_list[0]
            prompted_question =  input('Did you mean ' + suggested_word
                                       + '? Type "Y" if yes, "N" if no: ')
            if prompted_question == 'Y':
                return data[suggested_word]
            elif prompted_question == 'N':
                return "Please try other word."
            else:
                return "Sorry, I don't understand."

word = input("Enter word: ")

output = translate(word)

if type(output) == list: # only print the definition results,
                        # not other results
    for item in output:
        print(item)
else:
    print(output)

