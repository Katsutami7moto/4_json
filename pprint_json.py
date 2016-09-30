import json


def load_data(filepath):
    import os
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as handle:
        return json.load(handle)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    while True:
        path = input('Input a path to your .json file: ')
        if not path:
            break
        data_to_print = load_data(path)
        if not data_to_print:
            print("File not found")
        else:
            pretty_print_json(data_to_print)
