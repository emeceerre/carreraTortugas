import turtle

class Carrera:
	corredores = []
	# en lugar de crear la tupla de posiciones iniciales, se puede crear una función que 
	# calcule las posiciones en función de la altura del circuito o del nº de corredores.
	__posStartY = (-30, -10, 10, 30)
	__colorTurtle = ('red', 'blue', 'green', 'orange')
	
	def __init__(self, width, height):
		# width y height serán las dimensiones de nuestro circuito/pantalla
		self.__screen = turtle.Screen()
		self.__screen.setup(self.width, self.height)
		self.__screen.bgcolor('lightgray')
		# calculamos la línea de salida poniéndola 20uds más avanzada del comienzo del circuito.
		self.__startline = (width/2 - 20) * -1 
		self.__finishline = width/2 - 20

		self.__createRunners()

	def __createRunners(self):
		for i in range(4):
			new_turtle = turtle.Turtle()
			new_turtle.shape('turtle')
			new_turtle.color(self.__colorTurtle[i])
			new_turtle.penup()
			new_turtle.setpos(self.__startline, __posStartY[i])
			self.corredores.append(new_turtle)

	def competir(self):
		pass


if __name__=='__main__':
	circuito = Circuito(640, 480)