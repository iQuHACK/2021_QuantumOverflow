# Tutorial room where they enter a lab and see an orb and remote, i.e. Bloch Sphere
import qiskit as qk
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

from qiskit_ionq_provider import IonQProvider 
from qiskit.providers import aer

#Call provider and set token value
provider = IonQProvider(token='My token')
backend = aer.QasmSimulator()
orbSimpleState = "Zero"

def introRoomStart():
    print("You awaken in a dimly lit, abandoned laboratory. The door is locked and there are no windows." +
          "The lab is littered with with broken electronics, but across the lab, there is a mysterious orb cradled in a nest of wires." +
          "As you approach, the orb starts to glow.")
    objectTouched = False
    while not objectTouched:
        action = input("What do you do? ")
        if "look" in action:
            print("The orb seems to be waiting for you to touch it.")
            qc = qk.QuantumCircuit(2,2)
            qc.h(0)
            qc.cx(0,1)
            # fig = qc.draw('mpl')
            # fig.show()
            state = Statevector.from_instruction(qc)
            fig2 = plot_state_qsphere(state)
            fig2.show()
        elif "touch" in action:
            introRoomExplainOrb()
        elif "quit" in action:
            break
        else:
            print("Action not recognized. What would you like to do?")

def introRoomExplainOrb():
    print("When you touch the orb, a bright red laser begins to shine from the center to the top of the orb." +
          "As if the beam was travelling from the core of the Earth's mantle to the North Pole." +
          "The wires crackle and hiss, making you jump, startled. You notice a grey box tangled amidst the cords.")
    
    objectLooked = False
    while not objectLooked:
        action = input("What do you do?")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely.")
            objectLooked = True
        elif "touch" in action:
            print("You begin to reach for the box, but hesitate since you nearly got electrocuted." +
                  "Maybe it would be safer to observe it closely before grabbing.")
        elif "quit" in action:
            break
        else:
            print("Action not recognized. What would you like to do?")
    
    objectTouched = False
    while not objectTouched:
        action = input("What do you do?")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely.")
        elif "touch" in action:
            introRoomObtainRemote()
        elif "quit" in action:
            break
        else:
            print("Action not recognized. What would you like to do?")
    

    
def describeXTransformation():
#     """
#     Helper method to describe transformation of X gate on laser while still in introduction to bloch sphere room
#     """
    print("The orb makes a whirring sound, and the inside of the orb rotates 180 degrees clockwise, like a rolling ball. ") 
    if orbSimpleState is "Zero":
        setState("One")
    elif orbSimpleState is "One":
        setState("Zero")
    else:
        sameState()
        
def describeZTransformation():
#     """
#     Helper method to describe transformation of X gate on laser while still in introduction to bloch sphere room
#     """
    print("The orb makes a whirring sound, and the inside of the orb rotates 180 degrees facing up, like a spinning basketball. ") 
    if orbSimpleState is "Plus":
        setState("Minus")
    elif orbSimpleState is "Minus":
        setState("Plus")
    else:
        sameState()
        
def describeHTransformation():
#     """
#     Helper method to describe transformation of X gate on laser while still in introduction to bloch sphere room
#     """
    print("The orb makes a whirring sound, and the inside does a clever diagonal rotation. ") 
    if orbSimpleState is "Zero":
        setState("Plus")
    elif orbSimpleState is "Plus":
        setState("Zero")
    elif orbSimpleState is "One":
        setState("Minus")
    elif orbSimpleState is "Minus":
        setState("One")
    else:
        sameState()

def sameState():
    if orbSimpleState is "Zero":
        print("The internal laser beam turns on its axis, and it is still in the \"Zero\" state.")
    elif orbSimpleState is "One":
        print("The internal laser beam turns on its axis, and it is still in the \"One\" state.")
    elif orbSimpleState is "Plus":
        print("The internal laser beam turns on its axis, and it is still in the \"Plus\" state.")
    elif orbSimpleState is "Minus":
        print("The internal laser beam turns on its axis, and it is still in the \"Minus\" state.")
    elif orbSimpleState is "Unknown":
        print("The light in the orb is still blurred, and you cannot clearly tell the state.")
    else:
        print("ERROR: State not recognized")
    
