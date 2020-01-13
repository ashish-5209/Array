def main():
    testcase = int(input())
    while(testcase>0):
        sizeOfArray = int(input())

        arr = [int(x) for x in input().strip().split()]

        element = int(input())

        arr.append(element)

        for i in arr:
            print(i, end=" ")
        print()

        testcase -= 1


if __name__== "__main__":
    main()

