number = {}
generates = {1: number}
path = {1: {8: 8, 5: 0, 3: 0, 'pre': 0}}
key = 1


def findKey(num):
    global generates
    for key, value in generates.items():
        if value == num:
            return key


def already(num, pre):
    global generates
    global key
    global path
    for key, value in generates.items():
        if value == num:
            return False
    key += 1
    generates[key] = num
    numberWithPre = {key: value for key, value in num.items()}
    numberWithPre["pre"] = pre
    path[key] = numberWithPre
    return True


def pathPrint(pre):
    if pre == 1:
        return
    pre = path[pre]['pre']
    pathPrint(pre)
    print(generates[pre])


if __name__ == '__main__':
    queue = []
    flag = False
    print("Enter initial state")
    number[8] = int(input("Enter quantity for 8 : "))
    number[5] = int(input("Enter quantity for 5 : "))
    number[3] = int(input("Enter quantity for 3 : "))
    queue.append(number)
    while len(queue) != 0:
        number = queue.pop(0)
        index = findKey(number)
        if number[8] == 4 or number[5] == 4:
            flag = True
            print("Found ", number)
            pathPrint(index)
            print(generates[index])
            break
        newNum = {key: value for key, value in number.items()}
        if number[8] - (5 - number[5]) > 0:
            newNum[8] = number[8] - (5 - number[5])
            newNum[5] = 5
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[5] = number[5] + number[8]
            newNum[8] = 0
            if already(newNum, index):
                queue.append(newNum)
        newNum = {key: value for key, value in number.items()}
        if number[8] - (3 - number[3]) > 0:
            newNum[8] = number[8] - (3 - number[3])
            newNum[3] = 3
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[3] = number[3] + number[8]
            newNum[8] = 0
            if already(newNum, index):
                queue.append(newNum)
        newNum = {key: value for key, value in number.items()}
        if number[5] - (8 - number[8]) > 0:
            newNum[5] = number[5] - (8 - number[8])
            newNum[8] = 8
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[8] = number[8] + number[5]
            newNum[5] = 0
            if already(newNum, index):
                queue.append(newNum)
        newNum = {key: value for key, value in number.items()}
        if number[5] - (3 - number[3]) > 0:
            newNum[5] = number[5] - (3 - number[3])
            newNum[3] = 3
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[3] = number[3] + number[5]
            newNum[5] = 0
            if already(newNum, index):
                queue.append(newNum)
        newNum = {key: value for key, value in number.items()}
        if number[3] - (8 - number[8]) > 0:
            newNum[3] = number[3] - (8 - number[8])
            newNum[8] = 8
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[8] = number[8] + number[3]
            newNum[3] = 0
            if already(newNum, index):
                queue.append(newNum)
        newNum = {key: value for key, value in number.items()}
        if number[3] - (5 - number[5]) > 0:
            newNum[3] = number[3] - (5 - number[5])
            newNum[5] = 5
            if already(newNum, index):
                queue.append(newNum)
        else:
            newNum[5] = number[5] + number[3]
            newNum[3] = 0
            if already(newNum, index):
                queue.append(newNum)
    if not flag:
        print("Solution doesn't exist.")
