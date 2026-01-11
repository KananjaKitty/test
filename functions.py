# def dollarizer(word):
#    return word.replace("s", "$")

# def eurizer(word):
#    return word.replace("e", "&")

# def replacer(word, char1, char2):
#     return word.replace(char1, char2)

# word = input("Enter a word: ")
# char1 = input("Enther the character to replace: ")
# char2 = input("Enter the replacement character: ")

# result = replacer(word, char1, char2)
# print("Result:", result)
     

# def wonky_text(word):
#      return (word
#              .replace("s", "$")
#              .replace("e", "%")
#              .replace("l", "*"))

# word = input("what is your name?")
# result = wonky_text(word)
# print("Result:", result) 






# celsius = float(input("What is the temperature in celsius?"))
# Fahrenheit = (celsius * 9/5) + 32

# print("The temperature in Fahrenheit is:", Fahrenheit)
 
# age_in_days = int(input("What is your age?"))
# age = (age_in_days * 365)

# print("Your age in days is:", age)




# P = int(input("What is the principal amount?"))
# R = int(input("What is the rate of interest?"))
# T = int(input("What is the time in years"))
# result =(P * R * T)
# print("Your simple interest is", result)

# plan finances -
P = float(input("Principal amount: "))
R = float(input("Interest rate: "))
T = float(input("Time in years: "))
result =(P * R * T)
print("Your simple interest is", result)

D = int(input("Your desired amount: "))

result2 = result <= D
print(f"Your estimated amount is {result2}")


