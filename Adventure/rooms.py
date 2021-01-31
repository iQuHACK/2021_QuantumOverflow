# Tutorial room where they enter a lab and see an orb and remote, i.e. Bloch Sphere
import qiskit as qk
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

from qiskit_ionq_provider import IonQProvider 
from qiskit.providers import aer
import numpy as np

#Call provider and set token value
provider = IonQProvider(token='My token')
backend = aer.QasmSimulator()
orbSimpleState = "Zero"
orbEntangled = False
orbWireConnected = False
orb2State = "Zero"

def introRoomStart():
    #
    # Start of the game
    #
    print("You awaken in a dimly lit, abandoned laboratory. The door is locked and the windows are small and dark. " +
          "The lab is littered with with broken electronics, but across the lab, there is a mysterious orb cradled in a nest of wires. " +
          "As you approach, the orb starts to glow. ")
    
    objectTouched = False
    while not objectTouched:
        action = input("What do you do? ")
        if "look" in action:
            print("The orb seems to be waiting for you to touch it. ")
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
            print("Action not recognized. ")

def introRoomExplainOrb():
    #
    # Explaining what the orb is like after you touch it 
    #
    print("When you touch the orb, a bright red laser begins to shine from the center to the top of the orb. " +
          "As if the beam was travelling from the core of the Earth's mantle to the North Pole. " +
          "The wires crackle and hiss, making you jump, startled. You notice a grey box tangled amidst the cords. ")
    
    objectLooked = False
    while not objectLooked:
        action = input("What do you do? ")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely. ")
            objectLooked = True
        elif "touch" in action:
            print("You begin to reach for the box, but hesitate since you nearly got electrocuted. " +
                  "Maybe it would be safer to observe it closely before grabbing. ")
        elif "quit" in action:
            break
        else:
            print("Action not recognized. ")
    
    objectTouched = False
    while not objectTouched:
        action = input("What do you do? ")
        if "look" in action:
            print("The box seems to be some form of remote control. " +
                  "You notice that there's a convenient gap in the wires where you can reach it safely. ")
        elif "touch" in action:
            introRoomObtainRemote()
        elif "quit" in action:
            break
        else:
            print("Action not recognized. ")



def introRoomObtainRemote():
    #
    # Description of the remote and what it can do
    #
    print("You pick up the remote. Dusting off the top, you read \"A Qubit\". " +
          "The remote has two rows of buttons. " +
          "The top row has 3 buttons, labelled X, Z, and H. " +
          "The bottom row has 2 buttons, labelled CNOT and M. " +
          "Near the CNOT button, a small wire with a connector on the end hangs loosely, " +
          "and there is a switch labeled \"control\" with the options \"this\" and \"other\". " +
          "There are instructions on the back of the remote. ")    
    
    while orbSimpleState is not "Minus":
        action = input("What do you do?")
        if "instructions" in action:
            describeInstructions()
        if ["X","Z","H","M","CNOT"] in action:
            useRemote(action)
            
        #if Q0 == "H" and Q1 == "X":
        #    goingToQuantumRealm()
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
        
def describeInstructions():
    print("The instructions say \"Up: |0>, Down: |1>, Forward: |->, Back: |+>. Blur: Unknown\". " +
          "Beneath, the following diagram is drawn: \n \n" +
          "|0> ------ X ------ |1> \n" +
          " |                   | \n" +
          " H                   H \n" +
          " |                   | \n" +
          "|+> ------ Z ------ |-> \n \n")
    
    print("A taped-on scrap of paper says \"This remote control would take you to the Quantum Realm. " +
          "In order to get there you should create a superposition state |-> for your qubit. " + 
          "The qubit will start at |0>.\"")
    
    
    
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
                    
    
def useRemote(action):
    #
    # Helper method to process gate and measurement commands
    #
    if "X" in action:
        describeXTransformation()
    elif "Z" in action:
        describeZTransformation()
    elif "H" in action:
        describeHTransformation()
    elif "CNOT" in action:
        describeCNOTTransformation()
    elif "M" in action:
        describeMeasurement()
    else:
        print("Action not recognized. What would you like to do?")


# def describeCurrentSimpleState():
#     """
#     Helper method to remind user where the laser is pointing
#     """
#     print("You flip the switch and the laser within the orb shines brightly.")

                    
def describeXTransformation():
#     """
#     Helper method to describe transformation of X gate on laser
#     """
    print("The orb makes a whirring sound, and the inside of the orb rotates 180 degrees clockwise, like a rolling ball. ") 
    if orbSimpleState is "Zero":
        setState("One")
    elif orbSimpleState is "One":
        setState("Zero")
    else:
        rotateSameState()
        
def describeZTransformation():
#     """
#     Helper method to describe transformation of Z gate on laser
#     """
    print("The orb makes a whirring sound, and the inside of the orb rotates 180 degrees facing up, like a spinning basketball. ") 
    if orbSimpleState is "Plus":
        setState("Minus")
    elif orbSimpleState is "Minus":
        setState("Plus")
    else:
        rotateSameState()
        
