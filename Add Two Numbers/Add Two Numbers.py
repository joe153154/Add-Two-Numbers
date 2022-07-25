def add_two_numbers(a, b):
    c = []
    if len(a)>len(b):
        l = len(a)
    else:
        l = len(b)

    for i in range(l):
        if len(a) == len(b):
            x = a[i] + b[i]
            c.append(x)
        else:
            bl = abs(len(a) - len(b))
            if len(a) > len(b):
                if i < bl:
                    x = a[i]
                    c.append(x)
                else:
                    x = a[i] + b[i-bl]
                    c.append(x)
            else:
                if i < bl:
                    x = b[i]
                    c.append(x)
                else:
                    x = a[i-bl] + b[i]
                    c.append(x)
    c = c[::-1]
    for i in range(len(c)):
        if c[i] >= 10:
            c[i] = c[i]-10
            c[i+1] = c[i+1]+1
    print(c)

def main():
    a = [1, 2, 3, 4]
    b = [4, 5, 6]
    add_two_numbers(a, b)

if __name__ == "__main__":
    main()