# Game Rules

# Both players are given the same string,
# .
# Both players have to make substrings using the letters of the string

# .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string

# .

# For Example:
# String
# = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below


def minion_game(string):
    # your code goes here
    # Kevin only builds words out of vowels
    # Stuart only builds words out of constants 
    vowels = 'AEIOU'
    #Base score
    kev = 0
    stu= 0

    for i in range(len(s)):
        # checks if 'i' is in the vowels 
        if s[i] in vowels:
            # increments kevins score and drops the length of vowels by one
            kev += (len(s)-i)
        # if i is not in the vowels 
        else:
            # Add onto 
            stu += (len(s)-i)

    if kev > stu:
        print("Kevin", kev)
    elif kev < stu:
        print("Stuart", stu)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)