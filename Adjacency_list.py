COUNT_OF_ELEMENTS = int(input('Number of elements in circuit: ',))


class Elements:
	def __init__(self, id_A, id_B, element_type, value):
		self.id_A = id_A
		self.id_B = id_B
		self.element_type = element_type
		self.value = value
		

def create_element():
	elements = []
	print('Please, use 0 as a lowest index.')
	for element in range(COUNT_OF_ELEMENTS):
		id_A = int(input('id_A: ', ))
		id_B = int(input('id_B: ', ))
		element_type = input('element_type: ', )
		value = float(input('value: ', ))
		element = Elements(id_A, id_B, element_type, value)
		elements.append(element)
	return elements


ELEMENTS = create_element()


def junctions():
	id_X = []
	for i in range(COUNT_OF_ELEMENTS):
		id_X.append(ELEMENTS[i].id_A)
		id_X.append(ELEMENTS[i].id_B)
		
	maximum = max(id_X) +1
	
	return maximum
	
JUNCTIONS = junctions()

	
def empty_list():
	Adja_list = []
	for i in range(JUNCTIONS):
		i = []
		Adja_list.append(i)
	return Adja_list
	
Adjacency_list = empty_list()


def Adjacency():
	for junction in range(JUNCTIONS):
		for element in range(COUNT_OF_ELEMENTS):
			if ELEMENTS[element].id_A == junction or ELEMENTS[element].id_B == junction:
				Adjacency_list[junction].append(ELEMENTS.index(ELEMENTS[element]))
				
	return Adjacency_list
	
	
print(Adjacency())	