def setState(newState):
    if newState is "One":
        print("The internal laser beam is now pointing directly downwards, to the \"One\" state.")
    elif newState is "Zero":
        print("The internal laser beam is now pointing directly upwards, to the \"Zero\" state.")
    elif newState is "Plus":
        print("The internal laser beam is now pointing towards you, to the \"Plus\" state.")
    elif newState is "Minus":
        print("The internal laser beam is now pointing away from you, to the \"Minus\" state.")
    elif newState is "Unknown":
        print("The laser light is blurred, and the state is unknown.")
    else:
        print("ERROR: State not recognized")
    orbSimpleState = newState
    

# def describeCurrentSimpleState():
#     """
#     Helper method to remind user where the laser is pointing
#     """
#     print("You flip the switch and the laser within the orb shines brightly.")
    
    

# def describeInstructions():
#    print("This remote control would take you to the Quantum realm. In order to get there" +
#          "you should create a superposition state |+> for Qubit1 and |1> for Qubit2." + 
#          "Both qubits will start at |0>.")
def describeInstructions():
    print("The instructions say \"Up: 0, Down: 1, Forward: -, Back: +. Blur: Unknown\"")
    
def useRemote(action):
    if "X" in action:
        describeXTransformation()
    elif "Z" in action:
        describeZTransformation()
    elif "H" in action:
        describeHTransformation()
    elif "CNOT" in action:
        describeHTransformation()
    elif "M" in action:
        describeHTransformation()
    else:
        print("Action not recognized. What would you like to do?")

            
            
    
def introRoomObtainRemote():
    print("You pick up the remote. Dusting off the top, you read \"A Qubit\". " +
          "The remote has two rows of buttons. " +
          "The top row has 3 buttons, labelled X, Z, and H. " +
          "The bottom row has 2 buttons, labelled CNOT and M. " +
          "Near the CNOT button, a small wire with a connector on the end hangs loosely." +
          "There are instructions on the back of the remote.")
        
    XPressed = False
    HPressed = False
    while not XPressed and not HPressed:
        action = input("What do you do?")
        if "instructions" in action:
            describeInstructions()
        if ["X","Z","H","M","CNOT"] in action:
            useRemote(action)
            print("Looks like you should select first the Q0 or Q1 buttons.")
        if Q0 == "H" and Q1 == "X":
            goingToQuantumRealm()
        # if "X" in action:
        #     describeXTransformation()
        #     XPressed = True     
        # elif "H" in action:
        #     describeHTransformation()
        #     HPressed = True
        # elif "switch" in action:
        #     describeCurrentSimpleState()
        # elif "press" in action:
        #     introRoomObtainRemote()
        # else:
        #     print("Action not recognized. What would you like to do?")
    
def goingToQuantumRealm():
    print("An Inter-dimensional portal just open!")
    portalOpen = True
    while portalOpen:
        action = input("What do you do?")
        if "enter" in action:
            qc = qk.QuantumCircuit(2,2)
            qc.h([0,1])
            qc.measure([0,1],[0,1])
            result = qk.execute(qc, backend, shots=1).result().get_counts()
            for i in result.keys():
                if i == '00':
                    room1()
                elif i == '01':
                    room2()
                elif i == '10':
                    room3()
                elif i == '11':
                    room4()
                else:
                    print("Error")
                    
def room1():
    print("Room 1")
def room2():
    print("Room 2")
def room3():
    print("Room 3")
def room4():
    print("Room 4")
            
            
            
            
            
        
# TODO: Next steps is they leave the labratory.
# And they have an "are you sure?" since the orb will lose power to always show laser
# and now the switch will show them the position before converging to a measured state
