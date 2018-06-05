RESISTANCE = []
RESISTORS = []
UR = []
SOURCES = []

while True:
	try:
		RESISTORS_COUNT = int(input('Number of resistors in circuit: ',))
		break
	except ValueError:
		print('It was not a number')
		#RESISTORS_COUNT = int(input('Number of resistors in circuit: ',))

while True:
	try:
		SOURCES_COUNT = int(input('Number of voltage sources in circuit: ',))
		break
	except ValueError:
		print('It was not a number')
		

class Resistor:
	def __init__(self, resistance):
		self.resistance = resistance
		
	def voltage_on_resistor(self, I):
		self.voltage_on_res = self.resistance * I
		return self.voltage_on_res
		

class Source:
	def __init__(self, voltage):
		self.voltage = voltage
		

def totalresistance():
	for res in range(RESISTORS_COUNT):
		while True:
			try:
				res = Resistor(int(input('Resistance value: ')))
				break
			except ValueError:
				print('It was not a number.')
		RESISTANCE.append(res.resistance)
		RESISTORS.append(res)
		total_resistance = sum(RESISTANCE)
	return total_resistance
	
def totalvoltage():
	for sour in range(SOURCES_COUNT):
		while True:
			try:
				sour = Source(int(input('Voltage value: ')))
				break
			except ValueError:
				print('It was not a number.')
		SOURCES.append(sour.voltage)
		total_voltage = sum(SOURCES)		
	return total_voltage

def current(U, R):
	I = U / R
	return I
	
def voltage_on_all_res(I):
	for R in range(RESISTORS_COUNT):
		UR.append(RESISTORS[R].voltage_on_resistor(I))
	for i, ur in enumerate(UR):
		print('Voltage on resistor {} is {}'.format(i, ur))	

	
def voltage_on_one_res(I):
	while True:
		try:
			position = int(input('Index of resistor:', ))
			if position >= RESISTORS_COUNT:
				print('This index does not exist.')
			else:
				print('Voltage on resistor {} is {}'.format(position, RESISTORS[position].voltage_on_resistor(I)))
				break
		except ValueError:
			print('It was not a number.')
	
def calculate():
	U = totalvoltage()
	R = totalresistance()
	I = current(U, R)
	
	while True:
		key_pressed = input(
		'''
What do you need?
'a' ... calculate voltage on all resistors
'b' ... calculate voltage on one resistor
'c' ... cancel.
''', )
				
		if key_pressed == 'a':
			voltage_on_all_res(I)
			print('')
			print('')
		elif key_pressed == 'b':
			voltage_on_one_res(I)
			print('')
			print('')
		elif key_pressed == 'c':
			print('')
			print('')
			break
		else:
			print('This was not a correct key. Please, try it again and better.')
			
calculate()
	
