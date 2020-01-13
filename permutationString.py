def printSub(str, curr="", index=0, s = set()):


    if index == len(str):
        if curr != "":
            print(curr, [...])
            s.add(curr)
            print(s, [...])

        return

    else:
        printSub(str, curr, index+1)
        printSub(str, curr+str[index], index+1)



printSub("ABC")
