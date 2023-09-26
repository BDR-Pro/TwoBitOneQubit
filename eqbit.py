from qiskit import qasm3 
from qiskit import *
import qiskit as q

def eq01():
    qc=QuantumCircuit(2,2) 
    qc.h(0)
    qc.cx(0,1)
    qc.barrier()
    qc.z(0)
    qc.barrier()
    qc.cx(0,1)
    qc.h(0)
    qc.measure(1, 1)
    qc.measure(0, 0)
    qc.draw(output='mpl')
    job = q.execute(qc, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
    print(job.result().get_counts(qc))

def eq00():
    qc=QuantumCircuit(2,2) 
    qc.h(0)
    qc.cx(0,1)
    qc.barrier()
    qc.barrier()
    qc.cx(0,1)
    qc.h(0)
    qc.measure(1, 1)
    qc.measure(0, 0)
    qc.draw(output='mpl')
    job = q.execute(qc, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
    print(job.result().get_counts(qc))


def eq10():
    qc=QuantumCircuit(2,2) 
    qc.h(0)
    qc.cx(0,1)
    qc.barrier()
    qc.x(0)
    qc.barrier()
    qc.cx(0,1)
    qc.h(0)
    qc.measure(1, 1)
    qc.measure(0, 0)
    qc.draw(output='mpl')
    job = q.execute(qc, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
    print(job.result().get_counts(qc))

def eq11():
    qc=QuantumCircuit(2,2) 
    qc.h(0)
    qc.cx(0,1)
    qc.barrier()
    qc.x(0)
    qc.z(0)
    qc.barrier()
    qc.cx(0,1)
    qc.h(0)
    qc.measure(1, 1)
    qc.measure(0, 0)
    qc.draw(output='mpl')
    job = q.execute(qc, backend=q.Aer.get_backend('qasm_simulator'), shots=1024)
    print(job.result().get_counts(qc))

userbits = input("what is the bits")

if userbits=='01':
    eq01()
if userbits=='00':
    eq00()
if userbits=='10':
    eq10()
if userbits=='11':
    eq11()
else:
    print("valid two bits please")