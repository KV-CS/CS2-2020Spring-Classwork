#3-16-2020

import time

def linear (x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
        return -1

#Create small list
small_list = [1,2,3,4,5,6,7]

start_time = time.time()
linear(5, small_list)
print("--- {} seconds ---".format(time.time() - start_time))


#print("--- %s seconds ---" % (time.time() - start_time))
