import copy
import heapq
import random
import bisect

# sample1 = random.sample(range(1,1000001),1000000)
import time

#sample1 = random.sample(range(1,10000001),10000000)
sample1 = [i for i in range(1,10000001)]
sample2 = copy.deepcopy(sample1)
'''
def test_heap1(lst):
    heapq.heapify(lst)
    max_heap = heapq.heappop(lst)
    print(max_heap)
'''

def test_heap2(lst):

    print(heapq.nlargest(1,lst))

def test_bs(lst):
    idx = bisect.bisect_left(lst,10000000)

    if idx < len(lst) and lst[idx] == 10000000:
        print(lst[idx])
    else:
        print(-1)


start_time1 = time.process_time()
test_heap2(sample1)
end_time1 = time.process_time()
print(f"작동시간_heap : {end_time1 - start_time1}")

start_time2 = time.process_time()
test_bs(sample2)
end_time2 = time.process_time()
print(f"작동시간_bs : {end_time2 - start_time2}")