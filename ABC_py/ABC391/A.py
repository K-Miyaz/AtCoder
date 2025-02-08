D = input()
input_D = ["N", "E", "W", "S", "NE", "NW", "SE", "SW"]
ans_D = ["S", "W", "E", "N", "SW", "SE", "NW", "NE"]

for i in range(len(input_D)):
    if D == input_D[i]:
        print(ans_D[i])