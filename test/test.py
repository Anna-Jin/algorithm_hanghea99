d = [1,3,2,5,4]
budget = 9


total = 0
count = 0

for num in sorted(d):
    total += num
    if total > budget:
        break
    count += 1

print(count)