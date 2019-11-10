import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def get_key(data):
    search_word = input()
    lower_search_w = search_word.lower()
    title_search_w = search_word.title()
    upper_search_w = search_word.upper()
    keys = data.keys()
    print('Enter a word you would like to search for: ')
    if lower_search_w in keys:
        return '{} is defined as: '.format(lower_search_w.title()) + '\n{}'.format(data[lower_search_w])
    elif title_search_w in keys:
        return '{} is defined as: '.format(title_search_w) + '\n{}'.format(data[search_word])
    elif upper_search_w in keys:
        return '{} is defined as: '.format(upper_search_w) + '\n{}'.format(data[search_word])
    elif len(get_close_matches(lower_search_w, data.keys())) > 0:
        yes_no = input("Did you mean to type {}? Enter 'y' for yes or 'n' for no: "
                     .format(get_close_matches(lower_search_w, data.keys())[0]))
        yes_no = yes_no.lower()
        if yes_no == 'y':
            return data[get_close_matches(lower_search_w, data.keys())[0]]
        elif yes_no == 'n':
            print('Please re enter your chosen word: ')
            get_key(data)
    else:
        print('That word is not in the dictionary.')
        print('Please enter another word.\n ')
        get_key(data)

to_string = get_key(data)

if type(to_string) == list:
    for definition in to_string:
        print(definition)
else:
    print(to_string)
