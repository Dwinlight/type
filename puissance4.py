import numpy as np
currentPlayer = 0
longest = 0
RED = 1 
YELLOW = 0
colors = ["yellow is playing", "red is playing"]
court = np.array([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]])
                 
while longest < 4:
	print(colors[currentPlayer])
	c = input("Enter your column number")
	i = 0
	while i <len(court[:][0]) and court[i][c] != 0:
		i+=1
	if i < court[:].shape:
		court[i][c] = currentPlayer
		c = 0
		if currentPlayer == 0:
			currentPlayer = 1 
		else:
			currentPlayer = 0
	else:
		print("There is no place in this column select another") 
	print(court)

