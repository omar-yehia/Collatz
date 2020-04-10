

# odd numbers to bigger value (Odds To Big) OTB
# EOR is end of row (print hypotenuse)

def OTB_print_triangle(anyNumber=1,numberOfLevels=6):
	print("\nanyNumber={0}".format(anyNumber))
	for level in range(numberOfLevels):
		row=level
		col=0
		for i in range(level):
			print( -1+ ( 2 * 2**row * 3**col * anyNumber ) ,end="->")
			col+=1
			row-=1
		EOR = -1+ ( 2 * 2**row * 3**col * anyNumber )
		print(EOR)



def OTB_print_rectangle(anyNumber=1,numberOfLevels=6):
	print("\nanyNumber={0}".format(anyNumber))
	for row in range(numberOfLevels):
		for col in range(numberOfLevels):
			print( -1+ ( 2 * 2**row * 3**col * anyNumber ) ,end=",")
		print("")


OTB_print_rectangle(5,6)
OTB_print_triangle(5,6)
