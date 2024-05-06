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




inv = Inventory(9, [
    Slot(64),
    Slot(64),
    Slot(64),

    Slot(),
    Slot(),
    Slot(),

    Slot(),
    Slot(),
    Slot()
])


print(inv.percentage)
print(inv.signal)

