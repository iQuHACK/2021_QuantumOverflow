def getRandom():
    
    from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ, Aer

    def binaryToDecimal(binary): 

        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal


    #ibmq.enable_account(api token)
    #provider = IBMQ.get_provider()
    backend_sim = Aer.get_backend('qasm_simulator')

    q = QuantumRegister(11, 'q')
    c = ClassicalRegister(11, 'c')
    circuit = QuantumCircuit(q, c)
    circuit.h(q)
    circuit.measure(q,c)
    circuit.draw(output='mpl')

    backend_sim = Aer.get_backend('qasm_simulator')
    sim = execute(circuit, backend_sim, shots = 1)
    counts = sim.result().get_counts()
    count_list = list(counts.keys())
    value = count_list[0]
    toDecimal = binaryToDecimal(int(value))
    random = toDecimal / 2048.0
    print(random)
    return(random)

getRandom()
