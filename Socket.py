# socket information

from socket import socket
from Settings import SERVER, PORT, PASS, BOT, CHANNEL

def open_socket():

	s = socket()
	s.connect((SERVER, PORT))
	s.send(("PASS " + PASS + "\r\n").encode())
	s.send(("NICK " + BOT + "\r\n").encode())
	s.send(("JOIN #" + CHANNEL + "\r\n").encode())
	return s

def send_message(s, message):
	message_temp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send((message_temp + "\r\n").encode())