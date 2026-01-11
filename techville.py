def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

start_engine()
destination = input("Where do you want to go?")

# if destination == "library":
#     move_forward()
#     turn("left")
#     print("You have arrived at the library")
# #else:
#     #print("RAHHHHH BOOM BOOM POOF")

# if destination == "tech park":
#     move_forward()
#     turn("right")
#     print("You have arrived at the tech park")
# #else:
#    # print("RAHHHHH BOOM BOOM POOF")

# if destination == "hospital":
#     move_forward()
#     follow_roundabout(1)
#     print("You have arrived at the hospital")
# #else:
#    # print("RAHHHHH BOOM BOOM POOF")

# if destination == "mall":
#     move_forward()
#     follow_roundabout(2)
#     move_forward()
#     turn("right")
#     print("You have arrived at the mall")
# #else:
#    # print("RAHHHHH BOOM BOOM POOF")

# if destination == "airport":
#     move_forward()
#     follow_roundabout(3)
#     print("You have arrived at the mall")
# #else:
#   #  print("RAHHHHH BOOM BOOM POOF")

# if destination == "university" or destination == "stadium":
#     move_forward()
#     follow_roundabout(4)
#     move_forward()
#     if "university":
#         turn("left")
#         print("You have arrived at the university")
#     elif "stadium":
#         turn("right")
#         print("You have arrived at the stadium")
#     #else:
#        # print("RAHHHHH BOOM BOOM POOF")
# #else:
#   #  print("RAHHHHH BOOM BOOM POOF")


if destination == "library":
    move_forward()
    turn("left")
    print("You have arrived at the library")
elif destination == "tech park":
        move_forward()
        turn("right")
        print("You have arrived at the tech park")
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    if destination == "hospital":
        move_forward()
        follow_roundabout(1)
        print("You have arrived at the hospital")
    elif destination == "mall":
        move_forward()
        follow_roundabout(2)
        move_forward()
        turn("right")
        print("You have arrived at the mall")
    elif destination == "airport":
        move_forward()
        follow_roundabout(3)
        print("You have arrived at the airport")
    elif destination == "university":
        move_forward()
        follow_roundabout(4)
        turn("left")
        print("You have arrived at the university")
    elif destination == "stadium":
        move_forward()
        follow_roundabout(4)
        turn("right")
        print("You have arrived at the stadium")
else:
    print("WE'RE GONNA DIEEEE")