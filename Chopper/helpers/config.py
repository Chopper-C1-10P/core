import json

def config(filename, key):
    with open(f"K-2SO/{filename}", "r") as c:
        config = json.load(c)
    return config[key]
