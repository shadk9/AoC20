import itertools

with open('input_day9') as file:
    input = file.readlines()


def day9(input, preambel):
    for i in range(len(input)):


        preambel_list = [int(n) for n in input[i:(preambel+i)]]
        target = int(input[preambel + i])
        combinations_list = []

        for num in itertools.combinations(preambel_list, 2):
            combinations_list.append(sum(num))

        if target not in combinations_list:
            return (target)

print(day9(input, 25))
