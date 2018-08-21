# Circuit simulator

The point of these repository is to create circuit simulator, as the Falstad.com or similar. It should has GUI and it should be able to show circuit, graphical waveform and exports data.

First version SimulatorV1.py is a console app and it is just a simple calculator. It operates only with series circuit. You can put voltage values for one or more DC sources and resistance for optional number of resistors. SimulatorV1.py will calculate voltages on each resistor or voltage just on one of them.

To craete full-fledged  simulator for seriál-parallel circuit is more complicated.

First step is to describe the circuit and its connection (and explain it to computer in Python). The way how to do it is based on graph theory and the adjacency list.

This is included in the file Adjacency_list.py. 

It takes a number of Elements and put it into one list. There are required properties, id_A and id_B. Those id_s are junctions in circuit. Than there is function for creating the adjacency list, which is describing what Elements have same junctoins (or what Elements meet in one junction). 

Links to theory:

https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
http://www.algolist.net/Data_structures/Graph/Internal_representation

