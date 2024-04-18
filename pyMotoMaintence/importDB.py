import json

from importlib.resources import files


def importBD():
    print(__file__)

    with files('pyMotoMaintence.moto-maintenance-db.db.suzuki').joinpath('dl650_04-11.json').open('r') as fl:
        json.load(fl)
