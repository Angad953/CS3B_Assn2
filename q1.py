# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 1
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu

def create_dict(keys, values):
    result = {}

    for key, value in zip(keys, values):
        # Use a set to store values to avoid duplicates
        if key in result:
            result[key].add(value)
        else:
            result[key] = {value}

    return result


def run():
    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    color_list = [
        {'color_name': name, 'color_code': code}
        for name, code in zip(color_names, color_codes)
    ]
    print(color_list)
    keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
    values = [1, 2, 2, 3]
    output_dict = create_dict(keys, values)
    print(output_dict)


