# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 3
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu

def reverse(sentence):
    words = sentence.split(' ')
    rw = ' '.join(word[::-1] for word in words)
    return rw


def run():
    print("===== Question 3 =====")
    # implement your code here
    istr = "Let's take LeetCode contest"
    ostr = reverse(istr)
    print(ostr)

