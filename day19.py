with open('input_day19') as file:
    input = file.readlines()


rules = True
rules_list = []
messages = []

for line in input:
    if rules:
        rules_list.append(line.rstrip())
        if line == '\n':
            rules_list.pop(-1)
            rules = False
    else:
        messages.append(line)

print(rules_list)

def day19(rules, messages):
    rule_dict = {}

    for rule in rules:
        rule = rule.split(' ')
        rule_num = rule[0].split(':')

        rule_dict[int(rule_num[0])] = rule[1::]
    pass

day19(rules_list, messages)
