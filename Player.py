# player objection creation and miscellaneous functions

import random

RACES = ['human','elf','half-elf','dwarf','half-orc','kender', 'goblin','gnome']

CLASSES = ['fighter','mage', 'thief', 'cleric', 'paladin', 'ranger', 'sorcerer'
		'druid', 'peasant', 'bard', 'monk', 'barbarian']


def calculate_hp(race, c_class):

	base_age = 0
	num_of_dice = 0
	modifier_die = 0

	if race.lower() == 'human':
		base_age = 15	
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 1
			modifier = 4
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 1
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 2
			modifier = 6

	elif race.lower() == 'dwarf':
		base_age = 40
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 3
			modifier = 6
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 5
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 7
			modifier = 6

	elif race.lower() == 'elf':
		base_age = 110
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 4
			modifier = 6
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 6
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 10
			modifier = 6

	elif race.lower() == 'gnome':
		base_age = 40
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 4
			modifier = 6
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 6
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 9
			modifier = 6

	elif race.lower() == 'half-elf':
		base_age = 20
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 1
			modifier = 6
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 2
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 3
			modifier = 6

	elif race.lower() == 'half-orc':
		base_age = 14
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 1
			modifier = 4
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 1
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 2
			modifier = 6

	elif race.lower() == 'kender':
		base_age = 20
		if c_class.lower() in ['barbarian', 'thief', 'sorcerer', 'peasant']:
			num_of_dice = 2
			modifier = 4
		elif c_class.lower() in ['bard', 'fighter', 'paladin', 'ranger']:
			num_of_dice = 3
			modifier = 6
		elif c_class.lower() in ['cleric', 'druid', 'monk', 'wizard']:
			num_of_dice = 4
			modifier = 6

	elif race.lower() == 'goblin':
		base_age = 14
		num_of_dice = 1
		modifier = 6
