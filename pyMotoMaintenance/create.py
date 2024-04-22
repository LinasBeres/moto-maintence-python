import json

from pyMotoMaintenance.util import storeMotorcycle, validateMotorcycle, motorcycleMakeExists, motorcycleTypeExists

def inputFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('That is not a valid number.')
            return ''


def createMotorcycle():
    pass

def addTorqueValues(motorcycle: dict) -> dict:

    key = input('Enter torque input name: ')
    key = key.lower().strip().replace(' ', '_')

    while key != '':
        if key in motorcycle['torque_values']:
            print(f'torque {key} already in motorcycle as: {motorcycle["torque_values"][key]}')
            key = input('Enter torque input name: ')
            key = key.lower().strip().replace(' ', '_')
            continue

        newtonMetre = inputFloat('Enter Newton-metre: ')
        while newtonMetre == '':
            newtonMetre = inputFloat('Newton-metre must not be empty: ')

        footPound = inputFloat('Enter foot-pound: ')
        while footPound == '':
            footPound = inputFloat('Foot-pound must not be empty: ')

        torque = {}
        torque[key] = { 'newtonMetre': newtonMetre, 'footPound': footPound }

        agree = input(f'Torque to add: {torque} (y/n): ')

        if agree != 'n':
            motorcycle['torque_values'][key] = torque[key]

        print(f'Added: {torque}')

        key = input('Enter torque input name: ')
        key = key.lower().strip().replace(' ', '_')


    return motorcycle
