'''
Problem 7: Count Vowels & Consonants

• Write a program that counts the number of
vowels and consonants in a given string, with
letters in the English alphabet
– Hint: The vowels are: a/A, e/E, i/I, o/O or u/U and
the consonants are all of the other letters

• You can use any user interface that you like,
but the user must be able to continuously
enter strings to be analyzed

• Make sure that you attempt to handle
all/some error cases
'''

def count_vowels_and_consonants(phrase):
    #string of all the vowels (upper and lower case bc case sensitive)
    #can also approach by putting letters into a list but I'm too lazy to type everything out and write individual strings
    #vowels = (["a","e",...])
    vowels = "aeiouAEIOU" 
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" #string of all other letters in the alphabet (upper and lower case again)
    
    #Initializing the count for both vowels and consonants
    vowel_count = 0
    consonant_count = 0

    #Loop through each character in phrase
    for char in phrase:
        if char in vowels: #checks if the character is a vowel
            vowel_count += 1 #increases the vowel count
        elif char in consonants: #checks if the character is a consonant
            consonant_count += 1 #increases the consonant count

    return vowel_count, consonant_count #returns count of vowels and consonants

phrase = input("Enter a string: ") #User input -> asking to enter a string

# Calls the function to count vowels and consonants in the input phrase
vowel_count, consonant_count = count_vowels_and_consonants(phrase)

#Displays the number of vowels and consonants in the string
print("Number of vowels in the phrase:", vowel_count) 
print("Number of consonants in the phrase:", consonant_count) 


