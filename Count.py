#Author: Leo Dueker - 873542637

#Overview of Program:
# Count.py is intended to take in a single text file or multiple text files from a user and output each alpha characters frequency in
# a CSV format.  The Program also supports multiple flag options which modifies the output to the user's liking (such as distinguishing
# capital letters).The program is intended to work using command prompt for the user to provide the text files and selected flag option.



import sys
import numpy
from collections import Counter
import string


def add_frequencies(txt_file, dictionary = {}, remove_case = True):
    '''
    Add_Frequencies takes three parameters: txt_file, a dictionary, and remove_case as a boolean.  The function counts the
    characters in the given text file(s) and outputs a dictionary with the characters as keys and frequencies as values.
    Also included is a clean_string function which removes all of then non-alpha letters from the string so we only get a dictionary
    with alpha characters and thier frequencies
    '''

    # Setting variables
    old_dict = dictionary
    new_dict = {}
    open_file = open(txt_file, 'r').read()

    #Removing non alpha letters from string
    clean_string = ''.join([i for i in open_file if i.isalpha()])

    # Handling case logic
    clean_string = clean_string.lower() if remove_case else clean_string

    # Grabbing unique list of strings to be used as dictionary keys
    dict_keys = list(set(clean_string))

    # Cycling through all the keys in the dictionary and grabbing their frequency in the text file
    for i in dict_keys:

        sub_count = clean_string.count(i)
        new_dict[i] = sub_count

    final_dict = dict(Counter(new_dict) + Counter(old_dict))

    return(final_dict)

def main():

    #Creating List of Arguments
    arg_list = sys.argv

    # Grabbing all txt files from argv
    file_list = []

    for x in arg_list:
        if x.find('.txt') != -1:
            file_list.append(x)
        else:
            continue

    # Checking to see if there are more than one optional argument and throwing error if this is the case
    if ('-c' in arg_list) + ('-l' in arg_list) + ('-z' in arg_list) >1:
        raise ValueError('Provided too many optional arguments')

    # Handling Optional Flag case -c. Which uses the case sensitive add_frequencies method
    if '-c' in arg_list:

        #Creat initial dictionary
        dictionary_loop = {}

        #Cycling through the files
        for file in file_list:

            #Using Counter Method to merge two dictionaries which adds the values of common keys.
            dictionary_loop = add_frequencies(file, dictionary = dictionary_loop, remove_case = False)

        for i in dictionary_loop:
            print(f'"{i}",{dictionary_loop[i]}')

    elif '-z' in arg_list:


        # Dictionary Holding alphas with 0 values
        alpha_dict = dict.fromkeys(list(string.ascii_lowercase), 0)

        #Initalizing dictionary for file
        dictionary_loop = {}

        #Cycling through the files
        for file in file_list:

            dictionary_loop = add_frequencies(file, dictionary = dictionary_loop, remove_case = True) #Using Counter Method to merge two dictionaries which adds the values of common keys.

        # Updating alphabet dictionary with our updated frequencies
        alpha_dict.update(dictionary_loop)

        # Printing in CSV
        for i in alpha_dict:
            print(f'"{i}",{alpha_dict[i]}')


    elif '-l' in arg_list:

        # Grabbing argument occuring after -l argument
        text_pos  = arg_list.index('-l') + 1
        text_filter = list(arg_list[text_pos].lower())

        #Initalizing dictionary for file
        dictionary_loop = {}

        #Cycling through the files
        for file in file_list:

            dictionary_loop = add_frequencies(file, dictionary = dictionary_loop, remove_case = True) #Using Counter Method to merge two dictionaries which adds the values of common keys.

        # Filtering final dictionary to only include our letters
        filtered_dict = { key: dictionary_loop[key] for key in text_filter}

        # Printing in CSV
        for i in filtered_dict:
            print(f'"{i}",{filtered_dict[i]}')

    else:

        #Initalizing dictionary for file
        dictionary_loop = {}

        #Cycling through the files
        for file in file_list:

            dictionary_loop = add_frequencies(file, dictionary = dictionary_loop, remove_case = True) #Using Counter Method to merge two dictionaries which adds the values of common keys.

        # Printing in CSV
        for i in dictionary_loop:
            print(f'"{i}",{dictionary_loop[i]}')

if __name__ == '__main__':
   main()
