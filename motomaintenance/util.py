import json

from pathlib import Path
from importlib.resources import files

from jsonschema import validate

MOTODATABASE = 'motomaintence.moto-maintenance-db.db'
MOTOSCHEMA = 'motomaintence.moto-maintenance-db.schema'
MAINTENANCESCHEMA = 'maintenance.schema.json'

def iter_motorcycle_makes() -> str:
    for resource in files(MOTODATABASE).iterdir():
        if resource.is_dir():
            yield resource.name

def iter_motorcycle_types(motorcycleMake: str) -> str:
    for resource in files(MOTODATABASE).joinpath(motorcycleMake).iterdir():
        if resource.is_file():
            yield Path(resource.name).stem

def motorcycle_make_exists(motorcycleMake: str) -> bool:
    for make in iter_motorcycle_makes():
        if motorcycleMake.lower() == make:
            return True

    return False

def motorcycle_type_exists(motorcycleMake: str, motorcycleType: str) -> bool:
    for motoType in iter_motorcycle_types(motorcycleMake):
        if motorcycleType.lower() == motoType:
            return True

    return False

def load_motorcycle_maintenance(motorcycleMake: str, motorcycleType: str, safe=True) -> dict:
    outDict = {}

    if safe:
        if not motorcycle_make_exists(motorcycleMake):
            print(f"Warning: motorcycle make '{motorcycleMake}' doesn't exist!")
            return outDict
        if not motorcycle_type_exists(motorcycleMake, motorcycleType):
            print(f"Warning: motorcycle type '{motorcycleType}' doesn't exist!")
            return outDict

    makeDatabase = f'{MOTODATABASE}.{motorcycleMake}'

    with files(makeDatabase).joinpath(f'{motorcycleType}.json').open('r') as fl:
        outDict = json.load(fl)

    return outDict

def load_motorcycle_maintenances(motorcycles: dict, safe=True) -> dict:
    motoDict = {}

    for motoMake, motoType in motorcycles.items():
        motoDict[motoType] = load_motorcycle(motoMake, motoType, safe)

    return motoDict

def validate_motorcycle(motorcycle: dict) -> bool:
    with files(MOTOSCHEMA).joinpath(MAINTENANCESCHEMA).open('r') as fl:
        schema = json.load(fl)

    try:
        validate(instance=motorcycle, schema=schema)
        return True
    except ValidationError as err:
        print(err)
        return False

def store_motorcycle(motorcycle: dict, outFile="") -> bool:
    if outFile == '':
        outFile = f'{motorcycle["model"]}_{motorcycle["years"]}.json'

    if not validate_motorcycle(motorcycle):
        print("not valid motorcycle")
        return False

    with open(outFile, 'w', encoding='utf-8') as f:
        json.dump(motorcycle, f, ensure_ascii=False, indent=4)

    return True
