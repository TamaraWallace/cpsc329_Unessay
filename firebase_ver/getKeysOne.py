from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)

result = firebase.get('person', None)

file = open("log.txt", "a", encoding="utf-8")
for x in result:
	file.write(x+":\n")
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