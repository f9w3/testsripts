from random import randint, choice
import time
replies = ['Is it? ','What about ','Was it ','I know now its ', 'Im thinking its ']

def aiguess(ans):
	tried = 0
	aiguess = randint(1,100)
	print(choice(replies) + str(aiguess) + '?')
	reply = input('>> ')
	
	while aiguess != ans:
	
		if 'lo' in reply.lower():
			tried += 1
			aiguess += randint(1,7)
			print(choice(replies) + str(aiguess) + '?')
			reply = input('>> ')
			
		
		elif 'hig' in reply.lower():
			tried += 1
			aiguess -= randint(1,7)
			print(choice(replies) + str(aiguess) + '?')
			reply = input('>> ')

	print('The answer was %d it took the computer %d guesses.'%(ans, tried))
	
aiguess(43)
	
	


