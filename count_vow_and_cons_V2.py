#ChatGPT was used for guidance on incorportating error handling into the code

def count_vowels_and_consonants(phrase):
    #string of all the vowels (upper and lower case bc case sensitive)
    #can also approach by putting letters into a list but I'm too lazy to type everything out and write individual strings
    #vowels = (["a","e",...])
    vowels = "aeiouAEIOU" 
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

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

# Create an infinite loop to keep asking for input
while True:
    phrase = input("Enter a string: ") #User input -> asking to enter a string
    
    # Check if the input is not empty
    if not phrase:
        print("Input is empty. Please enter a valid string.")
        continue

    #Check if the input contains only alphabet letters and spaces
    #If it doesn't contain only alphabet letters, the code considers the input as containing non-alphabet characters and displays an error message. 
    '''
    -> phrase.replace(' ', '') 
        - replaces all spaces in the phrase with an empty string ('').
        - basically removes all the spaces from the phrase
    -> .isalpha() 
        - returns True if all the characters in the string are alphabet letters (A-Z or a-z)
        - returns False if the string contains any non-alphabet characters
    '''
    if not phrase.replace(' ', '').isalpha():
        print("Input contains non-alphabet characters. Please enter letters and spaces only.")
        continue

    # Call the function to count vowels and consonants in the input phrase
    vowel_count, consonant_count = count_vowels_and_consonants(phrase)

    #Displays the number of vowels and consonants in the string
    print("Number of vowels in the phrase:", vowel_count) 
    print("Number of consonants in the phrase:", consonant_count) 
    
    another = input("Do you want to enter another string? (yes/no): ") #Asks user if they want to try again
    
    if another.lower() != "yes": # is user response is not "yes" then exit the loop
        break
