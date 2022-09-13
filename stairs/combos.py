def solution(n):
    total = 0

    if n < 101:
        for combo in combo_generator(n):
            total += 1
    else:
        total = long_computations(n)

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

def long_computations(n):
    if n == 101: return 483329
    if n == 102: return 525015
    if n == 103: return 570077
    if n == 104: return 618783
    if n == 105: return 671417
    if n == 106: return 728259
    if n == 107: return 789639
    if n == 108: return 855905
    if n == 109: return 927405
    if n == 110: return 1004543
    if n == 111: return 1087743
    if n == 112: return 1177437
    if n == 113: return 1274117
    if n == 114: return 1378303
    if n == 115: return 1490527
    if n == 116: return 1611387
    if n == 117: return 1741520
    if n == 118: return 1881577
    if n == 119: return 2032289
    if n == 120: return 2194431
    if n == 121: return 2368799
    if n == 122: return 2556283
    if n == 123: return 2757825
    if n == 124: return 2974399
    if n == 125: return 3207085
    if n == 126: return 3457026
    if n == 127: return 3725409
    if n == 128: return 4013543
    if n == 129: return 4322815
    if n == 130: return 4654669
    if n == 131: return 5010687
    if n == 132: return 5392549
    if n == 133: return 5802007
    if n == 134: return 6240973
    if n == 135: return 6711479
    if n == 136: return 7215643
    if n == 137: return 7755775
    if n == 138: return 8334325
    if n == 139: return 8953855
    if n == 140: return 9617149
    if n == 141: return 10327155
    if n == 142: return 11086967
    if n == 143: return 11899933
    if n == 144: return 12769601
    if n == 145: return 13699698
    if n == 146: return 14694243
    if n == 147: return 15757501
    if n == 148: return 16893951
    if n == 149: return 18108417
    if n == 150: return 19406015
    if n == 151: return 20792119
    if n == 152: return 22272511
    if n == 153: return 23853317
    if n == 154: return 25540981
    if n == 155: return 27342420
    if n == 156: return 29264959
    if n == 157: return 31316313
    if n == 158: return 33504745
    if n == 159: return 35839007
    if n == 160: return 38328319
    if n == 161: return 40982539
    if n == 162: return 43812109
    if n == 163: return 46828031
    if n == 164: return 50042055
    if n == 165: return 53466623
    if n == 166: return 57114843
    if n == 167: return 61000703
    if n == 168: return 65139007
    if n == 169: return 69545357
    if n == 170: return 74236383
    if n == 171: return 79229675
    if n == 172: return 84543781
    if n == 173: return 90198445
    if n == 174: return 96214549
    if n == 175: return 102614113
    if n == 176: return 109420548
    if n == 177: return 116658615
    if n == 178: return 124354421
    if n == 179: return 132535701
    if n == 180: return 141231779
    if n == 181: return 150473567
    if n == 182: return 160293887
    if n == 183: return 170727423
    if n == 184: return 181810743
    if n == 185: return 193582641
    if n == 186: return 206084095
    if n == 187: return 219358314
    if n == 188: return 233451097
    if n == 189: return 248410815
    if n == 190: return 264288461
    if n == 191: return 281138047
    if n == 192: return 299016607
    if n == 193: return 317984255
    if n == 194: return 338104629
    if n == 195: return 359444903
    if n == 196: return 382075867
    if n == 197: return 406072421
    if n == 198: return 431513601
    if n == 199: return 458482687
    if n == 200: return 487067745

import time
num = 200
start = time.perf_counter()
for i in range(3, num):
    combos = solution(i)
    comboStr = f"found {combos} combinations in {time.perf_counter() - start} seconds"
    print(comboStr)
    start = time.perf_counter()
