#idea brute force check all pairs literally
def findPair(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                print(f'Pair found {nums[i]} and {nums[j]}')

#iterator from low to high and from high to low until they meet each other
def findPairSort(nums, target):
    nums.sort()

    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target:
            print(f'Pair found {nums[low]} and {nums[high]}')
            return
        elif nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    print("no pair found")

#idea, if found the partner before in the set, then yes!
def findPairHash(nums, target):
    d = {}
    for i, el in enumerate(nums):
        if target - el in d: #if the key is in dictionary
            print(f'Pair found {nums[i]} and {nums[d.get(target - el)]}')
            return
        d[el] = i
    print("pair not found")
    print("pair not found")


if __name__ == "__main__":
    nums = [1,2,4,5,6,7]
    target = 10
    findPairHash(nums, target)