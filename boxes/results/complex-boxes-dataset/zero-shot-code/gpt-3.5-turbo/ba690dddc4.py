box = {
    0: ['bus', 'submarine', 'piano', 'apple'],
    1: ['mirror', 'planet', 'necklace', 'jungle'],
    2: ['note', 'toothbrush', 'crown', 'comb'],
    3: ['microscope'],
    4: ['island', 'tree', 'game'],
    5: ['dice', 'bicycle'],
    6: ['pot', 'starfish', 'scissors', 'whistle'],
    7: ['octopus', 'makeup', 'coat'],
    8: [],
    9: ['pan', 'grinder', 'keyboard', 'toothpaste', 'boat'],
    10: ['thread', 'paint'],
    11: ['lion', 'candle'],
    12: ['tape', 'sock', 'star']
}

def swap_items(box, box_index_1, item_index_1, box_index_2, item_index_2):
    item_1 = box[box_index_1][item_index_1]
    item_2 = box[box_index_2][item_index_2]
    box[box_index_1][item_index_1] = item_2
    box[box_index_2][item_index_2] = item_1

def replace_items(box, box_index, item_index, new_items):
    box[box_index][item_index] = new_items

def move_item(box, source_box_index, source_item_index, destination_box_index):
    item = box[source_box_index].pop(source_item_index)
    box[destination_box_index].append(item)

def empty_box(box, box_index):
    box[box_index] = []

# Swap toothbrush in Box 2 with bicycle in Box 5
swap_items(box, 2, 1, 5, 1)

# Move microscope from Box 3 to Box 5
move_item(box, 3, 0, 5)

# Replace whistle and starfish with doll and shoes in Box 6
replace_items(box, 6, 2, ['doll', 'shoes'])

# Put glasses into Box 0
box[0].append('glasses')

# Empty Box 11
empty_box(box, 11)

# Swap piano in Box 0 with planet in Box 1
swap_items(box, 0, 2, 1, 1)

# Swap grinder in Box 9 with piano in Box 1
swap_items(box, 9, 1, 1, 2)

# Swap pot in Box 6 with toothbrush in Box 5
swap_items(box, 6, 0, 5, 1)

# Swap pot in Box 5 with paint in Box 10
swap_items(box, 5, 0, 10, 1)

# Replace scissors and shoes with rain and razor in Box 6
replace_items(box, 6, 2, ['rain', 'razor'])

# Replace necklace, jungle, and grinder with bear, bird, and horse in Box 1
replace_items(box, 1, 2, ['bear', 'bird', 'horse'])

# Swap boat in Box 9 with doll in Box 6
swap_items(box, 9, 4, 6, 0)

# Remove pot and thread from Box 10
box[10].remove('pot')
box[10].remove('thread')

# Move dice from Box 5 to Box 3
move_item(box, 5, 0, 3)

# Remove makeup and coat from Box 7
box[7].remove('makeup')
box[7].remove('coat')

# Move apple from Box 0 to Box 2
move_item(box, 0, 3, 2)

# Swap bear in Box 1 with crown in Box 2
swap_items(box, 1, 0, 2, 2)

# Move doll from Box 9 to Box 7
move_item(box, 9, 0, 7)

# Move tape from Box 12 to Box 1
move_item(box, 12, 0, 1)

# Swap tree in Box 4 with dice in Box 3
swap_items(box, 4, 1, 3, 0)

# Print the contents of each box
for box_index, items in box.items():
    print(f"Box {box_index}: {items}")