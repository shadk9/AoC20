with open('input_day8') as file:
    input = file.readlines()

#Part 1
def day8(input_file):
    curr_instruction=0
    accumulator = 0
    instruction_order = []

    while True:
        if curr_instruction not in instruction_order and input_file[curr_instruction] != '\n':
            instruction_order.append(curr_instruction)

            line = input_file[curr_instruction].split()
            if line[0] == 'nop':
                curr_instruction += 1
            elif line[0] == 'acc':
                accumulator += int(line[1])
                curr_instruction += 1
            else:
                curr_instruction += int(line[1])
        else:
            break
    print(accumulator)


#uses part 1, bc why not
#Part 2
def day8_2():
    for i in range(len(input)):
        line = input[i].split()
        if line[0] == 'nop':
            new_input = input.copy()
            new_input[i] = str('jmp ' + line[1])
            if (day8_2_helper(new_input)):
                return day8(new_input)
        elif line[0] == 'jmp':
            new_input = input.copy()
            new_input[i] = str('nop ' + line[1])
            if (day8_2_helper(new_input)):
                return day8(new_input)
        else:
            pass


def day8_2_helper(input_modified):
    curr_instruction=0
    accumulator = 0
    instruction_order = []

    while True:
        if curr_instruction not in instruction_order:

            if input_modified[curr_instruction] == '\n':
                return True

            instruction_order.append(curr_instruction)
            line = input_modified[curr_instruction].split()
            if line[0] == 'nop':
                curr_instruction += 1
            elif line[0] == 'acc':
                accumulator += int(line[1])
                curr_instruction += 1
            else:
                curr_instruction += int(line[1])
        else:
            break
    return False


day8_2()
