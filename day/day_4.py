file = open('../input_files/day_4_input.txt', 'r')
lines = file.readlines()

count = 0
some_overlap_count = 0

def does_fall_totally_within(first, second):
    if first[0] <= second[0] and first[1] >= second[1]:
        return True

    return False

def does_fall_witin(first, second):
    # (6,6)
    # (4, 6)
    if first[1] >= second[0] and first[0] <= second[1]:
        return True

    return False

for line in lines:
    line = line.strip().split(",")
    elf_1 = (int(line[0].split('-')[0]), int(line[0].split('-')[1]))
    elf_2 = (int(line[1].split('-')[0]), int(line[1].split('-')[1]))

    if does_fall_totally_within(elf_1, elf_2) or does_fall_totally_within(elf_2, elf_1):
        count+=1
    
    if does_fall_witin(elf_1, elf_2):
        some_overlap_count+=1


print("Count of total overlaps: {}".format(count))


# PART 2
print("Count of total overlaps: {}".format(some_overlap_count))
