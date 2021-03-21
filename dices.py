import random

print('Welcome to THE GAME')
y = input('Ready to roll the dices? (y/n')
wincount = 0
while y=='y':
	print('Computer rolls:')
	ca = random.randint(1,6)
	cb = random.randint(1,6)
	print(ca,cb)
	print('You roll:')
	ha = random.randint(1,6)
	hb = random.randint(1,6)
	print(ha,hb)
	if ca == cb:
	   rc = (ca+cb)*2
	else:
	 	rc = ca +cb
	if ha == hb:
		rh = (ha + hb)*2
	else:
		rh = ha + hb
	print('Computer score:', rc)
	print('Human score:', rh)
	
	if rc < rh:
		wincount = wincount + 1
		print('You win!')
	elif rc>rh:
		wincount-= 1
		print('You loose... It was just a fight though, not the war !')
	else:
		print('We have a draw! Draw swords again??')
	print('Win score', wincount)
	y = input('Play again?? y/n')
	if y=='n':
		print('Goodbye Sir... wincount: ', wincount)
		break
		