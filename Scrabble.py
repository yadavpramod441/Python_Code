# Assume that you are trying to complete a crossword puzzle. In a crossword puzzle, some letters are given and you have to figure out which complete word can you make out of it.
# For example, given letters "cwd"in the same order, you can make the word  "crossword" or "crowd" with it. But if "dw" is given in that order, you cannot make "crossword" out of it because d and w are in the opposite order here.

# You want to find an efficient method and write a code for this process. 
# The code will take two strings as input in two lines. The first string will contain letters on the crossword("cwd"), and the second string will contain a word that you want to check.(i.e. you want to check whether the word can be made out of given letters in the same order).
# The output should say "yes" if the word can be formed, else it should say "no"
# Sample Input 1:
# ccwd
# crossword
# Sample Output1:
# no

# Sample Input 2:
# cwd
# crossword
# Sample Output 2:
# yes


letters=input()#letters already in the crossword
guess=input()#word to check for fit
i = 0
for w in guess:
    if w == letters[i]: 
        i += 1
        if i >= len(letters): break

if (i == len(letters)):
    print('yes')
else:
    print('no')
