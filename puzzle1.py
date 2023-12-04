with open('input1.txt') as f:
    f = f.read().splitlines()

values = []

digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def find_last(patient: str, doctor):
    index = len(patient) - 1
    while index >= 0:
        new_patient = patient[index:]
        if doctor in new_patient:
            return index
        index -= 1
    raise ValueError
        
for value in f:
    first_value = None
    last_value = None
    first_index = None
    last_index = None
    for i, x in enumerate(value):
        try:
            int(x)
        except ValueError:
            continue
        else:
            if not first_value:
                first_value = x
                first_index = i
            last_value = x
            last_index = i
    for letters, digit in digits.items():
        try:
            letters_first_index = value.index(letters)
        except ValueError:
            continue
        else:
            if letters_first_index < first_index:
                first_value = digits.get(letters)
                first_index = letters_first_index
        try:
            letters_last_index = find_last(value, letters)
        except ValueError:
            pass
        else:
            if letters_last_index > last_index:
                last_value = digits.get(letters)
                last_index = letters_last_index

    values.append(int(first_value + last_value))

        
print(values)
print(sum(values))