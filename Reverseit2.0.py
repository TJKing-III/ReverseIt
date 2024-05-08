word = str(input("What Phrase would you like me to Reverse"))#set a variable to the user input
reversed_word = word[::-1]#sets a variabkle to the reverse oif the user input
vowels_amount = 0#sets the variable to 0
constant_amount = 0#sets the variable to 0
length = len(word)#fins the length of the word
print(reversed_word)#printds the reversed word
vowels = ['a','e','i','o','u']#creastes an arrau of vowels
constants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']#makes an array of constants
for char in word.lower():#for every charcter in the word
    if char in vowels:#checks if the chosen charcter is in the vowels array
        vowels_amount = vowels_amount + 1#adds  a value to the ampount of vowels
    elif char in constants:#anything else
        constant_amount = constant_amount + 1#adds one to the constant amount
print(str(vowels_amount) + " Vowels")#prints tghe amount of vowels
print(str(constant_amount) + " Constants")#prints the amount of constants
