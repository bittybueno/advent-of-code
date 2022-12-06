file = open('../input_files/day_6_input.txt', 'r')
lines = file.readlines()



def part_1(line, sub_len):
    for idx in range(0, len(line)-3):
        if len(set(line[idx:idx+sub_len])) == sub_len:
            return idx+sub_len
        
part_1_sol = part_1(lines[0], 4)
part_2_sol = part_1(lines[0], 14)

print("Solution to part 1: {}".format(part_1_sol))
print("Solution to part 2: {}".format(part_2_sol))