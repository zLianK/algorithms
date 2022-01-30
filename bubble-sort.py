from timeit import default_timer as timer


class BubbleSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        index = len(self.array)
        swapped = True

        while swapped:
            swapped = False
            for i in range(index - 1):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    index = i + 1
                    swapped = True

    def print_array(self):
        for i in range(len(self.array)):
            print(self.array[i], end=" ")
        print()


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    start = timer()
    b = BubbleSort(array)
    b.print_array()
    b.sort()
    b.print_array()

    elapsed_time = timer() - start
    print(elapsed_time)


if __name__ == "__main__":
    main()
