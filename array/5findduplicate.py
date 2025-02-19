
def findDuplicate(nums):
    visitedlist = [False] * (len(nums))
    duplicates = []
    for i in nums:
        if visitedlist[i]:
            duplicates.append(i) 
        visitedlist[i] = True
    return duplicates



if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 6, 7, 8, 6]
    print(findDuplicate(nums))