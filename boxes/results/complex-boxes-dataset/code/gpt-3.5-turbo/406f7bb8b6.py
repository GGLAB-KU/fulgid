# Initial state of boxes
boxes = {
    0: [],
    1: ['desert', 'rocket', 'dice', 'island', 'star'],
    2: ['car', 'belt', 'frame', 'toy'],
    3: ['shorts', 'dolphin', 'flower'],
    4: ['submarine', 'needle', 'skirt', 'ocean', 'comb'],
    5: ['doll', 'piano', 'cloud'],
    6: [],
    7: ['pan', 'clock', 'charger', 'helmet', 'fish'],
    8: ['ship', 'shelf', 'pot', 'dog'],
    9: ['guitar', 'blender', 'thread', 'shampoo', 'makeup'],
    10: ['lamp']
}

# Put the doll and the soap and the motorcycle into Box 7.
boxes[7].append('doll')
boxes[7].append('soap')
boxes[7].append('motorcycle')

# Move the comb from Box 4 to Box 0.
boxes[4].remove('comb')
boxes[0].append('comb')

# Remove the submarine and the needle from Box 4.
boxes[4].remove('submarine')
boxes[4].remove('needle')

# Move the toy and the belt and the car from Box 2 to Box 10.
items_to_move = ['toy', 'belt', 'car']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Move the makeup and the guitar and the blender from Box 9 to Box 6.
items_to_move = ['makeup', 'guitar', 'blender']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[6].append(item)

# Replace the frame with the dog in Box 2.
boxes[2].remove('frame')
boxes[2].append('dog')

# Put the blender and the truck and the lock into Box 1.
boxes[1].append('blender')
boxes[1].append('truck')
boxes[1].append('lock')

# Move the dog from Box 2 to Box 1.
boxes[2].remove('dog')
boxes[1].append('dog')

# Put the sandals and the toaster into Box 9.
boxes[9].append('sandals')
boxes[9].append('toaster')

# Remove the blender and the makeup from Box 6.
boxes[6].remove('blender')
boxes[6].remove('makeup')

# Empty Box 7.
boxes[7] = []

# Replace the shampoo and the sandals and the toaster with the console and the rain and the car in Box 9.
boxes[9].remove('shampoo')
boxes[9].remove('sandals')
boxes[9].remove('toaster')
boxes[9].append('console')
boxes[9].append('rain')
boxes[9].append('car')

# Swap the comb in Box 0 with the guitar in Box 6.
boxes[0].remove('comb')
boxes[6].remove('guitar')
boxes[0].append('guitar')
boxes[6].append('comb')

# Swap the console in Box 9 with the truck in Box 1.
boxes[9].remove('console')
boxes[1].remove('truck')
boxes[9].append('truck')
boxes[1].append('console')

# Replace the car and the belt and the lamp with the thread and the rocket and the keyboard in Box 10.
boxes[10].remove('car')
boxes[10].remove('belt')
boxes[10].remove('lamp')
boxes[10].append('thread')
boxes[10].append('rocket')
boxes[10].append('keyboard')

# Replace the piano with the butterfly in Box 5.
boxes[5].remove('piano')
boxes[5].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")