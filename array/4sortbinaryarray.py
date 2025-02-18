def sortLinear1(nums):
    zerocounts = nums.count(0)
    newlist = []
    for _ in range(zerocounts):
        newlist.append(0)
    for _ in range(zerocounts+1, len(nums)+1):
        newlist.append(1)
    print(newlist)

#create new list and add counted 0 to the first
def sortLinear2(nums):
    newlist = []
    for el in nums:
        if el == 0:
            newlist.append(0)
    for _ in range(len(newlist), len(nums)):
        newlist.append(1)
    print(newlist)

#putting nach und nach 0 to the 1, 2, 3 position by swapping the position of the 1, 2, 3
def quicksort(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            swap(nums, i, j)
            j+=1
    print(nums)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

if __name__ == "__main__":
    nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sortLinear1(nums)
    sortLinear2(nums)
    quicksort(nums)