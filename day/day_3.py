file = open('../input_files/day_3_input.txt', 'r')
lines = file.readlines()
lines_by_three = [line.strip() for line in lines][:3]

priorities = []

def getValue(letter: str) -> int:
    if letter.isupper():
        return ord(letter.lower()) - ord("a")+26+1
    
    return ord(letter) - ord("a")+1


for line in lines:
    line = line.strip()
    half_val = len(line) // 2
    m = []
    first_half = list(line[:half_val])
    second_half = list(line[half_val:])
    oops = ""

    for letter in first_half:
        if letter in second_half:
            val = getValue(letter)
            priorities.append(val)
            break



print("Sum of priorities: {}". format(sum(priorities)))

# PART 2
group_priorities = []
for i in range(0, len(lines)-1,3):
    elf_1 = lines[i]
    elf_2 = lines[i+1]
    elf_3 = lines[i+2]

    for letter in elf_1:
        if letter in elf_2 and letter in elf_3:
            val = getValue(letter)
            group_priorities.append(val)
            break

print("Sum of group priorities: {}". format(sum(group_priorities)))
