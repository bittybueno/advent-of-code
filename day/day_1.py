file1 = open('../input_files/day_1_input.txt', 'r')
lines = file1.readlines()
  
curr_elf_cal_count = 0
max_elf_id = 0
max_elf_count = 0
all_calories = []


for line in lines:
    if line == '\n':
        if curr_elf_cal_count > max_elf_count:
            max_elf_count = curr_elf_cal_count
        
        all_calories.append(curr_elf_cal_count)
        curr_elf_cal_count = 0
        
    else: 
        curr_elf_cal_count += int(line.strip())

all_calories.sort()


print("Most calories: {}".format( max_elf_count))
print("Top three calories: {}".format(sum(all_calories[-3:])))
