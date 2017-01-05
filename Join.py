# initiate connection to Twitch channel

from Socket import open_socket, send_message

def loading_completed(line):
	if ("End of /NAMES list" in line):
		return False
	else:
		return True

def join_chat(s):
	readbuffer_join = "".encode()
	Loading = True
	while Loading:
		readbuffer_join = s.recv(1024)
		readbuffer_join = readbuffer_join.decode()
		temp = readbuffer_join.split("\n")
		readbuffer_join = readbuffer_join.encode()
		readbuffer_join = temp.pop()
		for line in temp:
			Loading = loading_completed(line)
	print("Bot has joined the channel!")