# Circuit simulator

The point of these repository is to create circuit simulator, as the Falstad.com or similar. It should has GUI and it should be able to show circuit, graphical waveform and exports data.

First version SimulatorV1.py is a console app and it is just a simple calculator. It operates only with series circuit. You can put voltage values for one or more DC sources and resistance for optional number of resistors. SimulatorV1.py will calculate voltages on each resistor or voltage just on one of them.

To craete full-fledged  simulator for serial-parallel circuit is more complicated.

First step is to describe the circuit and its connection (and explain it to computer in Python). The way how to do it is based on graph theory, especially on adjacency list.

This is contained a file Adjacency_list.py. 

This console app takes a number of Elements with its properties and put it into one list. There are required properties, id_A and id_B. Those id_X are junctions in circuit. Than there is function for creating the adjacency list, which is describing what Elements have same junctoins (or what Elements meet in one junction).

For better understandig, there is an example:

![alt text](https://github.com/KattyKing/Circuit-simulator/blob/master/SchemaGraph.png)

Picture A and B are simple circuits. 

Picture C is a the same circuit modified for Python. Components in a scheme are described as "E" (=elements) and junctions have indexes. In Python, we will create a list of lists. It should looks like this one:

('ID-A', 'ID-B', 'Component-Type', 'Value')


Elements = [

(1, 3, 'R', 0.5),  # 0:R₀

(0, 2, 'R', 2.5),  # 1:R₁

(2, 3, 'R', 6.0),  # 2:R₂

(3, 5, 'R', 1.5),  # 3:R₃

(4, 5, 'R', 0.5),  # 4:R₄

(0, 1, 'U', 18.0), # 5:U₀

(2, 4, 'U', 45.0)  # 6:U₁

]

On the picture D there is a graph of the circuit.  It has junctions, but there are only lines instead of elements. This is a basis for creating an adjacency list. It is final adjacency list for our example: first line shows what junctions are connected to junction 0, etc. 

AdjacencyList = [

[1,5],   # junction-0: R₁, U₀

[0,5],   # junction-1: R₀, U₀

[1,2,6], # junction-2 ...

[0,2,3], # junction-3 ...

[4,6],   # junction-4 ...

[3,4],   # junction-5 ...

]

Other parts will follow later.


Link to theory of adjacencz list:

http://www.algolist.net/Data_structures/Graph/Internal_representation

