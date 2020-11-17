import os

def gen():
	stream = os.popen('curl -v -X POST https://postb.in/api/bin')
	output = stream.read()

	file = open("binID.txt", "w")
	file.write(output[10:37])
	file.close()