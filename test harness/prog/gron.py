import json
import sys

def flatten_json(json_obj, parent_key='', sep='.'):
    flattened = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_json(value, new_key, sep=sep))
        else:
            flattened[new_key] = value
    return flattened

def main():
    if len(sys.argv) == 1:
        # Read from stdin
        input_json = sys.stdin.read()
    else:
        # Read from file
        try:
            with open(sys.argv[1], 'r') as file:
                input_json = file.read()
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found.")
            sys.exit(1)

    try:
        json_obj = json.loads(input_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    flattened_json = flatten_json(json_obj)

    for key, value in flattened_json.items():
        print(f"{key} = {json.dumps(value)};")

    sys.exit(0);

if __name__ == "__main__":
    main()
