with open("day10_input.txt", "r") as f:
    adapter_list = [int(line.rstrip()) for line in f]
    
sorted_list = sorted(adapter_list)
threeCount = 0
oneCount = 0
max_joltage = sorted_list[-1] + 3
adapter_sorted_list = [0] + sorted_list + [max_joltage]

for i in range(1, len(adapter_sorted_list)):
    last_num = adapter_sorted_list[i-1]
    current = adapter_sorted_list[i]
    difference = current - last_num
    if(difference == 3):
        threeCount += 1
    elif(difference == 1):
        oneCount += 1

sol = {0:1}
for item in adapter_sorted_list[1:]:
    sol[item] = 0
    if item - 1 in sol:
        sol[item]+=sol[item-1]
    if item - 2 in sol:
        sol[item]+=sol[item-2]
    if item - 3 in sol:
        sol[item]+=sol[item-3]

total_ways = sol[max(adapter_sorted_list)]

print("PART 1:", threeCount * oneCount)
print("PART 2:", total_ways)
