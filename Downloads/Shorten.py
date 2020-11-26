"""Shorten"""
def main(result=""):
    """main"""
    check = start = end = 0
    while True:
        num = int(input())
        if check == 0:
            start = end = num
        if num == end+1:
            end = num
        elif num != end-1 and check != 0:
            if start != end:
                result += str(start)+'-'+str(end)
            else:
                result += str(end)
            if num != -1:
                result += ", "
            start = end = num
        if num == -1:
            break
        check += 1
    print(result)
main()
