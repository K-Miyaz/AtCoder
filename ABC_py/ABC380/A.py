N = input()
ans = False
if N.count("1") == 1:
    if N.count("2") == 2:
        if N.count("3") == 3:
            ans = True
if ans:
    print("Yes")
else:
    print("No")