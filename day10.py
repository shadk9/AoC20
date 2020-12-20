with open('input_day10') as file:
    input = file.readlines()


def day10(input):

    input = [int(n) for n in input]
    input = sorted(input)

    prev_jolt = 0
    dist_dict = { 0 : 0, 1: 0, 2: 0, 3: 0}

    for i in input:
        dist_dict[(i-prev_jolt)] += 1
        prev_jolt = i
    dist_dict[3] += 1

    print(dist_dict)
    print(dist_dict[1] * dist_dict[3])

day10(input)



