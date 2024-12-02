from src.api.client import get_data
import json

def main():
    data = get_data('users')

    print(json.dumps(data, indent=4))

main()