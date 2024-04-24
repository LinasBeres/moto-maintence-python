import json

from motomaintence.util import store_motorcycle, validate_motorcycle, motorcycle_make_exists, motorcycle_type_exists

def input_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print('That is not a valid number.')


def create_motorcycle():
	pass

def add_torque_values(motorcycle: dict) -> dict:

	key = input('Enter torque input name: ')
	key = key.lower().strip().replace(' ', '_')

	while key != '':
		if key in motorcycle['torque_values']:
			print(f'torque {key} already in motorcycle as: {motorcycle["torque_values"][key]}')
			key = input('Enter torque input name: ')
			key = key.lower().strip().replace(' ', '_')
			continue

		newtonMetre = input_float('Enter Newton-metre: ')

		footPound = input_float('Enter foot-pound: ')

		torque = {}
		torque[key] = { 'newtonMetre': newtonMetre, 'footPound': footPound }

		agree = input(f'Torque to add: {torque} (y/n): ')

		if agree != 'n':
			motorcycle['torque_values'][key] = torque[key]
			print(f'Added: {torque}')

		key = input('Enter torque input name: ')
		key = key.lower().strip().replace(' ', '_')


	return motorcycle
