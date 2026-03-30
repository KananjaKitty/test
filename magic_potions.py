potions = {
    "1": {
        "name": "big boy potion",
        "ingredients": ["muscle", "blood"]
    },
    "2": {
        "name": "evil potion",
        "ingredients": ["500 cigarretes", "pixie dust"]
    },
     "3": {
        "name": "bean potion",
        "ingredients": ["1 carrot", "elf teeth"]
    }
}

print("Whats gooooood take a looksy around vro!")
print("Heres what we got my guy:")
for key, p in potions.items():
    print(f"{key}. {p['name']}")
choice = input("What do you even wanttts?")

if choice in potions:
    selected = potions[choice]
    print(f"You chose: {selected['name']}")
    print("Ingredients required:")
    for ingredient in selected["ingredients"]:
        print(f"- {ingredient}")
    print(f"alright vro you wanted {selected['name']}...")
    for ingredient in selected["ingredients"]:
        print(f"buyin {ingredient}")
    print('There you go my guy!')
else:
        print("yo yo I don got nun o that")
