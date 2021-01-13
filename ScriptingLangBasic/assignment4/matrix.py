"""
You are given a text file ‘matrix1.txt’. This file contains the values of a 4x6 matrix. Write a
function that storesthe values from this files into a two-dimensional(i.e. nested) list. This
means you will end up with one variable that contains all the values. Make sure your function
is able to read a matrix of any size.
"""


def TextToMatrix(file):
    with open(file, 'r') as f:
        matrix = f.readlines()
    m = []
    for line in matrix:
        values = line.split(" ")
        intValues = [int(v) for v in values if v != '\n']
        m.append(intValues)
    return m


print(TextToMatrix("matrix1.txt"))


"""
Write a new function that writes a nested list to a file, organized in the same way as the data
in ‘matrix1.txt’ (i.e. each row of the matrix will be a sub-list in your nested list). Test your
function by writing the result of the function written in question 3a)to a new file.

"""
def MatrixToText(m):
    temp = []
    for row in m:
        stringValues = [str(v) for v in row]
        stringValues += ['\n']
        stringValues = " ".join([v for v in stringValues])
        temp.append(stringValues)
        f = open("myfile.txt", "w")
        for line in temp:
            f.write(line)
        f.close()

MatrixToText(TextToMatrix("matrix1.txt"))
