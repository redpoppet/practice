def translateNum(num):
    # num = int(str(num)[::-1])
    a = b = 1
    y = num % 10
    while num != 0:
        num //= 10
        x = num % 10
        a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
        y = x
    return a

if __name__ == "__main__":
    print(translateNum(11258))
    print(translateNum(85211))
    