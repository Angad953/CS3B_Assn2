# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 4
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu


def kth(n, k):
    if n == 1:
        return 0
    i = (k + 1) // 2
    is_even = k % 2 == 0
    sym = kth(n - 1, i)
    if sym == 0:
        return 1 if is_even else 0
    else:
        return 0 if is_even else 1


def run():
    print("===== Question 4 =====")
    # implement your code here
    print(kth(1, 1))
    print(kth(2, 2))
    print(kth(4, 5))

