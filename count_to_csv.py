import Count
import csv
import sys

#Initializing variables
arg_list = sys.argv
file_path =  arg_list[-1]

#Finds csv in given string
if ('.csv' in file_path) == False:
        raise ValueError('Your outfile is not a csv')

final_dict = Count.main(arg_list)

#Writing the csv
with open(file_path, 'w') as f:
    for key in final_dict.keys():
        f.write("%s,%s\n"%(key,final_dict[key]))
