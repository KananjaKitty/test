sentence = input("Please enter a sentence here: ")
sentence_formatted = sentence.strip().upper()

print(f"You said:  {sentence_formatted}")

paragraph = input("Can you please enter a paragraph? :3")
words = paragraph.split()
word_count = len(words)

print(f"That paragraph has {word_count} words.")

user_input = input("Please enter a string: ")
result =user_input.isdigit()

print(result)

Letter_change = input("Please enter another string baby boy:")
Letter_change_formatted = Letter_change.replace("a" , "o")

print(f"{Letter_change_formatted}")

name1 = input("Please enter your full name sir madam:")

name1_formatted = name1.capitalize() 
name_parts = name1.split()
initials = ""
for part in name_parts:
    initials += part[0].upper()
print("Initials:", initials)

text = input("Can you enter one more string handsome boy?")
print(len(text))
