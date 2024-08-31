# ComparatorCalc
calculator of strenght of the signal from comparator based on "fullness" of storage block

## How does it work?

1. First get the fullness percentage of each slot:

`num_of_items_in_slot / stack_size_of_slot`

2. Then sum fullness percentages for each slot in the whole inventory and divide that sum by number of slots in inventory.

3. Just multiply the result with constant `15` (maximum redstone signal strength) and floor it
