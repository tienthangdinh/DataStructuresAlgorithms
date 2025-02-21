#idea: for each i, keep track of the longest track so that the sum is subtrack length - 1

def myImplementation(nums): #also correct
    longesttrack = (0,0)
    for i in range(len(nums)):
        sum = nums[i]
        longestj = 0
        for j in range(i, len(nums)):
            sum+= nums[j]
            if sum == j - i:
                longestj = j
        longesttrack = (i, longestj)
    print(nums[longesttrack[0]:longesttrack[1]])

def consecutive(nums, i, j, minval, maxval):
    if maxval - minval != j - i: #make sure its exactly the correct size, very clever
        return False
    visited = [False] * (j - i + 1) #make sure no duplicate
    for k in range(i, j + 1):
        #if the element has seen before, duplicate
        if visited[nums[k] - minval]:
            return False
        visited[nums[k] - minval] = True
    return True

def findMaxSublist(nums):
    length = 1
    start = end = 0
    for i in range(len(nums) - 1):
        minval = nums[i]
        maxval = nums[i]
        for j in range(i + 1, len(nums)):
            minval = min(minval, nums[j])
            maxval = max(maxval, nums[j])

            if consecutive(nums, i, j, minval, maxval):
                if length < maxval - minval + 1: #only update this if the current found sublist shorter than what we have found before
                    length = maxval - minval + 1
                    start = i
                    end = j
    print("The largest sublist is", (start, end))

if __name__ == "__main__":
    A = [2, 0, 2, 1, 4, 3, 1, 0]
 
    findMaxSublist(A)