# https://www.reddit.com/r/Minecraft/comments/etrfs0/how_exactly_do_comparators_calculate_redstone/

class Slot:
    def __init__(self, items_num=0, stack_size=64):
        self.items = items_num
        self.stack_size = stack_size
        self.percentage = self.items / self.stack_size


class Inventory:
    def __init__(self, num_slots, slots):
        self.num_slots = num_slots
        self.sum = 0
        self.slots = slots

        for slot in self.slots:
            self.sum += slot.percentage

        self.percentage = self.sum / self.num_slots
        self.signal = int(self.percentage * 15)



slots_num = int(input("Enter num of slots: "))
slots = []

for slot_ in range(slots_num):
    num = input(f"[{slot_}] Enter num of max size of the stack (default 64): ")
    fullness = input(f"[{slot_}] Enter number of items in the slot(default 0): ")
    slots.append(Slot(int(fullness if fullness != "" else 0), int(num if num != "" else 64)))

inv = Inventory(slots_num, slots)

print(f"Signal strength: {inv.signal}")

