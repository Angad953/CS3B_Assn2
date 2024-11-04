# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 2
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu

def match(d1, d2):
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            print(f"{key}: {d1[key]} is present in both dictionaries")


def run():
    print("===== Question 2 =====")
    # implement your code here
    d1 = {'key1': 1, 'key2': 3, 'key3': 2}
    d2 = {'key1': 1, 'key2': 2}
    match(d1, d2)
    scores = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    print(sorted_scores)

