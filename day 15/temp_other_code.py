import numpy as np

from numba import njit
from numba import types
from numba.typed import Dict


nums = np.array([11, 0, 1, 10, 5, 19], dtype=np.int64)


@njit("int64(int64[:], int64)")
def day15(nums, N):
    last = np.full(N, -1, dtype=np.int64)
    for i, x in enumerate(nums[:-1]):
        last[x] = i
    buffer = nums[-1]
    for i in range(len(nums) - 1, N - 1):
        y = 0 if last[buffer] == -1 else i - last[buffer]
        last[buffer], buffer = i, y
    return buffer


# print(day15(nums, 2020))
print(day15(nums, 30000000))
