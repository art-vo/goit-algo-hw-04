'''

'''

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:     # We open the file for reading with an indication of encoding
            for line in file:
                values = line.strip().split(',')            # We separate the line by commas and get a list of values
                if len(values) >= 3:                        # If the list has at least three elements (id, name, age)
                    cat_info = {                            # We create a dictionary with information about the cat and add it to the list
                        "id": values[0].strip(),
                        "name": values[1].strip(),
                        "age": values[2].strip() }
                    cats_info.append(cat_info)
        return cats_info                                    # We return the list of dictionaries with information about cats

    except FileNotFoundError:
        print("File not found.")                            # File not found case
    except Exception as e:
        print("An error occurred:", e)                      # The case when another error occurred

cats_info = get_cats_info("hw4_2/cats_file.txt")
print(cats_info)
