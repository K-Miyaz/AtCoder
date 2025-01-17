Sab, Sac, Sbc = map(str,input().split())

if Sab == "<":
    if Sac == "<":
        if Sbc == "<":
            print("B")
        else:
            print("C")
    else:
        print("A")
else:
    if Sac == "<":
        print("A")
    elif Sbc == "<":
        print("C")
    else:
        print("B")
