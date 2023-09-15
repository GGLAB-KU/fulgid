box_0 = ['lamp']
box_1 = ['lipstick', 'mirror', 'chair']
box_2 = ['makeup', 'card', 'necklace', 'toy']
box_3 = ['wig', 'soap', 'ocean', 'starfish', 'flower']
box_4 = ['shark', 'console']
box_5 = []
box_6 = ['note']
box_7 = ['fridge', 'pen', 'mountain', 'bag']
box_8 = []
box_9 = ['lightning', 'boat', 'button', 'bowl', 'table']
box_10 = ['cat', 'bus', 'tree', 'basket']
box_11 = ['planet', 'book']
box_12 = ['dolphin', 'river', 'horn', 'jacket']
box_13 = ['bird']

def move_item(source_box, destination_box, item):
    source_box.remove(item)
    destination_box.append(item)

def remove_item(box, item):
    box.remove(item)

def replace_item(box, item_to_remove, item_to_add):
    box.remove(item_to_remove)
    box.append(item_to_add)

# Move the lamp from Box 0 to Box 11
move_item(box_0, box_11, 'lamp')

# Swap the button in Box 9 with the card in Box 2
button = box_9.pop(box_9.index('button'))
card = box_2.pop(box_2.index('card'))
box_9.append(card)
box_2.append(button)

# Remove the bird from Box 13
remove_item(box_13, 'bird')

# Swap the starfish in Box 3 with the shark in Box 4
starfish = box_3.pop(box_3.index('starfish'))
shark = box_4.pop(box_4.index('shark'))
box_3.append(shark)
box_4.append(starfish)

# Remove the starfish from Box 4
remove_item(box_4, 'starfish')

# Move the planet and the lamp from Box 11 to Box 13
move_item(box_11, box_13, 'planet')
move_item(box_11, box_13, 'lamp')

# Move the console from Box 4 to Box 0
move_item(box_4, box_0, 'console')

# Swap the mountain in Box 7 with the note in Box 6
mountain = box_7.pop(box_7.index('mountain'))
note = box_6.pop(box_6.index('note'))
box_7.append(note)
box_6.append(mountain)

# Remove the console from Box 0
remove_item(box_0, 'console')

# Remove the shark and the wig from Box 3
remove_item(box_3, 'shark')
remove_item(box_3, 'wig')

# Remove the soap from Box 3
remove_item(box_3, 'soap')

# Replace the bus and the tree and the cat with the magnet and the pen and the mirror in Box 10
replace_item(box_10, 'bus', 'magnet')
replace_item(box_10, 'tree', 'pen')
replace_item(box_10, 'cat', 'mirror')

# Put the flower and the cup into Box 9
box_9.append('flower')
box_9.append('cup')

# Move the mountain from Box 6 to Box 8
move_item(box_6, box_8, 'mountain')

# Remove the mountain from Box 8
remove_item(box_8, 'mountain')

# Put the lamp and the branch into Box 1
box_1.append('lamp')
box_1.append('branch')

# Replace the pen and the magnet with the bear and the branch in Box 10
replace_item(box_10, 'pen', 'bear')
replace_item(box_10, 'magnet', 'branch')

# Replace the necklace with the doll in Box 2
replace_item(box_2, 'necklace', 'doll')

# Replace the planet and the lamp with the laptop and the microwave in Box 13
replace_item(box_13, 'planet', 'laptop')
replace_item(box_13, 'lamp', 'microwave')

# Move the fridge from Box 7 to Box 10
move_item(box_7, box_10, 'fridge')

# Swap the jacket in Box 12 with the laptop in Box 13
jacket = box_12.pop(box_12.index('jacket'))
laptop = box_13.pop(box_13.index('laptop'))
box_12.append(laptop)
box_13.append(jacket)

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")