import bubble_sort
import time

L = [2, 5, 31, 6, 8, 4, 7, 9, 1, 42, 52, 35, 100, 11, 0, 13, 19, 71, 47, 3089, 231, 482, 91238, 432, 43, 6, 87, 33, 57, 981, 24, 19, 22, 1001]

start_long = time.time()
bubble_sort.BubbleSort_long(L)
end_long = time.time()
print("The LONG version of BubbleSort took {} seconds.".format(end_long - start_long))

start_short = time.time()
bubble_sort.BubbleSort_short(L)
end_short = time.time()
print("The SHORT version of BubbleSort took {} seconds.".format(end_short - start_short))