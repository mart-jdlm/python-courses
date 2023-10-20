import numpy as np

def exercise1():
    vector = np.arange(21)
    vector[9:16] *= -1
    print(vector)

def exercise2():
    vector = np.arange(15, 56)
    print(vector[1:-1])

def exercise3():
    array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
    for row in array:
        for element in row:
            print(element)

def exercise4():
    vector = np.linspace(5,50,10)
    print(vector)

def exercise5():
    vector = np.random.randint(0, 11, 5)
    print(vector)

def exercise6():
    vector1 = np.array([1, 2, 3, 4])
    vector2 = np.array([5, 6, 7, 8])
    result = vector1 * vector2
    print(result)

def exercise7():
    values = np.arange(10, 22)
    matrix = values.reshape(3,4)
    print(matrix)

def exercise8():
    matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    print(f"Number of rows: {rows}")
    print(f"Number of columns: {columns}")

def exercise9():
    x = np.zeros((4, 4))
    x[::2, 1::2] = 1
    x[1::2, ::2] = 1
    print(x)

def exercise10():
    array1 = np.array([0, 10, 20, 40, 60])
    print("Array1: ",array1)
    array2 = [10, 30, 40]
    print("Array2: ",array2)
    print("Common values between two arrays:")
    print(np.intersect1d(array1, array2))

def exercise11():
    x = np.array([10, 10, 20, 20, 30, 30])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))
    x = np.array([[1, 1], [2, 3]])
    print("Original array:")
    print(x)
    print("Unique elements of the above array:")
    print(np.unique(x))

def exercise12():
    p = [[1, 0], [0, 1]]
    q = [[1, 2], [3, 4]]
    print("original matrix:")
    print(p)
    print(q)
    result1 = np.cross(p, q)
    result2 = np.cross(q, p)
    print("cross product of the said two vectors(p, q):")
    print(result1)
    print("cross product of the said two vectors(q, p):")
    print(result2)

def exercise13():
    z= np.random.random((10,2))
    x,y = z[:,0], z[:,1]
    r = np.sqrt(x**2+y**2)
    t = np.arctan2(y,x)
    print(r)
    print(t)

def exercise14():
    x = np.arange(100)
    print("Original array:")
    print(x)
    a = np.random.uniform(0,100)
    print("Value to compare:")
    print(a)
    index = (np.abs(x-a)).argmin()
    print(x[index])

def main():
    while True:
        try:
            print("Choose an exercise number (1 through 14) or 'q' to quit:")
            exercise = input()

            if exercise == 'q':
                print("Program terminated.")
                break

            exercise = int(exercise)
            if 1 <= exercise <= 14:
                globals()[f'exercise{exercise}']()
            else:
                print("Unknown exercise. Please enter a number between 1 and 14, or 'q' to quit.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
