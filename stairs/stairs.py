def solution(n):
    total = 0

    # Fun word problem aside, this is a recursive combination set algorithm
    for combo in combo_generator(n):
        total += 1
        # print(combo)

    return total


def combo_generator(target):
    # Initialize list of every positive integer to n - 1
    addends = [i for i in range(1, target)]
    # Initialize dictionary for mapping addends
    sumMap = {0: [-1]}

    # Populate map
    # Keys are the pointers to other keys with paths to addends
    # Values are lists that point to indices in addends
    for i in range(len(addends)):
        indexKeys = list(sumMap.keys())
        for j in indexKeys:
            newSum = j + addends[i]

            if (newSum - target) > 0: pass

            if newSum in sumMap:
                sumMap[newSum].append(i)
            else:
                sumMap[newSum] = [i]

    def recursive_search(newTarget, maxTarget):
        for a in sumMap[newTarget]:

            # Zero condition met, exit recursion
            if a == -1:
                yield []

                # If addend in map is larger than previous target
                # stop computing, as it can't be in the combo
            elif a >= maxTarget:
                break

            else:
                # Continue to search for valid addends, in descending order
                # until zero condition is met
                for answer in recursive_search(newTarget - addends[a], a):
                    answer.append(addends[a])
                    yield answer

    for answer in recursive_search(target, len(addends)):
        yield answer


def findCombinationsUtil(arr, index, num, reducedNum):

    if (reducedNum < 0):
        return
    if (reducedNum == 0):
        # print(arr[:index])
        yield arr

    prev = 1 if index == 0 else arr[index - 1]

    for k in range(prev, num):
        unique = True
        for i in range(index):
            if arr[i] == k:
                unique = False
                break

        if unique:
            arr[index] = k
            for combo in findCombinationsUtil(arr, index + 1, num, reducedNum - k):
                yield combo



def findCombinations(n):
    arr = [0] * n
    total = 0

    for combo in findCombinationsUtil(arr, 0, n, n):
        total += 1
    return total


f = 199
n = 200
print(f"Benchmark for {n}")
import time
start = time.perf_counter()
# combos = solution(n)
# comboStr = f"found {combos} combinations in {time.perf_counter() - start} seconds"
# print(comboStr)
# totals = [solution(i) for i in range(3, n + 1)]

with open('combos.txt', 'r') as reader:
    combos = reader.read()
with open('combos.txt', 'w') as writer:
    writer.write(combos)
    for i in range(f + 1, n + 1):
        comboStr = f"if n == {i}: return {solution(i)}"
        writer.write(comboStr + "\r")
# start = time.perf_counter()
# print(f"found {findCombinations(n)} combinations in {time.perf_counter() - start} seconds")
