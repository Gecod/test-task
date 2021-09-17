numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

# way #1
new_nums_1 = list(x for x in numbers if x % 2 == 1 and x > 50)
print(new_nums_1)

# way #2
def filter_nums(nums):
    new_nums = []
    
    for i in nums:
        if i % 2 == 1 and i > 50:
            new_nums.append(i)
            
    return new_nums

new_nums_2 = filter_nums(numbers)
print(new_nums_2)
