# Tutorial room where they enter a lab and see an orb and remote, i.e. Bloch Sphere
import qiskit as qk
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere
from qiskit.providers.jobstatus import JobStatus

from qiskit_ionq_provider import IonQProvider 
from qiskit.providers import aer

import os, sys, itertools
from dotenv import load_dotenv

load_dotenv()

IONQ_API_KEY = os.getenv('IONQ_API_KEY')

# Used to print spinning animation
spinner = itertools.cycle(['-', '/', '|', '\\'])

#Call provider and set token value
provider = IonQProvider(token=IONQ_API_KEY)
simulator = provider.get_backend("ionq_simulator")
qpu = provider.get_backend("ionq_qpu")
orbSimpleState = "PosZ"

def introRoomStart():
    print("There is an orb cradled in a nest of wires across the lab. As you approach, the orb starts to glow")
    objectTouched = False
    while not objectTouched:
        action = input("What do you do?")
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
          "The wires crackle and hiss, making you jump, startled. You notice a grey box tangled amist the cords.")
    
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
    

    
# def describeXTransformation():
#     """
#     Helper method to describe transformation of X gate on laser while still in introduction to bloch sphere room
#     """
#     if orbSimpleState is "PosZ":
#         print("The orb flickers and its internal laser beam is now pointing directly downwards, towards the South Pole")
#         orbSimpleState = "NegZ"
#     elif orbSimpleState is "NegZ":
#         print("The orb flickers and its internal laser beam is now pointing directly upwards, towards the North Pole")
#         orbSimpleState = "PosZ"
#     elif orbSimpleState is "PosX" or orbSimpleState is "NegX" or orbSimpleState is "PosY" or orbSimpleState is "NegY":
#         print("The orb flickers but the laser does not move")
#     else:
#         print("ERROR: State not recognized")
    
    
# def describeHTransformation():
#     """
#     Helper method to describe transformation of H gate on laser while still in introduction to bloch sphere room
#     """
    
#     # TODO: Fill in transformations
#     print("The orb flickers and the laser beam makes a 90 degree rotation.")
#     if orbSimpleState is "PosZ":
#         print("Now, the laser beam is pointing directly to the right along the equator")
#         orbSimpleState = "PosX"
#     elif orbSimpleState is "NegZ":
#         print("Now, the laser beam is pointing directly to the left along the equator")
#         orbSimpleState = "NegX"
        
        
        
#     elif orbSimpleState is "PosX":
#         print("Now, the laser ")
#         orbSimpleState = ""
#     elif orbSimpleState is "NegX":
#         print("Now, the laser .")
#         orbSimpleState = ""
#     elif orbSimpleState is "PosY":
#         print("Now, the laser .")
#         orbSimpleState = ""
#     elif orbSimpleState is "NegY":
#         print("Now, the laser .")
#         orbSimpleState = ""
#     else:
#         print("ERROR: State not recognized")
    
# def describeCurrentSimpleState():
#     """
#     Helper method to remind user where the laser is pointing
#     """
#     print("You flip the switch and the laser within the orb shines brightly.")
    
    
#     # TODO: Fill in transformations
    
#     if orbSimpleState is "PosZ":
#         print("Now, the laser beam")
#     elif orbSimpleState is "NegZ":
#         print("Now, the laser beam ")
        
        
        
#     elif orbSimpleState is "PosX":
#         print("Now, the laser ")
#     elif orbSimpleState is "NegX":
#         print("Now, the laser ")
#     elif orbSimpleState is "PosY":
#         print("Now, the laser ")
#     elif orbSimpleState is "NegY":
#         print("Now, the laser ")
#     else:
#         print("ERROR: State not recognized")
    
def describeInstructions():
    print("This remote control would take you to the Quantum realm. In order to get there" +
          "you should create a superposition state |+> for Qubit1 and |1> for Qubit2." + 
          "Both qubits will start at |0>.")
    
    
def describeQ():
    print("Now you can change the qubit 0 state!")
    Pressed = False
    while not Pressed:
        action = input("What do you do?")
        if ["X","Y","Z","H"] in action:
            return action
        else:
            print("Action not recognized. What would you like to do?")

            
            
    
def introRoomObtainRemote():
    print("You pick up the remote and see three rows of buttons. " +
          "The top row has a button, labelled instructions"+
          "The middle row has 2 distinct buttons, labelled Qubit1 and Qubit2 " +
          "The second row also has 4 distinct buttons, labelled X, Y, Z, and H")
        
    XPressed = False
    HPressed = False
    while not XPressed and not HPressed:
        action = input("What do you do?")
        if "instructions" in action:
            describeInstructions()
        elif "Qubit1" in action:
            Q0 = describeQ()
        elif "Qubit2" in action:
            Q1 = describeQ()
        elif ["X","Y","Z","H"] in action:
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
            print("Two more orbs appear in front of you! Their colour changes rapidly between different shades of red "
                  "and blue. You wait for them to settle down...")
            qc = qk.QuantumCircuit(2,2)
            qc.h([0,1])
            qc.measure([0,1],[0,1])
            job = qpu.run(qc, shots=1)
            while job.status() is not JobStatus.DONE:
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                sys.stdout.write('\b')
            counts = job.result().get_counts()
            q0, q1 = list(list(counts.keys())[0])
            print(f"The first orb settles to {'red' if q0 == '0' else 'blue'}, "
                  f"and the second orb settles to {'red' if q1 == '0' else 'blue'}.")
            if q0 == '0' and q1 == '0':
                room1()
            elif q0 == '0' and q1 == '1':
                room2()
            elif q1 == '0':
                room3()
            else:
                room4()

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
