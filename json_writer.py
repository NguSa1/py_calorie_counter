import os
import json


def json_write():
    if os.path.isfile("target_row.json"):
        with open("target_row.json", "r") as read:
            load_data = json.load(read)
            print(load_data)

            with open("target_row.json", "w") as write:
                json.dump(load_data, write, indent=4)
                write.close()
        return load_data["target_row"]

    else:
        with open("target_row.json", "w") as write:
            json.dump(dict(target_row=0), write, indent=4)
            write.close()

        with open("target_row.json", "r") as read:
            load_data = json.load(read)
            load_data["target_row"] = 3
            print(load_data)

            with open("target_row.json", "w") as write:
                json.dump(load_data, write, indent=4)
                write.close()
        return load_data["target_row"]


def json_load():
    with open("target_row.json", "r") as read:
        load_data = json.load(read)
        return load_data["target_row"]


def json_reset():
    with open("target_row.json", "w") as write:
        json.dump(dict(target_row=0), write, indent=4)
        write.close()
