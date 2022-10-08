def main():

    def iteration(nums):
        add = lambda a, b: a + b
        sub = lambda a, b: a - b
        mul = lambda a, b: a * b
        div = lambda a, b: a / b
        new_nums = set(nums)
        operations = [add, sub, mul, div]
        for i in nums:
            for o in nums:
                for u in operations:
                    if o != 0:
                        new_nums.add(u(i,o))
                    if i != 0:
                        new_nums.add(u(o,i))
        return new_nums
        
    n1, n2, n3, n4 = 0, 0, 0, 0
    nums = [n1, n2, n3, n4]
    for i in range(len(nums)):
        nums[i] = int(input('input a number: '))

    final_nums = iteration(iteration(iteration(nums)))

    if 24 in final_nums:
        print('possible')
        
    

if __name__ == '__main__':
    while True:
        main()
