class SelectionSort:
    def __init__(self, A, n):
        self.A = A
        self.n = n

    def selectSort(self):
        for i in range(len(A) - 1):
            iMin = i

            for j in range(i + 1, len(A)):
                if A[j] < A[iMin]:
                    iMin = j

            temp = A[i]
            A[i] = A[iMin]
            A[iMin] = temp


if __name__ == '__main__':
    A = [2, 7, 4, 1, 5, 3]
    n = 5
    obj = SelectionSort(A, n)
    obj.selectSort()
    for i in range(len(A) - 1):
        print(A[i])
