def turn(direction):
    print(f"turning {direction}")

def forward():
    print("Moving forward")

def turn2(direction2):
    print(f"turning {direction2}")



destination = input("You're trapped in an unstable lab that could blow up any second. Do you turn Left or Right?")

if destination == "Right":
    turn("Right")
    print("YOu run right into the reactor core and explode.")
    print("THE END :)")
elif destination == "Left":
    turn("Left")
    print("You run down a long passage and end up with 3 directions: Left, Right, and forward. Where do you go?")
  
    if destination == "Forward":
        forward 
        print("Congratulations! You found the exit and got out safely")
        print("THE END :)")
    elif destination == "left":
        turn2("left")
        print("You run into a dead end and the reactor finally blows up, you are incinerated instantly.")
        print("THE END :)")
    elif destination == "Right":
        turn2("Right")
        print("You find the secret ending and defeat Vecna. You take so long that the reactor blows up and you still die.")
        "THE END :)"