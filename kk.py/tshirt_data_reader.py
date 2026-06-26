import csv

def read_data(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                return None

            return data

    except Exception as e:
        print(f"Error reading file: {e}")
        return None