#main idea to learn: as long as the accumulator comes back at a value in the past, it means the last sublist is a zero sum
#to learn: initializing a set and add new element
def zerosum(nums):
    accuset = set()
    total = 0
    for i in nums:
        total += i
        if total in accuset:
            return True
        accuset.add(total)
    return False

if __name__ == "__main__":
    nums = [4, -6, 3, -1, 4, 2, 7]
    if zerosum(nums):
        print("sum exists")
    else:
        print("not exist")