# Day 20, part 1 of Advent of Code 2023

#data_file = open('./Data/2023/day20_test1.txt', 'r')
#data_file = open('./Data/2023/day20_test2.txt', 'r')

data_file = open('./Data/2023/day20.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

from abc import ABC, abstractmethod  

class Module(ABC) :
    
    @abstractmethod
    def receive(self,pulse) :
        pass
    
    @abstractmethod
    def __repr__(self) :
        pass

class FlipFlop(Module) :
    def __init__(self, name, destinations) :
        self.name = name
        self.state = 'low'
        self.destinations = destinations
    
    def receive(self, pulse) :
        #print(f"    {pulse[1]} -{pulse[0]}-> {self.name}")
        global pulses_to_send
        if pulse[0] == 'low' :
            self.state = 'high' if self.state == 'low' else 'low'
            if self.state == 'high' :
                pulses_to_send.append(['high',self.name,self.destinations])
            else :
                pulses_to_send.append(['low',self.name,self.destinations])
    
    def __repr__(self):
        return f"%{self.name} - {self.state} - -> {', '.join(self.destinations)}"

class Conjunction(Module) :
    def __init__(self,name,destinations) :
        self.name = name
        self.precedents = {}
        self.destinations = destinations
    
    def receive(self, pulse) :
        #print(f"    {pulse[1]} -{pulse[0]}-> {self.name}")
        self.precedents[pulse[1]] = pulse[0]
        all = True
        for input in self.precedents.keys() :
            if self.precedents[input] != 'high' :
                all = False
                break
        global pulses_to_send
        pulses_to_send.append(['low' if all else 'high',self.name,self.destinations])
    
    def init_inputs(self) :
        global modules
        for mod in modules :
            if mod != self.name and self.name in modules[mod].destinations :
                self.precedents[mod] = 'low'
    
    def __repr__(self):
        return f"&{self.name} - {self.precedents.items()} - -> {', '.join(self.destinations)}"
    
class Broadcast(Module) :
    def __init__(self,name,destinations) :
        self.name = name
        self.destinations = destinations
    
    def receive(self, pulse) :
        #print(f"    {pulse[1]} -{pulse[0]}-> {self.name}")
        global pulses_to_send
        pulses_to_send.append([pulse[0],self.name,self.destinations])
    
    def __repr__(self):
        return f"{self.name} -> {', '.join(self.destinations)}"

class NoneType(Module) :
    def __init__(self,name,destinations) :
        self.name = name
        self.destinations = destinations
    
    def receive(self, pulse) :
        #print(f"    {pulse[1]} -{pulse[0]}-> {self.name}")
        pass
    
    def __repr__(self):
        return f"{self.name} -> {', '.join(self.destinations)}"

modules = {}
for line in data_lines :
    name = line.split(' ')[0].strip()
    destinations = [dest.strip() for dest in line.split('>')[1].strip().split(',')]
    if name == 'broadcaster' :
        modules[name] = Broadcast(name,destinations)
    elif name[0] == '%' :
        modules[name[1:]] = FlipFlop(name[1:],destinations)
    elif name[0] == '&' :
        modules[name[1:]] = Conjunction(name[1:],destinations)
    else :
        modules[name] = NoneType(name,destinations)
modules['output'] = NoneType('output',[])
modules['rx'] = NoneType('rx',[])

for mod in modules :
    if modules[mod].__repr__()[0] == '&' :
        modules[mod].init_inputs()

count_low_pulses_to_rx = 0
pulses_to_send = []
def push_button() :
    global count_pulses_to_rx
    global pulses_to_send
    pulses_to_send = [['low','aptly',['broadcaster']]]
    while len(pulses_to_send) > 0 :
        pulse = pulses_to_send[0]
        for dest in pulse[2] :
            if dest == 'rx' and pulse[0] == 'low':
                count_low_pulses_to_rx += 1
            modules[dest].receive(pulse[:2])
        pulses_to_send.remove(pulse)

acc = 0
while count_low_pulses_to_rx != 1 :
    count_low_pulses_to_rx = 0
    push_button()
    acc += 1
    print(f'{acc} : {count_low_pulses_to_rx}')

print(f'\nResult = {acc}')
# Answer is 825167435
