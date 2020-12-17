with open('input_day8') as file:
    input = file.readlines()


def day8():

    curr_instruction = 0
    accumulator = 0
    instruction_order = []

    while curr_instruction not in instruction_order:
        instruction_order.append(curr_instruction)

        line = input[curr_instruction].split()
        if line[0] == 'nop':
            curr_instruction += 1
        elif line[0] == 'acc':
            accumulator += int(line[1])
            curr_instruction += 1
        else:
            curr_instruction += int(line[1])


    print(accumulator)

day8()
