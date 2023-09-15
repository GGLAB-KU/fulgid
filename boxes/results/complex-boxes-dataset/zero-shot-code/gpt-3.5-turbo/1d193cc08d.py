box = {
    0: ['lamp', 'jacket', 'towel', 'plane', 'toaster'],
    1: ['wallet', 'mountain', 'bag', 'phone'],
    2: ['bus', 'bowl', 'perfume', 'needle', 'desert'],
    3: [],
    4: ['motorcycle'],
    5: ['necklace', 'horse'],
    6: ['microscope', 'star', 'whistle', 'scissors'],
    7: ['shampoo', 'boat', 'headphone', 'bell'],
    8: [],
    9: ['pan'],
    10: ['cup', 'pants', 'crown', 'battery'],
    11: ['bear', 'coin']
}

def move_item(source_box, destination_box, item):
    box[source_box].remove(item)
    box[destination_box].append(item)

def replace_item(box, item_to_remove, item_to_add):
    box.remove(item_to_remove)
    box.append(item_to_add)

# Put the horn into Box 5
box[5].append('horn')

# Move the toaster and the plane and the towel from Box 0 to Box 2
move_item(0, 2, 'toaster')
move_item(0, 2, 'plane')
move_item(0, 2, 'towel')

# Replace the bag with the brush in Box 1
replace_item(box[1], 'bag', 'brush')

# Move the star and the whistle and the scissors from Box 6 to Box 0
move_item(6, 0, 'star')
move_item(6, 0, 'whistle')
move_item(6, 0, 'scissors')

# Move the pan from Box 9 to Box 1
move_item(9, 1, 'pan')

# Replace the wallet and the pan with the comet and the cloud in Box 1
replace_item(box[1], 'wallet', 'comet')
replace_item(box[1], 'pan', 'cloud')

# Swap the cloud in Box 1 with the motorcycle in Box 4
replace_item(box[1], 'cloud', 'motorcycle')
replace_item(box[4], 'motorcycle', 'cloud')

# Remove the jacket and the whistle from Box 0
box[0].remove('jacket')
box[0].remove('whistle')

# Move the bear from Box 11 to Box 9
move_item(11, 9, 'bear')

# Put the apple and the piano and the basket into Box 4
box[4].extend(['apple', 'piano', 'basket'])

# Move the lamp and the scissors and the star from Box 0 to Box 2
move_item(0, 2, 'lamp')
move_item(0, 2, 'scissors')
move_item(0, 2, 'star')

# Put the shampoo and the bus into Box 11
box[11].extend(['shampoo', 'bus'])

# Move the crown from Box 10 to Box 0
move_item(10, 0, 'crown')

# Move the motorcycle and the phone from Box 1 to Box 3
move_item(1, 3, 'motorcycle')
move_item(1, 3, 'phone')

# Remove the battery and the cup from Box 10
box[10].remove('battery')
box[10].remove('cup')

# Remove the motorcycle from Box 3
box[3].remove('motorcycle')

# Move the headphone from Box 7 to Box 1
move_item(7, 1, 'headphone')

# Replace the bear with the polish in Box 9
replace_item(box[9], 'bear', 'polish')

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")