file = open('../input_files/day_5_input.txt', 'r')
lines = file.readlines()

def parse_line(line, longest_line, m):
    counter = 1
    for i in range(0, longest_line, 4):
        letter = line[i:i+3].replace("[", "").replace("]", "")
        if letter.isalpha():
            prev = m[counter]
            prev.append(letter)
            m[counter] = prev
        counter+=1

    return m

def parse(lines, longest_line, num_of_stacks):
    m = {}
    for v in range(1,num_of_stacks+1):
        m[v] = []

    for i, line in enumerate(reversed(lines)):
        m = parse_line(line, longest_line, m)
        
    return m

for i,line in enumerate(lines):
    if line[1] == "1":
        num_of_stacks = int(list(line.strip())[-1])
        longest_len = (num_of_stacks * 3) + (num_of_stacks-1)
        m = parse(lines[0:i], longest_len, num_of_stacks)
        break

def part_1(m):
    for line in lines[i+2:]:
        nums = [int(s) for s in line.split() if s.isdigit()]

        quantity = nums[0]
        from_idx = nums[1]
        to_idx = nums[2]


        while quantity > 0:
            m[to_idx].append(m[from_idx].pop())
            quantity-=1

    fin = ""
    for arr in m.values():
        fin = fin + arr.pop()

    print("Answer: {}".format(fin))

part_1(m)
