from timeit import default_timer as timer


class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    def print_array(self):
        for i in range(len(self.array)):
            print(self.array[i], end=" ")
        print()


def main():
    array = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    start = timer()

    s = SelectionSort(array)
    s.print_array()
    s.sort()
    s.print_array()

    elapsed_time = timer() - start
    print(elapsed_time)


if __name__  == "__main__":
    main()

