from timeit import default_timer
import numpy as np

t1 = default_timer()
# ---
input_ = '0,3,6'  # '6,19,0,5,7,13,1'
test_solution = 175594  # 436

num_iterations = 30000000
starting_nums = list(map(int, input_.split(',')))
last_times_spoken_arr = [0 for _ in range(num_iterations)]  # np.zeros(num_iterations, dtype=np.long)
for turn, num in enumerate(starting_nums, start=1):
    last_times_spoken_arr[num] = turn

last_time_spoken = 0  # assume that starting nums contain no duplicates
for turn in range(len(starting_nums) + 1, num_iterations + 1):
    if turn % 1000000 == 0:
        print(turn)
    spoken_num = 0 if last_time_spoken == 0 else (turn - 1) - last_time_spoken
    last_time_spoken = last_times_spoken_arr[spoken_num]  # if spoken_num in last_times_spoken_arr else None
    last_times_spoken_arr[spoken_num] = turn
# ---
t2 = default_timer()
print(spoken_num, spoken_num == test_solution)
print(t2 - t1)

# dict: 22.269
# np.zeros as longs: ~30s
# list comprehension: 20s