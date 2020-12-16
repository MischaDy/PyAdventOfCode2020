input_ = '6,19,0,5,7,13,1'
num_iterations = 30000000
starting_nums = list(map(int, input_.split(',')))
last_times_spoken_dict = dict(zip(starting_nums, range(1, len(starting_nums) + 1)))
last_time_spoken = None  # assume that starting nums contain no duplicates
for turn in range(len(starting_nums) + 1, num_iterations + 1):
    spoken_num = 0 if last_time_spoken is None else (turn - 1) - last_time_spoken
    last_time_spoken = last_times_spoken_dict[spoken_num] if spoken_num in last_times_spoken_dict else None
    last_times_spoken_dict[spoken_num] = turn
print(spoken_num)
