file = open('../input_files/day_7_input.txt', 'r')
lines = file.readlines()

m = {"/": 0}
pwd = ""

for line in lines:
    line = line.strip()

    if line == "$ ls":
        continue
    elif line == "$ cd /":
        pwd = "/"
    elif line == "$ cd ..":
        pwd = "/".join(pwd.split("/")[:-2]) + "/"
    elif line.startswith("$ cd"):
        pwd += line.split(" ")[-1] + "/"
    elif line.startswith("dir "):
        m[pwd + line.split(" ")[-1] + "/"] = 0
    else:
        m[pwd] += int(line.split(" ")[0])


res = {}
for k in m:
    arr = []
    for l in m:
        if l.startswith(k):
            arr.append(m[l])
    res[k] = sum(arr)


print(sum([res[d] for d in res if res[d] <= 100000]))


space = 70000000 - res["/"]
needed = 30000000 - space

print(min([res[d] for d in res if res[d] >= needed]))

