import json

from pathlib import Path
from importlib.resources import files

_motoDatabase = 'pyMotoMaintence.moto-maintenance-db.db'

def iterMotorcycleMakes() -> str:
    for resource in files(_motoDatabase).iterdir():
        if resource.is_dir():
            yield resource.name

def iterMotorcycleTypes(motorcycleMake: str) -> str:
    for resource in files(_motoDatabase).joinpath(motorcycleMake).iterdir():
        if resource.is_file():
            yield Path(resource.name).stem

def motorcycleMakeExists(motorcycleMake: str) -> bool:
    for make in iterMotorcycleMakes():
        if motorcycleMake.lower() == make:
            return True

    return False

def motorcycleTypeExists(motorcycleMake: str, motorcycleType: str) -> bool:
    for motoType in iterMotorcycleTypes(motorcycleMake):
        if motorcycleType.lower() == motoType:
            return True

    return False

def loadMotorcycleMaintence(motorcycleMake: str, motorcycleType: str, safe=True) -> dict:
    outDict = {}

    if safe:
        if not motorcycleMakeExists(motorcycleMake):
            print(f"Warning: motorcycle make '{motorcycleMake}' doesn't exist!")
            return outDict
        if not motorcycleTypeExists(motorcycleMake, motorcycleType):
            print(f"Warning: motorcycle type '{motorcycleType}' doesn't exist!")
            return outDict

    makeDatabase = f'{_motoDatabase}.{motorcycleMake}'

    with files(makeDatabase).joinpath(f'{motorcycleType}.json').open('r') as fl:
        outDict = json.load(fl)

    return outDict

def loadMotorcycleMaintences(motorcycles: dict, safe=True) -> dict:
    motoDict = {}

    for motoMake, motoType in motorcycles.items():
        motoDict[motoType] = loadMotorcycle(motoMake, motoType, safe)

    return motoDict
