import time
import random 

print('-'*65)
print("welcome to magic eight Ball")
print()
question= input('what is yor question? ')
time.sleep(0.7)
print('shaking!')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice= random.randint(1,6)

if choice == 1:
	print('yes')
elif choice == 2:
	print('no')
elif choice == 3:
	print('maybe')
elif choice == 4:
	print('ask later')
elif choice == 5:
	print('defenitly NO!')
elif choice == 6:
	print ('sureeeee....')

print('-'*65)