def describeHTransformation():
#     """
#     Helper method to describe transformation of X gate on laser
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
        rotateSameState()
        
def describeCNOTTransformation(controlBit):
#     """
#     Helper method to describe transformation of CNOT gate on your qubit and a different one
#     """
    if orbConnected != True:
            print("The button flashes red. You have to connect to another qubit to use CNOT.")
    else:
        order = ""
        while not ["this","other"] in order:
            order = input("Which qubit do you use as the control bit?")
            if "this" in order:
                print("The light in your orb flickers, but the inside of your orb does not move. ")
                stillSameState()
                if orb2State is not "Unknown":
                    print("However, the other orb, connected by wire, has become blurred. ")
                else:
                    print("The other orb is still blurred. ")
                orb2State = "Unknown"
                print("A small green light labeled \"entangled\" lights up on your orb. ")
                orbEntangled = True
            elif "other" in order:
                print("The light in your orb flickers. ")
                setState("Unknown")
                if orb2State is not "Unknown":
                    print("The other orb does not move, and it is still in the \"" + orb2State + "\" state. ")
                else:
                    print("The other orb does not move, and it is still blurred. ")
                print("A small green light labeled \"entangled\" lights up on your orb. ")
                orbEntangled = True
            else:
                print("The switch only has \"this\" and \"other\"")
            
    
    
def describeMeasurement():
#     """
#     TODO: Please help me write this
#     """
# We need to actually measure our qubit using qiskit, and then use some print statements and the setState(newState)
# command to describe the result to the player
        

def stillSameState():
    if orbSimpleState in ["Zero","One","Plus","Minus"]:
        print("The orb is still in the \"" + orbSimpleState + "\" state. ")
    elif orbSimpleState is "Unknown":
        print("The light in the orb is still blurred, and you still cannot tell the state. ")
    else:
        print("ERROR: State not recognized")
        
def rotateSameState():
    if orbSimpleState in ["Zero","One","Plus","Minus"]:
        print("The internal laser beam turns on its axis, and it is still in the \"" + orbSimpleState + "\" state. ")
    elif orbSimpleState is "Unknown":
        print("The light in the orb is still blurred, and you still cannot tell the state. ")
    else:
        print("ERROR: State not recognized")
    
def setState(newState):
    if newState is "One":
        print("The internal laser beam is now pointing directly downwards, to the \"One\" state. ")
    elif newState is "Zero":
        print("The internal laser beam is now pointing directly upwards, to the \"Zero\" state. ")
    elif newState is "Plus":
        print("The internal laser beam is now pointing towards you, to the \"Plus\" state. ")
    elif newState is "Minus":
        print("The internal laser beam is now pointing away from you, to the \"Minus\" state. ")
    elif newState is "Unknown":
        print("The laser light is now blurred, and you cannot tell the state.")
    else:
        print("ERROR: State not recognized")
    orbSimpleState = newState
    
    
def QuantumCryptography():
    print("Alice was here and leaved you a message on a BB84 protocol" +
          "a key = [0111001] and a Quantum circuit for you to measure"+
           "For  basis[i]=0  (i.e., if the  ith  bit is zero), she encodes"+
           " the ith  qubit in the standard  {|0>,|1>} basis, while for  basis[i]=1,"+
           "she encodes it in the  {|+⟩,|−⟩}. Now, you can create a basis for you"
           )
    # message encoded
    qc = qk.QuantumCircuit(7,7)
    qc.h(0)
    qc.h(1)
    qc.z(1)
    qc.x(2)
    qc.h(3)
    qc.z(3)
    qc.x(6)
    return qc
    
def room1(qc = None):
    basis_Alice = [1101000]
    print("The portal conducted you to the Quantum Cryptography room"+
          "Someone was here some time ago and leave a box with a message" + 
          "There is a button called measure and 4 spaces for a key.")
    while True:
        action = input("What do you do?")
        if "look" in action:
            qc = QuantumCryptography()
        elif 'measure' in action:
            if qc != None:
                basis = [np.random.randint(0,2) for i in range(7)]
                for n, i in enumerate(basis):
                    if i == 1:
                        qc.h(n) # To measure in |-⟩,|+⟩
                qc.measure(range(7),range(7))
                job = qk.execute(qc,backend, shots=1000)
                results = job.result().get_counts()
                print("The measurement gives you the following outcome: ")
                print(results)
            else:
                print("you should look the message first!")
        elif "key" in action:
            while True:
                key = input("Please introduce the key.")
                if key == "0110":
                    print("Awesome, you got the correct key. You complete this"+
                          "Room")
                    goingToQuantumRealm()
                else:
                    print("Sorry, wrong key. Try again")
                    room1(qc)
        elif "quit" in action:
            break
        else:
            print("Action not recognized. What would you like to do?")
def room2():
    print("Room 2")
def room3():
    print("Room 3")
def room4():
    print("Room 4")
            
            
            
            
            
        
# TODO: Next steps is they leave the labratory.
# And they have an "are you sure?" since the orb will lose power to always show laser
# and now the switch will show them the position before converging to a measured state
