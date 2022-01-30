from timeit import default_timer as timer


class ShakerSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        min_index = 1
        max_index = len(self.array) - 1
        swapped = True

        while swapped:
            swapped = False
            for i in range(max_index, min_index - 1, -1):
                if self.array[i] < self.array[i-1]:
                    self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
                    min_index = i + 1
                    swapped = True

            for i in range(min_index, max_index + 1):
                if self.array[i] < self.array[i-1]:
                    self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
                    max_index = i - 1
                    swapped = True

    def print_array(self):
        for i in range(len(self.array)):
            print(self.array[i], end=" ")
        print()


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    start = timer()
    s = ShakerSort(array)
    s.print_array()
    s.sort()
    s.print_array()

    elapsed_time = timer() - start
    print(elapsed_time)


if __name__ == "__main__":
    main()
