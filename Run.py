# Twitch bot written by TheAngryGinger (Brandon C. Brown) aka TAG
# https://www.twitch.tv/theangryginger
# Source Code: 
# Free to Use/modify, just credit appropriately please

from Join import join_chat
from Read import get_user, get_quote, get_message, get_argument, get_command, get_text, parse_character
import Settings
import SQL
import string
from Socket import open_socket, send_message

### Functions

s = open_socket()
join_chat(s)
readbuffer = ""
commands = SQL.get_commands()

def Console(line):
	# gets if it is a user or twitch servers
	if "PRIVMSG" in line:
		return False
	else:
		return True

while True:
		try:
			readbuffer = s.recv(1024)
			readbuffer = readbuffer.decode()
			temp = readbuffer.split("\n")
			readbuffer = readbuffer.encode()
			readbuffer = temp.pop()
		except:
			temp = ""
		for line in temp:
			if line == "":
				break
			# So twitch doesn't timeout the bot.
			if "PING" in line and Console(line):
				msgg = "PONG tmi.twitch.tv\r\n".encode()
				s.send(msgg)
				print(msgg)
				break
			# get user
			user = get_user(line)
			# get message send by user
			message = get_message(line)
			# for you to see the chat from CMD
			print(user + " >> " + message)
			# sends private msg to the user (start line)
			PMSG = "/w " + user + " "

################################# Hard-coded Commands ######################

			cmd = get_command(message)
			arg = get_argument(message)
			text = get_text(message)

			# iterate through custom commands to find a match
			for command in commands:
				if command[0] in cmd:
					response = SQL.run_command(command[0])
					send_message(s, response)
					break
			
			# simple ping response
			if message.startswith("!ping"):
				send_message(s, "PONG!")
				break
			
			# add quote for user
			if message.startswith("!addquote"):
				quote = get_quote(message)
				SQL.add_quote(quote)
				break

			# display quote
			if message.startswith("!quote"):
				quote = SQL.get_quote()
				send_message(s, quote)

			# add command 
			# syntax: !addcom <new command> <command text>
			if SQL.is_mod(user) and message.startswith("!addcom"):
				# add this command
				SQL.add_command(arg, text)
				commands = SQL.get_commands()
				break
			
			# delete a command
			# syntax: !delcom <command>
			if SQL.is_mod(user) and message.startswith("!delcom"):
				# remove this command
				SQL.delete_command(arg)
				commands = SQL.get_commands()
				break
			
			# modify a current command 
			# maybe check to see if command is valid first
			if SQL.is_mod(user) and message.startswith("!modcom"):
				SQL.modify_command(arg, text)
				break
			
			# add a moderator
			# syntax: !addmod <username>
			if SQL.is_mod(user) and message.startswith("!addmod"):
				SQL.add_mod(arg)
				break
			
			# remove a moderator
			# syntax: !delmod <username>
			if SQL.is_mod(user) and message.startswith("!delmod"):
				SQL.remove_mod(arg)
				break
			
			# ban a user
			# syntax: !ban <username>
			if SQL.is_mod(user) and message.startswith("!ban"):
				break
			
			# timeout a user
			# syntax: !timeout <username>
			if SQL.is_mod(user) and message.startswith("!timeout"):
				break

			# user add suggestions for games to be played - similar to Lirik's
			# Sub sunday 
			if message.startswith("!suggestgame"):
				suggestion = get_quote(message)
				SQL.add_suggestion(suggestion)
				break

			# retrieves top 3 recommended games
			if SQL.is_mod(user) and message.startswith("!suggestions"):
				suggestions = SQL.get_suggestions()
				for suggestion in suggestions:
					sugg = "{} had {} votes".format(suggestion[0], suggestion[1])
					send_message(s, sugg)
				break

			# resets the suggestions table
			if (user == Settings.OWNER) and message.startswith("!purgegames"):
				SQL.purge_suggestions()
				break

			# creates a new player character for the user
			if message.startswith("!createplayer"):
				SQL.create_character(user, parse_character(message))
				break

############################################################################