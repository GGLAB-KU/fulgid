box = {
    0: ['planet', 'console'],
    1: ['lipstick', 'glove', 'river', 'key'],
    2: ['umbrella'],
    3: ['battery', 'paint'],
    4: [],
    5: ['dice', 'ship', 'table'],
    6: ['coral', 'shampoo', 'shoe', 'sock', 'ring'],
    7: ['lock', 'fridge', 'horn'],
    8: ['blanket', 'moon', 'necklace'],
    9: ['phone', 'toothpaste', 'flower', 'skirt'],
    10: ['boat', 'bell'],
    11: ['lightning'],
    12: ['game', 'brush', 'telescope', 'cloud', 'puzzle'],
    13: [],
    14: []
}

def remove_item(box_num, item):
    if item in box[box_num]:
        box[box_num].remove(item)

def add_item(box_num, item):
    box[box_num].append(item)

def swap_items(box_num1, item1, box_num2, item2):
    if item1 in box[box_num1] and item2 in box[box_num2]:
        box[box_num1].remove(item1)
        box[box_num2].remove(item2)
        box[box_num1].append(item2)
        box[box_num2].append(item1)

def move_item(from_box, to_box, item):
    if item in box[from_box]:
        box[from_box].remove(item)
        box[to_box].append(item)

# Remove items from Box 8
remove_item(8, 'moon')
remove_item(8, 'necklace')
remove_item(8, 'blanket')

# Remove items from Box 6
remove_item(6, 'shoe')
remove_item(6, 'shampoo')

# Remove items from Box 5
remove_item(5, 'dice')
remove_item(5, 'table')

# Add usb to Box 7
add_item(7, 'usb')

# Swap battery with key
swap_items(3, 'battery', 1, 'key')

# Swap console with ship
swap_items(0, 'console', 5, 'ship')

# Swap console with boat
swap_items(5, 'console', 10, 'boat')

# Move key and paint to Box 11
move_item(3, 11, 'key')
move_item(1, 11, 'paint')

# Move fridge, usb, and horn to Box 14
move_item(7, 14, 'fridge')
move_item(7, 14, 'usb')
move_item(7, 14, 'horn')

# Swap boat with ship
swap_items(5, 'boat', 0, 'ship')

# Replace boat and planet with scissors and console
box[0] = ['scissors', 'console']

# Move ship to Box 8
move_item(5, 8, 'ship')

# Replace console and scissors with snow and flower
box[0] = ['snow', 'flower']

# Replace battery and lipstick with comb and seaweed
box[1] = ['comb', 'seaweed']

# Move ring and coral to Box 1
move_item(6, 1, 'ring')
move_item(6, 1, 'coral')

# Move paint and key to Box 7
move_item(11, 7, 'paint')
move_item(11, 7, 'key')

# Remove cloud, game, and puzzle from Box 12
remove_item(12, 'cloud')
remove_item(12, 'game')
remove_item(12, 'puzzle')

# Swap telescope with lightning
swap_items(12, 'telescope', 11, 'lightning')

# Put beach and pants into Box 1
add_item(1, 'beach')
add_item(1, 'pants')

# Swap lightning with telescope
swap_items(12, 'lightning', 11, 'telescope')

# Swap console with ship
swap_items(10, 'console', 8, 'ship')

# Put fork and tree into Box 10
add_item(10, 'fork')
add_item(10, 'tree')

# Print the contents of each box
for box_num, items in box.items():
    print(f"Box {box_num}: {items}")