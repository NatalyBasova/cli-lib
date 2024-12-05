import json


def read_data(path: str):
    with open(path, "r") as file:
        data = json.load(file)

    return data


def save(path: str, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
