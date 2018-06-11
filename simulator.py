RESISTORS = []

class Resistor:
	'''Class for creating resistor objects and calculating its voltage.'''
	def __init__(self, resistance):
		'''Method sets initial parameter resistance.'''
		self.resistance = resistance
		
	def voltage_on_resistor(self, I):
		'''Method takes total current and calculate voltage on resistor.'''
		self.voltage_on_res = self.resistance * I
		return self.voltage_on_res
		

class Source:
	'''Class for creating source objects. '''
	def __init__(self, voltage):
		'''Method sets initial parameter.'''
		self.voltage = voltage
		

def totalresistance(RESISTORS_COUNT):
	'''Function for calculating total resistance in circuit. It create all resistors object and sum the resistance.'''
	resistance = []
	for res in range(RESISTORS_COUNT):
		while True:
			try:
				res = Resistor(int(input('Resistance value: ')))
				break
			except ValueError:
				print('It was not a number. Please, try it again and better.')
		resistance.append(res.resistance)
		RESISTORS.append(res)
		total_resistance = sum(resistance)
	return total_resistance
	
def totalvoltage(SOURCES_COUNT):
	'''Function creates source objects and sum its voltages.'''
	sources = []
	for sour in range(SOURCES_COUNT):
		while True:
			try:
				sour = Source(int(input('Voltage value: ')))
				break
			except ValueError:
				print('It was not a number. Please, try it again and better.')
		sources.append(sour.voltage)
		total_voltage = sum(sources)		
	return total_voltage

def current(U, R):
	'''Function takes total voltage and total resistance and calculates total current. '''
	I = U / R
	return I
	
def voltage_on_all_res(I, RESISTORS_COUNT):
	'''Function takes list Resistors and calls method voltage_on_resistor for each of them. '''
	UR = []
	for R in range(RESISTORS_COUNT):
		UR.append(RESISTORS[R].voltage_on_resistor(I))
	for i, ur in enumerate(UR):
		print('Voltage on resistor {} is {} V'.format(i, ur))	

	
def voltage_on_one_res(I, RESISTORS_COUNT):
	'''Function takes position of one object in list Resistors and calls for this object method voltage_on_resistor.'''
	while True:
		try:
			position = int(input('Index of resistor: ', ))
			if position >= RESISTORS_COUNT:
				print('This index does not exist. Please, try it again and better.')
			else:
				print('Voltage on resistor {} is {} V'.format(position, RESISTORS[position].voltage_on_resistor(I)))
				break
		except ValueError:
			print('It was not a number. Please, try it again and better.')
			
def counts():
	'''Function sets number of resistors and sources in circuit.'''
	count = []
	while True:
		try:
			RESISTORS_COUNT = int(input('Number of resistors in circuit: ',))
			count.append(RESISTORS_COUNT)
			break
		except ValueError:
			print('It was not a number. Please, try it again and better.')
			
	while True:
		try:
			SOURCES_COUNT = int(input('Number of voltage sources in circuit: ',))
			count.append(SOURCES_COUNT)
			break
		except ValueError:
			print('It was not a number. Please, try it again and better.')
	
	return count
	
				
def simulator():
	'''Function simulator. Calling of previous funkcion. '''
	while True:
		count = counts()
		U = totalvoltage(count[1])
		R = totalresistance(count[0])
		I = current(U, R)
		
		key_pressed = input(
		'''
What do you need?
'a' ... calculate voltage on all resistors
'b' ... calculate voltage on one resistor
'c' ... restart
'd' ... cancel.
Your choice: ''', )

		if key_pressed == 'a':
			voltage_on_all_res(I, count[0])
			RESISTORS = []
			anything_else = input('''
			
Do you want put another values? 
If yes, type 'a'. 
If don't, type anything else and cancel this app.
Your choice: ''')
			if anything_else != 'a':
				print('Thanks for using simulator.')
				break
			
		elif key_pressed == 'b':
			voltage_on_one_res(I, count[0])
			while True:
				another = input('''
Another voltage value? 
If yes, type 'a'.
If don't, type anything else and cancel this app.
Your choice: ''')

				if another == 'a':
					voltage_on_one_res(I, count[0])
				else:
					print('Thanks for using simulator.')
					break
			break
			
		elif key_pressed == 'c':
			print('Type new values: ')
			
		elif key_pressed == 'd':
			print('Thanks for using simulator.')
			break
			
		else:
			print('This was not a correct key. Please, try it again and better.')
			
simulator()
	
