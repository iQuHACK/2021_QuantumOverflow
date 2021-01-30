# Tutorial room where they enter a lab and see an orb and remote, i.e. Bloch Sphere

orbSimpleState = "PosZ"

def introRoomStart():
    print("There is an orb cradled in a nest of wires across the lab. As you approach, the orb starts to glow")
    objectTouched = False
    while (!objectTouched):
        action = input("What do you do?")
        if "look" in action:
            print("The orb seems to be waiting for you to touch it.")
        elif "touch" in action:
            introRoomExplainOrb()
        else:
            print("Action not recognized. What would you like to do?")

def introRoomExplainOrb():
    print("When you touch the orb, a bright red laser begins to shine from the center to the top of the orb." +
          "As if the beam was travelling from the core of the Earth's mantle to the North Pole." +
          "The wires crackle and hiss, making you jump, startled. You notice a grey box tangled amist the cords.")
    
    objectLooked = False
    while (!objectLooked):
        action = input("What do you do?")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely.")
            objectLooked = true
        elif "touch" in action:
            print("You begin to reach for the box, but hesitate since you nearly got electrocuted." +
                  "Maybe it would be safer to observe it closely before grabbing.")
        else:
            print("Action not recognized. What would you like to do?")
    
    objectTouched = False
    while (!objectTouched):
        action = input("What do you do?")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely.")
        elif "touch" in action:
            introRoomObtainRemote()
        else:
            print("Action not recognized. What would you like to do?")
    

def describeXTransformation():
    """
    Helper method to describe transformation of X gate on laser while still in introduction to bloch sphere room
    """
    if orbSimpleState is "PosZ":
        print("The orb flickers and its internal laser beam is now pointing directly downwards, towards the South Pole")
        orbSimpleState = "NegZ"
    elif orbSimpleState is "NegZ":
        print("The orb flickers and its internal laser beam is now pointing directly upwards, towards the North Pole")
        orbSimpleState = "PosZ"
    elif orbSimpleState is "PosX" or orbSimpleState is "NegX" or orbSimpleState is "PosY" or orbSimpleState is "NegY":
        print("The orb flickers but the laser does not move")
    else:
        print("ERROR: State not recognized")
    
    
def describeHTransformation():
    """
    Helper method to describe transformation of H gate on laser while still in introduction to bloch sphere room
    """
    
    # TODO: Fill in transformations
    print("The orb flickers and the laser beam makes a 90 degree rotation.")
    if orbSimpleState is "PosZ":
        print("Now, the laser beam is pointing directly to the right along the equator")
        orbSimpleState = "PosX"
    elif orbSimpleState is "NegZ":
        print("Now, the laser beam is pointing directly to the left along the equator")
        orbSimpleState = "NegX"
        
        
        
    elif orbSimpleState is "PosX":
        print("Now, the laser ")
        orbSimpleState = ""
    elif orbSimpleState is "NegX":
        print("Now, the laser .")
        orbSimpleState = ""
    elif orbSimpleState is "PosY":
        print("Now, the laser .")
        orbSimpleState = ""
    elif orbSimpleState is "NegY":
        print("Now, the laser .")
        orbSimpleState = ""
    else:
        print("ERROR: State not recognized")
    
def describeCurrentSimpleState():
    """
    Helper method to remind user where the laser is pointing
    """
    print("You flip the switch and the laser within the orb shines brightly.")
    
    
    # TODO: Fill in transformations
    
    if orbSimpleState is "PosZ":
        print("Now, the laser beam")
    elif orbSimpleState is "NegZ":
        print("Now, the laser beam ")
        
        
        
    elif orbSimpleState is "PosX":
        print("Now, the laser ")
    elif orbSimpleState is "NegX":
        print("Now, the laser ")
    elif orbSimpleState is "PosY":
        print("Now, the laser ")
    elif orbSimpleState is "NegY":
        print("Now, the laser ")
    else:
        print("ERROR: State not recognized")
    

    
def introRoomObtainRemote():
    print("You pick up the remote and see a switch and two rows of buttons. " +
          "The top row has 2 distinct buttons, labelled X and H " +
          "The second row also has 2 distinct buttons, however, the labels are faded and no longer legible.")
        
    XPressed = False
    HPressed = False
    while (!XPressed and !HPressed):
        action = input("What do you do?")
        if "X" in action:
            describeXTransformation()
            XPressed = True     
        elif "H" in action:
            describeHTransformation()
            HPressed = True
        elif "switch" in action:
            describeCurrentSimpleState()
        elif "press" in action:
            introRoomObtainRemote()
        else:
            print("Action not recognized. What would you like to do?")
    
    
# TODO: Next steps is they leave the labratory.
# And they have an "are you sure?" since the orb will lose power to always show laser
# and now the switch will show them the position before converging to a measured state
