# Day 19, part 2 of Advent of Code 2023

data_file = open('./Data/day19_test1.txt', 'r')

#data_file = open('./Data/day19.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

class Rule :
    def __init__(self, rule) :
        if len(rule.split(':')) > 1 :
            self.attribute = rule[0]
            self.test_sign = rule[1]
            self.compare = int(rule.split(':')[0].split(self.test_sign)[1])
            self.destination = rule.split(':')[1]
        else :
            self.attribute = True
            self.test_sign = None
            self.compare = None
            self.destination = rule
    
    def __repr__(self) :
        if self.test_sign == None :
            return f'{self.attribute} => {self.destination}'
        return f'if {self.attribute} {self.test_sign} {self.compare} => {self.destination}'
    
    def get_str(self) :
        if self.test_sign == None :
            return self.destination
        return f'{self.attribute}{self.test_sign}{self.compare}:{self.destination}'
    
    def test(self, rating) :
        if self.test_sign == None :
            return self.attribute
        if self.test_sign == '>' :
            if self.attribute == 'x' :
                return rating.x > self.compare
            if self.attribute == 'm' :
                return rating.m > self.compare
            if self.attribute == 'a' :
                return rating.a > self.compare
            if self.attribute == 's' :
                return rating.s > self.compare
        if self.test_sign == '<' :
            if self.attribute == 'x' :
                return rating.x < self.compare
            if self.attribute == 'm' :
                return rating.m < self.compare
            if self.attribute == 'a' :
                return rating.a < self.compare
            if self.attribute == 's' :
                return rating.s < self.compare
        return False

    def get_inv(self) :
        if self.test_sign == None :
            return not self.attribute
        if self.test_sign == '<' :
            new_compare = self.compare - 1
            new_test_sign = '>'
        if self.test_sign == '>' :
            new_compare = self.compare + 1
            new_test_sign = '<'
        strr = f'{self.attribute}{new_test_sign}{new_compare}:{self.destination}'
        return Rule(strr)
        

class Workflow :
    def __init__(self, line) :
        self.name = line.split('{')[0]
        self.rules = []
        for rule in line.split('{')[1].split('}')[0].split(',') :
            self.rules.append(Rule(rule))
    
    def __repr__(self) :
        return f'{self.name} : {self.rules}'
    
    def get_destinations(self) :
        return [rule.destination for rule in self.rules]
    
    def find(self,dest) :
        destinations = self.get_destinations()
        for i in range(len(destinations)) :
            if destinations[i] == dest :
                return i
        return -1

workflows = {}
l = 0
while data_lines[l] != '' :
    wk = Workflow(data_lines[l])
    workflows[wk.name] = wk
    l += 1

workflows_with_A = []
for wk in workflows :
    if 'A' in workflows[wk].get_destinations() :
        workflows_with_A.append(workflows[wk])

def compatible(rules,add_rules) :
    comp = True
    for rule in rules :
        if rule.test_sign != None :
            if rule.attribute == 'x' :
                for add_rule in add_rules :
                    if add_rule.attribute == 'x' :
                        if rule.test_sign == '<' and add_rule.test_sign == '>' :
                            comp = comp and rule.compare >= add_rule.compare
                        elif rule.test_sign == '>' and add_rule.test_sign == '<' :
                            comp = comp and rule.compare <= add_rule.compare
                        #print(rule,add_rule,comp)
            elif rule.attribute == 'm' :
                for add_rule in add_rules :
                    if add_rule.attribute == 'm' :
                        if rule.test_sign == '<' and add_rule.test_sign == '>' :
                            comp = comp and rule.compare >= add_rule.compare
                        elif rule.test_sign == '>' and add_rule.test_sign == '<' :
                            comp = comp and rule.compare <= add_rule.compare
                        #print(rule,add_rule,comp)
            elif rule.attribute == 'a' :
                for add_rule in add_rules :
                    if add_rule.attribute == 'a' :
                        if rule.test_sign == '<' and add_rule.test_sign == '>' :
                            comp = comp and rule.compare >= add_rule.compare
                        elif rule.test_sign == '>' and add_rule.test_sign == '<' :
                            comp = comp and rule.compare <= add_rule.compare
                        #print(rule,add_rule,comp)
            elif rule.attribute == 's' :
                for add_rule in add_rules :
                    if add_rule.attribute == 's' :
                        if rule.test_sign == '<' and add_rule.test_sign == '>' :
                            comp = comp and rule.compare >= add_rule.compare
                        elif rule.test_sign == '>' and add_rule.test_sign == '<' :
                            comp = comp and rule.compare <= add_rule.compare
                        #print(rule,add_rule,comp)
    #print(comp)
    return comp

