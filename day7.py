with open('input_day7') as file:
    input = file.readlines()


# Part one
def day_seven(input_list, target_bag):
    # target string should not contain space
    bag_dict = {}
    # list that acts like a set. need order so using list for now
    contain_target_set = set()

    num_of_bags = 0

    for line in input_list:
        line = line.split()

        curr_bag = line[0] + line[1]

        bag_dict[curr_bag] = []

        for i in range(5, len(line), 4):
            contained_bag = line[i] + line[i + 1]

            if contained_bag == 'otherbags.':
                bag_dict.pop(curr_bag)

            else:
                bag_dict[curr_bag].append(contained_bag)

                # membership test ensures that the list only contains uniqe elements
                if contained_bag == target_bag and contained_bag not in contain_target_set:
                    contain_target_set.add(curr_bag)

    eventually_contain_list = set()

    while contain_target_set:
        curr_b = contain_target_set.pop()

        for key, item_list in bag_dict.items():
            for item in item_list:
                if item == curr_b:
                    contain_target_set.add(key)

        eventually_contain_list.add(curr_b)

    print(len(eventually_contain_list))


# Part 2
def day_seven_part_two(target):
    # target string should not contain space
    total = 0
    n_bags = 0

    for line in input:
        line = line.split()
        curr_bag = line[0] + line[1]

        if (curr_bag) == target:
            for i in range(4, len(line), 4):

                if line[i] == 'no':
                    return 0
                else:
                    new_target = line[i + 1] + line[i + 2]
                    total += int(line[i])
                    total += (int(line[i]) * day_seven_part_two(new_target))
    return total


print(day_seven_part_two('shinygold'))

# day_seven(input, 'shinygold')
