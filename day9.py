import itertools

with open('input_day9') as file:
    input = file.readlines()


def day9(input, preambel):
    for i in range(len(input)):

        preambel_list = [int(n) for n in input[i:(preambel + i)]]
        target = int(input[preambel + i])
        combinations_list = []

        for num in itertools.combinations(preambel_list, 2):
            combinations_list.append(sum(num))

        if target not in combinations_list:
            return target


#print(day9(input, 25))


def day9_2(input, preambel_target):
    repeats = 3
    preambel = 3
    target = day9(input, preambel_target)

    while True:
        for i in range(len(input)):
            preambel_list = [int(n) for n in input[i:(preambel + i)]]
            combinations_list = []

            for num in itertools.combinations(preambel_list, repeats):
                combinations_list.append(sum(num))

            if target in combinations_list:
                print(min(preambel_list) +  max(preambel_list))
                return

        preambel += 1
        repeats += 1

day9_2(input, 25)
