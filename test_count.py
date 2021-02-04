import Count

#initialization of Dictionaries for Testing
z_flag_dict  = {'a': 2,
 'b': 2,
 'c': 2,
 'd': 2,
 'e': 2,
 'f': 2,
 'g': 0,
 'h': 0,
 'i': 0,
 'j': 0,
 'k': 0,
 'l': 0,
 'm': 0,
 'n': 0,
 'o': 0,
 'p': 0,
 'q': 0,
 'r': 0,
 's': 0,
 't': 0,
 'u': 0,
 'v': 0,
 'w': 0,
 'x': 0,
 'y': 0,
 'z': 0}

l_flag_dict = {'a':2}
c_flag_dict = {'a':1,'A':1,'B':1,'b':1,'C':1,'c':1,'D':1,'d':1,'E':1,'e':1,'F':1,'f':1}
no_flag_dict = {'a':2,'b':2,'c':2,'d':2,'e':2,'f':2}

#Testing the flags using Test1 and Test2 text files
assert (Count.main(['-z','Test1.txt','Test2.txt']) == z_flag_dict), '-z flag incorrect'
assert (Count.main(['-l', 'a','Test1.txt','Test2.txt'])== l_flag_dict), '-l flag incorrect'
assert (Count.main(['-c','Test1.txt','Test2.txt']) == c_flag_dict), '-c flag incorrect'
assert (Count.main(['Test1.txt','Test2.txt']) == no_flag_dict), 'No flag incorrect'
print('All Test Cases Passed')
