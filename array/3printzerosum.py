#to learn: dictionary setdefault value if key not yet initialized, and value is a list
#upgrade from set from exercise 2
def insertvalue(dict, key, value):
    dict.setdefault(key, []).append(value)

def printallzero(nums):
    dict = {}
    insertvalue(dict, 0, -1)
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total in dict:
            starters = dict.get(total)
            for starter in starters:
                print(f'Zero sum at index ({starter + 1},{i})')

        insertvalue(dict, total, i)

if __name__ == "__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printallzero(nums)