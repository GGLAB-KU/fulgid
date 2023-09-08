# Initial state of boxes
boxes = {
    0: ['ring', 'rocket', 'plane', 'phone', 'toothbrush'],
    1: ['cloud', 'gloves', 'comb', 'flute'],
    2: ['cow', 'lipstick', 'dress', 'thunder'],
    3: ['snow', 'blender'],
    4: ['moon', 'submarine', 'blanket', 'butterfly', 'brush'],
    5: ['umbrella', 'sock', 'flower', 'necklace', 'starfish'],
    6: ['branch', 'frame', 'truck', 'boot', 'grinder'],
    7: ['leaf', 'pillow', 'apple', 'motorcycle'],
    8: ['puzzle', 'hat', 'mirror'],
    9: ['helmet', 'island'],
    10: ['freezer', 'basket', 'coin', 'microscope']
}

# Put the boat into Box 8.
boxes[8].append('boat')

# Move the freezer from Box 10 to Box 7.
boxes[10].remove('freezer')
boxes[7].append('freezer')

# Swap the plane in Box 0 with the starfish in Box 5.
boxes[0].remove('plane')
boxes[5].remove('starfish')
boxes[0].append('starfish')
boxes[5].append('plane')

# Put the zipper and the lightning and the necklace into Box 3.
items_to_move = ['zipper', 'lightning', 'necklace']
for item in items_to_move:
    boxes[3].append(item)

# Swap the zipper in Box 3 with the apple in Box 7.
boxes[3].remove('zipper')
boxes[7].remove('apple')
boxes[3].append('apple')
boxes[7].append('zipper')

# Move the microscope from Box 10 to Box 9.
boxes[10].remove('microscope')
boxes[9].append('microscope')

# Replace the toothbrush with the seaweed in Box 0.
boxes[0].remove('toothbrush')
boxes[0].append('seaweed')

# Remove the grinder and the branch and the boot from Box 6.
items_to_remove = ['grinder', 'branch', 'boot']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the truck and the frame from Box 6 to Box 5.
items_to_move = ['truck', 'frame']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Move the basket and the coin from Box 10 to Box 7.
items_to_move = ['basket', 'coin']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[7].append(item)

# Swap the truck in Box 5 with the cloud in Box 1.
boxes[5].remove('truck')
boxes[1].remove('cloud')
boxes[5].append('cloud')
boxes[1].append('truck')

# Swap the microscope in Box 9 with the blanket in Box 4.
boxes[9].remove('microscope')
boxes[4].remove('blanket')
boxes[9].append('blanket')
boxes[4].append('microscope')

# Remove the submarine from Box 4.
boxes[4].remove('submarine')

# Put the chair and the gloves and the octopus into Box 2.
items_to_move = ['chair', 'gloves', 'octopus']
for item in items_to_move:
    boxes[2].append(item)

# Put the belt and the shorts into Box 2.
items_to_move = ['belt', 'shorts']
for item in items_to_move:
    boxes[2].append(item)

# Put the lightning and the meteor and the card into Box 8.
items_to_move = ['lightning', 'meteor', 'card']
for item in items_to_move:
    boxes[8].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")