# File: q2.py
# Author: Angel Valdez
# Date: 10/24/19
# Section: 502
# E-mail: angelval@tamu.edu
# Description:This program takes a DNA sequence and pattern lenght and finds the most common patterns in the sequence. The program imports a function from collections.py called Counter which counts how many times an item is repeated on a list. The variable sequence is equivalent to the input DNA sequence from the user. The variable pattern_lenght is equivalent to the input integer from the user that will determine how long each pattern will be. The variable end is equivalent to the lenght of the input DNA sequence. The variable DNA is equivalent to an empty list in which the patterns will added. The variable temporary_list is equivalent to an empty list in which keys that have a value equal to 1 will be appended. The first for loop slices the characters in the variable sequence according to the specified lenght by th user and appends them to the DNA list. The variable DNA_patterns is equivalent to the Counter function which counts how many times a pattern is repeated based on the DNA list which will then be stored in a dictionary with the pattern as key and the times it repeats as a value. The next for loop creates the variables key and value in DNA_patterns.item(). If the value is equal to 1 it appends the key(DNA pattern) to the list temporary_list. The next for loop gets the key from the list temporary_list and looks for it in the dictionary DNA_patterns. If the key is present in the dictionary it deletes it. In short the third for loop eliminates any DNA patterns that are not repeated. The program then prints on the screen "Most frequent pattern of length" followed by the specified lenght of pattern from the user. The program then executes a fourth loop in which it only prints the keys remaining in the dictionary DNA_patterns which are the most frequent keys.

from collections import Counter
sequence = input("Enter DNA Sequence Here:")
pattern_lenght = int(input("Enter pattern lenght here:"))

end = len(sequence)
DNA =[]
temporary_list = []

for i in range(0,end):
    DNA.append(sequence[i:i+pattern_lenght])

DNA_patterns = dict(Counter(DNA))

for key,value in DNA_patterns.items():
    if value == 1:
        temporary_list.append(key)
        
for key in temporary_list:
    if key in DNA_patterns:
        del DNA_patterns[key]

print(" ")
print("Most frequent pattern of length", pattern_lenght,":")
for key in DNA_patterns:
    print(key)
