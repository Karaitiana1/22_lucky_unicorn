show_instruction = input("have you played this game before?").lower()
if show_instruction == "yes" or show_instruction == "y":
    print("program continues")

elif show_instruction == "no" or show_instruction == "n":
    print("display instrtions")

else:
    print("error please enter yes or no")

