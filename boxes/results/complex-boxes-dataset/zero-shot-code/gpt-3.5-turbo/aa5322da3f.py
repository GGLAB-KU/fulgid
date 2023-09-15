box_0 = ['ring', 'rocket', 'plane', 'phone', 'toothbrush']
box_1 = ['cloud', 'gloves', 'comb', 'flute']
box_2 = ['cow', 'lipstick', 'dress', 'thunder']
box_3 = ['snow', 'blender']
box_4 = ['moon', 'submarine', 'blanket', 'butterfly', 'brush']
box_5 = ['umbrella', 'sock', 'flower', 'necklace', 'starfish']
box_6 = ['branch', 'frame', 'truck', 'boot', 'grinder']
box_7 = ['leaf', 'pillow', 'apple', 'motorcycle']
box_8 = ['puzzle', 'hat', 'mirror']
box_9 = ['helmet', 'island']
box_10 = ['freezer', 'basket', 'coin', 'microscope']

def print_boxes():
    for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]):
        print(f"Box {i}: {box}")

def move_item(source_box, target_box, item):
    source_box.remove(item)
    target_box.append(item)

def swap_items(box1, item1, box2, item2):
    box1.remove(item1)
    box2.remove(item2)
    box1.append(item2)
    box2.append(item1)

# Initial state
print_boxes()

# Put the boat into Box 8
move_item(box_0, box_8, 'boat')

# Move the freezer from Box 10 to Box 7
move_item(box_10, box_7, 'freezer')

# Swap the plane in Box 0 with the starfish in Box 5
swap_items(box_0, 'plane', box_5, 'starfish')

# Put the zipper and the lightning and the necklace into Box 3
box_3.extend(['zipper', 'lightning', 'necklace'])

# Swap the zipper in Box 3 with the apple in Box 7
swap_items(box_3, 'zipper', box_7, 'apple')

# Move the microscope from Box 10 to Box 9
move_item(box_10, box_9, 'microscope')

# Replace the toothbrush with the seaweed in Box 0
box_0.remove('toothbrush')
box_0.append('seaweed')

# Remove the grinder and the branch and the boot from Box 6
box_6.remove('grinder')
box_6.remove('branch')
box_6.remove('boot')

# Move the truck and the frame from Box 6 to Box 5
move_item(box_6, box_5, 'truck')
move_item(box_6, box_5, 'frame')

# Move the basket and the coin from Box 10 to Box 7
move_item(box_10, box_7, 'basket')
move_item(box_10, box_7, 'coin')

# Swap the truck in Box 5 with the cloud in Box 1
swap_items(box_5, 'truck', box_1, 'cloud')

# Swap the microscope in Box 9 with the blanket in Box 4
swap_items(box_9, 'microscope', box_4, 'blanket')

# Remove the submarine from Box 4
box_4.remove('submarine')

# Put the chair and the gloves and the octopus into Box 2
box_2.extend(['chair', 'gloves', 'octopus'])

# Put the belt and the shorts into Box 2
box_2.extend(['belt', 'shorts'])

# Put the lightning and the meteor and the card into Box 8
box_8.extend(['lightning', 'meteor', 'card'])

# Final state
print_boxes()