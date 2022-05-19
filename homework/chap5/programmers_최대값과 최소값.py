s = "11 21 31 41"


a = s.split(" ")

max = int(a[0])
min = int(a[len(a) - 1])
for num in a:
    num = int(num)
    if num > max:
        max = num
    else:
        min = num

answer = str(min) + ' ' + str(max)
print(answer)
