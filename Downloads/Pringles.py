"""Pringles"""
def main(text1, text2, text3, value):
    """main"""
    ans = text2.count(')', 0, value)
    mid = " "*value+text2[value:]
    empty = mid.count(')')
    print(ans)
    if empty > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(text1)
    print(mid)
    print(text3)
main(input(), input(), input(), int(input()))
