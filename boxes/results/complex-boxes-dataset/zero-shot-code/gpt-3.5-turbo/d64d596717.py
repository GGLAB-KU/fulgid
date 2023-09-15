box = {
    0: ['dice', 'tree'],
    1: ['fridge', 'speaker', 'laptop', 'wire', 'pants'],
    2: ['rain', 'razor'],
    3: ['branch'],
    4: [],
    5: ['island'],
    6: ['wallet', 'shoe', 'dress', 'elephant'],
    7: ['note', 'chair', 'bag', 'boot'],
    8: [],
    9: ['starfish'],
    10: ['rocket', 'mountain'],
    11: [],
    12: ['thread', 'bicycle', 'pen', 'grinder'],
    13: ['magnet', 'lion', 'jacket', 'motorcycle'],
    14: []
}

def swap_items(box, box_index_1, item_index_1, box_index_2, item_index_2):
    item_1 = box[box_index_1].pop(item_index_1)
    item_2 = box[box_index_2].pop(item_index_2)
    box[box_index_1].append(item_2)
    box[box_index_2].append(item_1)

def move_item(box, source_box_index, item_index, destination_box_index):
    item = box[source_box_index].pop(item_index)
    box[destination_box_index].append(item)

def remove_item(box, box_index, item_index):
    box[box_index].pop(item_index)

def replace_item(box, box_index, item_index, new_item):
    box[box_index][item_index] = new_item

# Swap the starfish in Box 9 with the branch in Box 3
swap_items(box, 9, 0, 3, 0)

# Move the wire from Box 1 to Box 11
move_item(box, 1, 3, 11)

# Remove the speaker and the pants and the laptop from Box 1
remove_item(box, 1, 1)
remove_item(box, 1, 1)
remove_item(box, 1, 1)

# Replace the chair with the thread in Box 7
replace_item(box, 7, 1, 'thread')

# Replace the razor and the rain with the pot and the lock in Box 2
replace_item(box, 2, 1, 'pot')
replace_item(box, 2, 0, 'lock')

# Move the note and the bag from Box 7 to Box 10
move_item(box, 7, 0, 10)
move_item(box, 7, 0, 10)

# Replace the fridge with the lipstick in Box 1
replace_item(box, 1, 0, 'lipstick')

# Replace the dice with the thread in Box 0
replace_item(box, 0, 0, 'thread')

# Put the lipstick into Box 10
box[10].append('lipstick')

# Put the chair and the cat and the shelf into Box 10
box[10].extend(['chair', 'cat', 'shelf'])

# Remove the thread and the grinder and the bicycle from Box 12
remove_item(box, 12, 2)
remove_item(box, 12, 1)
remove_item(box, 12, 0)

# Put the towel and the train and the table into Box 13
box[13].extend(['towel', 'train', 'table'])

# Move the boot from Box 7 to Box 11
move_item(box, 7, 3, 11)

# Remove the starfish from Box 3
remove_item(box, 3, 0)

# Move the lipstick from Box 1 to Box 13
move_item(box, 1, 0, 13)

# Swap the pen in Box 12 with the chair in Box 10
swap_items(box, 12, 2, 10, 0)

# Put the towel and the bracelet into Box 13
box[13].extend(['towel', 'bracelet'])

# Remove the lock from Box 2
remove_item(box, 2, 0)

# Remove the thread from Box 7
remove_item(box, 7, 1)

# Remove the thread from Box 0
remove_item(box, 0, 0)

# Swap the branch in Box 9 with the island in Box 5
swap_items(box, 9, 0, 5, 0)

# Move the shoe from Box 6 to Box 3
move_item(box, 6, 1, 3)

# Print the contents of each box
for box_index, items in box.items():
    print(f"Box {box_index}: {items}")