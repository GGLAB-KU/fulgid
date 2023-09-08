# Initial state of boxes
boxes = {
    0: ['mixer'],
    1: ['shoes', 'button', 'bag', 'tape'],
    2: ['vase', 'seaweed'],
    3: ['speaker', 'rock', 'controller', 'doll'],
    4: [],
    5: ['cow', 'tree', 'frame'],
    6: ['plate'],
    7: ['car', 'grass'],
    8: ['ship'],
    9: ['necklace', 'clock', 'branch'],
    10: ['charger', 'sock', 'river'],
    11: ['plane', 'toothpaste', 'oven', 'sun'],
    12: ['starfish', 'earring', 'snow', 'phone', 'forest'],
    13: ['blanket', 'bell'],
    14: ['makeup', 'shelf', 'ocean', 'usb', 'toaster']
}

# Move the tape and the shoes and the bag from Box 1 to Box 9.
items_to_move = ['tape', 'shoes', 'bag']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[9].append(item)

# Swap the vase in Box 2 with the button in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Replace the frame with the bicycle in Box 5.
boxes[5].remove('frame')
boxes[5].append('bicycle')

# Replace the bag and the branch and the tape with the pen and the table and the moon in Box 9.
items_to_remove = ['bag', 'branch', 'tape']
items_to_add = ['pen', 'table', 'moon']
for item in items_to_remove:
    boxes[9].remove(item)
for item in items_to_add:
    boxes[9].append(item)

# Swap the starfish in Box 12 with the bicycle in Box 5.
boxes[12], boxes[5] = boxes[5], boxes[12]

# Move the forest and the earring and the phone from Box 12 to Box 9.
items_to_move = ['forest', 'earring', 'phone']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[9].append(item)

# Swap the mixer in Box 0 with the snow in Box 12.
boxes[0], boxes[12] = boxes[12], boxes[0]

# Swap the necklace in Box 9 with the vase in Box 1.
boxes[9], boxes[1] = boxes[1], boxes[9]

# Put the clock into Box 0.
boxes[0].append('clock')

# Empty Box 9.
boxes[9] = []

# Move the plate from Box 6 to Box 8.
boxes[6].remove('plate')
boxes[8].append('plate')

# Empty Box 12.
boxes[12] = []

# Move the necklace from Box 1 to Box 13.
boxes[1].remove('necklace')
boxes[13].append('necklace')

# Move the clock and the snow from Box 0 to Box 13.
items_to_move = ['clock', 'snow']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[13].append(item)

# Empty Box 13.
boxes[13] = []

# Put the leaf and the umbrella into Box 8.
boxes[8].extend(['leaf', 'umbrella'])

# Put the toothbrush and the blender into Box 7.
boxes[7].extend(['toothbrush', 'blender'])

# Move the car from Box 7 to Box 3.
boxes[7].remove('car')
boxes[3].append('car')

# Remove the toothbrush from Box 7.
boxes[7].remove('toothbrush')

# Remove the button from Box 2.
boxes[2].remove('button')

# Move the seaweed from Box 2 to Box 3.
boxes[2].remove('seaweed')
boxes[3].append('seaweed')

# Swap the river in Box 10 with the shelf in Box 14.
boxes[10], boxes[14] = boxes[14], boxes[10]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")