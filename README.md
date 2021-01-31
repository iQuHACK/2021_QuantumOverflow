Having a README in your team's repository facilitates judging. A good README contains:
* a clear title for your project,
* a short abstract,
* the motivation/goals for your project,
* a description of the work you did, and
* proposals for future work.


# Colossal Quantum Adventure: An educational quantum text-based game

Miasya Bulger, Corbin McElhanney, Matthew Mikhailov, Alejandro Montanez, Ben Sachs.

## Introduction

As Professor Chuang mentioned in his keynote, quantum computing today has to straddle a divide, between abstraction in computer science, and complexity in physics. Interference and entanglement are central to quantum computing, but because they are difficult to visualize, quantum computing often has a steep and heavily mathematical learning curve.

Inspired by 1977's Colossal Cave Adventure, one of the first adventure video games invented, we have created a text-based video game called Colossal Quantum Adventure. Colossal Cave Adventure players claimed they could easily navigate the real Kentucky cave system it was based on. With Colossal Quantum Adventure, we hope to build a strong intuition for quantum phenomena, that will help players explore the real, quantum world with ease. 
In Colossal Quantum Adventure, you can learn concepts such as superposition, entanglement, and a few basic quantum protocols in a creative and fun way.

## Basic principles

The player has a "Qubit", which looks like a large electromechanical Bloch sphere. Moving forward in the game involves discovering what the qubit can do, and using it to solve challenges and overcome obstacles. This involves understanding the operation of gates, creating and measuring a Bell State, and teleporting a qubit.

## Elements and rules

The Qubit has a remote, which can be used to apply X, Z, and H gates on the qubit or perform a measurement on the qubit. The remote can also be used to apply a controlled not gate between the player's qubit and any other qubit they encounter. The game visualizes states in the sign and standard bases as a laser pointer in the orb, pointing to a location on the Bloch sphere. Gates are described as mechanical rotations of the inside of the sphere, and this explains why some states are unchanged by certain gates. For example, applying an X gate to the |+> state is visualized as a rotation around the axis of the laser, so the |+> state does not change. Superpositions are described as blurred light in the orb, and entanglement is indicated by a handy green LED on the side panel.

## Demonstrations:

The GitHub repository link is [https://github.com/iQuHACK/2021_QuantumOverflow](https://github.com/iQuHACK/2021_QuantumOverflow).


## ToDo:
### Things we would wanna fix/implement but didn't have enough time to do

* Make it more "colossal", add more locations and puzzles
* Have a lot of people play it, to work out challenges to comprehension
* Process more player options, such as "pick up" instead of "touch"


## Highlights:

* The game requires no prior knowledge of quantum phenomena or quantum computing math, but leaves the player with an intuition for both.
* We think our visualizations are very intuitive.
* Because the game is text-based, the queue waiting time on the quantum computer does not significantly affect gameplay. 
* When the player uses superposition, the BB84 QKD algorithm, or quantum teleportation, their circuits actually run on a quantum computer or simulator.