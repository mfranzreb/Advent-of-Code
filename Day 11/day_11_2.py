class Monkey:
    def __init__(self, block):
        self.items = [int(nums) for nums in block[1].split(": ")[1].split(", ")]
        self.operation = block[2].split("old ")[1]
        self.test_op = int(block[3].split("by ")[1])
        self.yes = int(block[4].split("monkey")[1])
        self.no = int(block[5].split("monkey")[1])
        self.activity = 0

    def inspect(self, item, item_index):
        if any(char.isdigit() for char in self.operation):
            operator = int(self.operation.split(" ")[1])

        else:
            operator = False

        if "*" in self.operation:
            if not operator:
                item = item**2
            else:
                item *= operator

        elif "+" in self.operation:
            item += operator

        self.items[item_index] = item
        self.activity += 1
        return item

    def test(self, item, item_index, test_divisors_mult):
        if item % self.test_op == 0:
            if item % test_divisors_mult == 0:
                 item = 96577
                 print("YAAASSSS")
                 self.items[item_index] = item
            return self.yes
        else:
            return self.no

    def receiveItem(self, item):
        self.items.append(item)

    def removeItems(self):
        self.items.clear()

        

    
with open("C:/Users/Marco/Desktop/Advent of Code/Day 11/test.txt") as f:
    content = [paraf.split("\n") for paraf in f.read().split("Monkey")]
    content = content[1:]
    monkeys = []
    test_divisors = []
    test_divisors_mult = 1
    for block in content:
        monk = Monkey(block)
        monkeys.append(monk)
        test_divisors.append(monk.test_op)
        test_divisors_mult *= monk.test_op


    for i in range(1000):
        for j, monkey in enumerate(monkeys):

            #print("MOnkey: "+ str(j))

            for x, item in enumerate(monkey.items):
                current_item = monkey.inspect(item, x)
                pass_to = monkey.test(current_item, x, test_divisors_mult)
                monkeys[pass_to].receiveItem(current_item)
                #if pass_to == monkey.yes:
                    #print(current_item, i, j)

                #print(item, current_item, pass_to)

            monkey.removeItems()

    max_act_1 = 0
    max_act_2 = 0
    for m in monkeys:
        current_activity = m.activity

        if current_activity > max_act_1:
            past_activity = max_act_1
            max_act_1 = current_activity
            if past_activity > max_act_2:
                max_act_2 = past_activity
            
        
        elif current_activity > max_act_2:
            max_act_2 = current_activity

    print(max_act_1, max_act_2, max_act_2*max_act_1)