def new_rules(rules,add_rules) :
    add_rules_copy = add_rules.copy()
    new_rules = []
    for rule in rules :
        if rule.test_sign != None :
            if rule.attribute == 'x' :
                find_other_x = False
                for add_rule in add_rules_copy :
                    if add_rule.attribute == 'x' :
                        find_other_x = True
                        if rule.test_sign == add_rule.test_sign :
                            if rule.test_sign == '<' :
                                if rule.compare <= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                            else :
                                if rule.compare >= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                        else :
                            if rule not in new_rules :
                                new_rules.append(rule)
                            if add_rule not in new_rules :
                                new_rules.append(add_rule)
                        add_rules_copy.remove(add_rule)
                if not find_other_x :
                    new_rules.append(rule)
            elif rule.attribute == 'm' :
                find_other_m = False
                for add_rule in add_rules_copy :
                    if add_rule.attribute == 'm' :
                        find_other_m = True
                        if rule.test_sign == add_rule.test_sign :
                            if rule.test_sign == '<' :
                                if rule.compare <= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                            else :
                                if rule.compare >= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                        else :
                            if rule not in new_rules :
                                new_rules.append(rule)
                            if add_rule not in new_rules :
                                new_rules.append(add_rule)
                        add_rules_copy.remove(add_rule)
                if not find_other_m :
                    new_rules.append(rule)
            elif rule.attribute == 'a' :
                find_other_a = False
                for add_rule in add_rules_copy :
                    if add_rule.attribute == 'a' :
                        find_other_a = True
                        if rule.test_sign == add_rule.test_sign :
                            if rule.test_sign == '<' :
                                if rule.compare <= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                            else :
                                if rule.compare >= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                        else :
                            if rule not in new_rules :
                                new_rules.append(rule)
                            if add_rule not in new_rules :
                                new_rules.append(add_rule)
                        add_rules_copy.remove(add_rule)
                if not find_other_a :
                    new_rules.append(rule)
            elif rule.attribute == 's' :
                find_other_s = False
                for add_rule in add_rules_copy :
                    if add_rule.attribute == 's' :
                        find_other_s = True
                        if rule.test_sign == add_rule.test_sign :
                            if rule.test_sign == '<' :
                                if rule.compare <= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                            else :
                                if rule.compare >= add_rule.compare :
                                    new_rules.append(rule)
                                else :
                                    new_rules.append(add_rule)
                        else :
                            if rule not in new_rules :
                                new_rules.append(rule)
                            if add_rule not in new_rules :
                                new_rules.append(add_rule)
                        add_rules_copy.remove(add_rule)
                if not find_other_s :
                    new_rules.append(rule)
    for rule in add_rules_copy :
        if rule not in new_rules :
            new_rules.append(rule)
    return new_rules

paths = []
for wk in workflows_with_A :
    index = wk.find('A')
    if index >= 0 :
        rules_to_follow = [rule.get_inv() for rule in wk.rules[:index]]
        rules_to_follow.append(wk.rules[index])
        paths.append([wk.name,rules_to_follow])
    #print(paths[-1])

correct_ratings = []
while len(paths) > 0 :
    path = paths[0]
    for wk in workflows :
        index = workflows[wk].find(path[0])
        if index >= 0 :
            rules_to_follow = [rule.get_inv() for rule in workflows[wk].rules[:index]]
            rules_to_follow.append(workflows[wk].rules[index])
            if compatible(path[1],rules_to_follow) :
                new_path = [workflows[wk].name,new_rules(path[1],rules_to_follow)]
                #print(new_path)
                if new_path[0] != 'in' :
                    paths.append(new_path)
                else : 
                    correct_ratings.append(new_path)
            paths.remove(path)
        
def nb_possibilities(correct_rules) :
    nb = 1
    for attribute in ['x','m','a','s'] :
        if attribute not in [rule.attribute for rule in correct_rules] :
            nb *= 4000
        else :
            rules = []
            for rule in correct_rules :
                if rule.attribute == attribute :
                    rules.append(rule)
            if len(rules) == 1 :
                if rules[0].test_sign == '<':
                        nb *= rules[0].compare -1
                elif rules[0].test_sign == '>':
                    nb *= 4000 - rules[0].compare
            else :
                if rules[0].test_sign == '<' :
                    nb *= rules[0].compare - rules[1].compare - 1
                elif rules[0].test_sign == '>' :
                    nb *= rules[1].compare - rules[0].compare - 1
    print(correct_rules,nb)
    return nb

print('\nResult = ',sum([nb_possibilities(correct_rating[1]) for correct_rating in correct_ratings]))
# Answer is 167409079868000 for the test
