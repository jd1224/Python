
spaces = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
print (spaces[1])
player1 = ''
player2 = ''

winner = False
full = False

def board_init():
	global spaces
	global full
	global winner
	full = False
	winner = False
	for i in range(1,10):
		spaces[i] = ' '

def player_choice():
	global player1
	global player2
	choice = input('Player 1, would you like to be X or O? ')
	if choice.lower()=='x':
		player1 = 'X'
		player2 = 'O'
	else:
		player1='O'
		player2='X'

def print_board():
	
	global spaces
	global winner
	#sides *************************************
	#tops  *******************************************************************************************
	print ('*******************************************************************************************')
	print ('************************************     |     |     **************************************')
	print ('************************************  {}  |  {}  |  {}  **************************************'.format(spaces[7],spaces[8],spaces[9]))
	print ('************************************     |     |     **************************************')
	print ('************************************-----------------**************************************')
	print ('************************************     |     |     **************************************')
	print ('************************************  {}  |  {}  |  {}  **************************************'.format(spaces[4],spaces[5],spaces[6]))
	print ('************************************     |     |     **************************************')
	print ('************************************-----------------**************************************')
	print ('************************************     |     |     **************************************')
	print ('************************************  {}  |  {}  |  {}  **************************************'.format(spaces[1],spaces[2],spaces[3]))
	print ('************************************     |     |     **************************************')
	print ('*******************************************************************************************')
	

def gameplay():
	turn = 1
	board_init()
	running = True
	choicesList = ['1','2','3','4','5','6','7','8','9']
	while running:
		print_board()
		choice = (input('*************************************Choose a square Player {}: '.format(turn)))
		if choice in choicesList:
			choice = int(choice)
			if check_choice(choice):
				turn = mark(turn,choice)
			else:
				print('*************************************That square is already full!*************************************')
			check_board()
			if winner:
				print("*************************************Congratualation you've won*************************************")
				print_board()
				break
			if full:
				print_board()
				print('************************************    ./\.../\\     **************************************')
				print("************************************    (.'0 0'.)    **************************************")
				print('************************************      | . |      **************************************')
				print('************************************    (.\|.|/.)    **************************************')
				print("***********************************This is the Cat's Game**********************************")
				break
		else:
			print('INVALID CHOICE')
			
def check_choice(choice):
	if not spaces[choice]==' ':
		return False
	else:
		return True
	
def mark(turn,choice):
		if turn==1:
			spaces[choice]=player1
			return 2
		else:
			spaces[choice]=player2
			return 1
	
def check_board():
	global winner
	global full
	count = 0
	for i in range(1,10):
		if not spaces[i] == ' ':
			count +=1
	print ('This is the count {}'.format(count))
	if count == 9:
		full = True
	if spaces[1]==spaces[4] ==spaces[7] !=' ' :
		winner = True
	elif spaces[1]==spaces[2]==spaces[3]!=' ':
		winner = True
	elif spaces[1]==spaces[5]==spaces[9]!=' ':
		winner = True
	elif spaces[2]==spaces[5]==spaces[8]!=' ':
		winner = True
	elif spaces[3]==spaces[6]==spaces[9]!=' ':
		winner = True
	elif spaces[4]==spaces[5]==spaces[6]!=' ':
		winner = True
	elif spaces[7]==spaces[5]==spaces[3]!=' ':
		winner = True
	elif spaces[7]==spaces[8]==spaces[9]!=' ':
		winner = True

def play_again():
	answer = input('Play another Game? (Y/N) ')
	return answer.lower() == 'y'
	

def run():
	playing = True
	while playing:
		player_choice()
		gameplay()
		playing = play_again()
		
	print('*************************************Goodbye*************************************')	
run()