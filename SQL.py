# SQL commands

import sqlite3
import random
import Read
import Player

conn = sqlite3.connect('twitch.db')
c = conn.cursor()

def is_mod(u):
	u = u.strip()
	c.execute("SELECT * FROM moderators WHERE user = (?)", (u,))
	mod = c.fetchone()
	if mod:
		result = True
	else:
		result = False
	return result

def add_mod(u):
	u = u.strip()
	c.execute("INSERT INTO moderators VALUES (?)", (u,))
	conn.commit()
	print ("Moderator added.")

def remove_mod(u):
	u = u.strip()
	c.execute("DELETE FROM moderators WHERE user = (?)", (u,))
	conn.commit()
	print ("Moderator removed.")

def add_command(trigger, response):
	c.execute("INSERT INTO commands VALUES (?,?)", (trigger, response,))
	conn.commit()
	print ("Command added.")

def delete_command(trigger):
	c.execute("DELETE FROM commands WHERE trigger = (?)", (trigger,))
	conn.commit()
	print ("Command deleted.")

def modify_command(trigger, response):
	c.execute("UPDATE commands SET response = (?) WHERE trigger = (?)", (response, trigger,))
	conn.commit()
	print ("Command Updated.")

def get_commands():
	c.execute("SELECT trigger FROM commands")
	commands = c.fetchall()
	return commands

def run_command(trigger):
	c.execute("SELECT response FROM commands WHERE trigger = (?)", (trigger,))
	response = c.fetchone()
	r = str(response[0])
	return r

def add_quote(quote):
	c.execute("INSERT INTO quotes VALUES (?,?)", (None, quote,))
	conn.commit()
	print ("Quote added.")

def get_quote():
	c.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;")
	result = c.fetchone()
	quote = "Quote #" + str(result[0]) + ": " + str(result[1])
	return quote.strip()

def add_suggestion(suggestion):
	c.execute("INSERT INTO suggestions VALUES (?,?)", (None, suggestion,))
	conn.commit()
	print ("Suggestion added.")

def get_suggestions():
	c.execute("SELECT suggestion, count(suggestion) FROM suggestions GROUP BY suggestion ORDER BY count(suggestion) DESC LIMIT 3")
	r = c.fetchall()
	return r

def purge_suggestions():
	c.execute("DELETE FROM suggestions")
	c.execute("VACUUM")
	conn.commit()

# pid, name, race, sex, class, hp, age, religion, str, dex, con, wis, int, xp
def create_character(user, player):
	name = player[0]
	race = player[1]
	c_class = player[2]
	sex = player[3]
	hp = calculate_hp(race, c_class)
	age = get_player_age(race)
	c.execute("INSERT INTO players VALUES (?,?,?,?,?,?,?)", (user, name, race, 
															c_class, sex, hp, age, None, 
															None, None, None, None, None))
	conn.commit()

