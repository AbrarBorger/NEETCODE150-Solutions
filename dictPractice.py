x = {"1": 45, "2": 76}
x["3"] = [2, 1, 2, 3, 5]
print(list(x.keys()))
print("3" in x)

del x["3"]
print(list(x.keys()))

for key, value in x.items():
    print(key, value)