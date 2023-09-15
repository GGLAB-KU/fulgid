box_0 = ['shoes', 'rain', 'jungle']
box_1 = ['cloud', 'leaf']
box_2 = []
box_3 = ['puzzle', 'crown', 'coat']
box_4 = ['mirror', 'lamp', 'glove', 'cat', 'magnet']
box_5 = ['mountain', 'bus', 'polish']
box_6 = ['bag']
box_7 = ['piano', 'toothpaste', 'train']
box_8 = ['necklace', 'game', 'bicycle', 'branch', 'earring']
box_9 = ['skirt', 'soap']
box_10 = ['octopus', 'apple']
box_11 = ['bracelet', 'frame']
box_12 = ['candle']

def move_item(source_box, destination_box, item):
    source_box.remove(item)
    destination_box.append(item)

def empty_box(box):
    box.clear()

def replace_item(box, old_item, new_item):
    box.remove(old_item)
    box.append(new_item)

# Move the crown from Box 3 to Box 9
move_item(box_3, box_9, 'crown')

# Empty Box 10
empty_box(box_10)

# Replace the leaf with the freezer in Box 1
replace_item(box_1, 'leaf', 'freezer')

# Replace the magnet and the mirror and the lamp with the bear and the branch and the microwave in Box 4
replace_item(box_4, 'magnet', 'bear')
replace_item(box_4, 'mirror', 'branch')
replace_item(box_4, 'lamp', 'microwave')

# Replace the branch and the necklace and the game with the harmonica and the butterfly and the lamp in Box 8
replace_item(box_8, 'branch', 'harmonica')
replace_item(box_8, 'necklace', 'butterfly')
replace_item(box_8, 'game', 'lamp')

# Put the comb into Box 3
box_3.append('comb')

# Move the candle from Box 12 to Box 7
move_item(box_12, box_7, 'candle')

# Replace the bus with the tiger in Box 5
replace_item(box_5, 'bus', 'tiger')

# Put the mountain into Box 3
box_3.append('mountain')

# Empty Box 5
empty_box(box_5)

# Remove the bracelet from Box 11
box_11.remove('bracelet')

# Remove the bag from Box 6
box_6.clear()

# Move the crown and the skirt and the soap from Box 9 to Box 3
move_item(box_9, box_3, 'crown')
move_item(box_9, box_3, 'skirt')
move_item(box_9, box_3, 'soap')

# Replace the frame with the toothpaste in Box 11
replace_item(box_11, 'frame', 'toothpaste')

# Move the freezer from Box 1 to Box 3
move_item(box_1, box_3, 'freezer')

# Move the glove and the microwave from Box 4 to Box 5
move_item(box_4, box_5, 'glove')
move_item(box_4, box_5, 'microwave')

# Move the toothpaste from Box 11 to Box 5
move_item(box_11, box_5, 'toothpaste')

# Put the crown and the mirror and the phone into Box 7
box_7.append('crown')
box_7.append('mirror')
box_7.append('phone')

# Replace the skirt and the mountain with the train and the lock in Box 3
replace_item(box_3, 'skirt', 'train')
replace_item(box_3, 'mountain', 'lock')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")