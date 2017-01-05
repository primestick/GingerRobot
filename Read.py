# chat reading

import string

def get_user(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user.strip()

def get_message(line):
	global message
	try:
		message = (line.split(":", 2))[2]
	except:
		message = ""
	return message.strip()

def get_command(message):
	try:
		cmd = message.split(" ", 2)[0]
	except:
		cmd = ""
	return cmd.strip()

def get_argument(message):
	try:
		arg = message.split(" ", 2)[1]
	except:
		arg = ""
	return arg.strip()

def get_text(message):
	try:
		text = message.split(" ")
		del text[0:2]
		result = ' '.join(text)
	except:
		result = ""
	return result.strip()

def get_quote(message):
	try:
		quote = message.split(" ")
		del quote[0:1]
		quote = ' '.join(quote)
	except:
		quote = ""
	print ("Quote was set to {}".format(quote))
	return quote.strip()

def parse_character(message):
	try:
		player = message.split(" ")
		del player[0:1]
	except:
		player = ""
	print ("Player information parsed.")
	return player.strip()

# def message_handler(message):
