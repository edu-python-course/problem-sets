# Triangle classification #81
# https://github.com/edu-python-course/problem-sets/issues/81

if __name__ == "__main__":
    a = input("Enter a side length: ")
    b = input("Enter b side length: ")
    c = input("Enter c side length: ")

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
