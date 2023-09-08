# Initial state of boxes
boxes = {
    0: ['fish', 'sculpture', 'car', 'cloud'],
    1: ['dog'],
    2: ['mixer', 'bell', 'shampoo', 'usb', 'shoe'],
    3: ['pot', 'skirt', 'rocket'],
    4: ['harmonica', 'pants', 'wire'],
    5: [],
    6: ['headphone', 'crown', 'ocean'],
    7: ['lock', 'star'],
    8: ['toaster'],
    9: ['fork'],
    10: ['vase', 'tree', 'plate', 'brush'],
    11: ['island'],
    12: ['frame', 'shoes', 'spoon', 'bird'],
    13: ['bicycle', 'console', 'shirt', 'perfume'],
    14: ['guitar', 'doll']
}

# Move the dog from Box 1 to Box 6.
boxes[1].remove('dog')
boxes[6].append('dog')

# Replace the rocket and the pot with the swimsuit and the desert in Box 3.
boxes[3].remove('rocket')
boxes[3].remove('pot')
boxes[3].append('swimsuit')
boxes[3].append('desert')

# Put the earring into Box 0.
boxes[0].append('earring')

# Replace the headphone and the crown with the wire and the polish in Box 6.
boxes[6].remove('headphone')
boxes[6].remove('crown')
boxes[6].append('wire')
boxes[6].append('polish')

# Put the truck into Box 6.
boxes[6].append('truck')

# Remove the fork from Box 9.
boxes[9].remove('fork')

# Replace the toaster with the toothpaste in Box 8.
boxes[8].remove('toaster')
boxes[8].append('toothpaste')

# Remove the swimsuit from Box 3.
boxes[3].remove('swimsuit')

# Remove the island from Box 11.
boxes[11].remove('island')

# Move the toothpaste from Box 8 to Box 5.
boxes[8].remove('toothpaste')
boxes[5].append('toothpaste')

# Swap the mixer in Box 2 with the bicycle in Box 13.
boxes[2].remove('mixer')
boxes[13].remove('bicycle')
boxes[2].append('bicycle')
boxes[13].append('mixer')

# Put the dress and the earring and the submarine into Box 7.
items_to_move = ['dress', 'earring', 'submarine']
for item in items_to_move:
    boxes[7].append(item)

# Remove the earring from Box 0.
boxes[0].remove('earring')

# Replace the submarine and the dress and the lock with the leaf and the brush and the belt in Box 7.
boxes[7].remove('submarine')
boxes[7].remove('dress')
boxes[7].remove('lock')
boxes[7].append('leaf')
boxes[7].append('brush')
boxes[7].append('belt')

# Put the elephant into Box 3.
boxes[3].append('elephant')

# Move the earring and the belt from Box 7 to Box 12.
items_to_move = ['earring', 'belt']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[12].append(item)

# Replace the guitar with the candle in Box 14.
boxes[14].remove('guitar')
boxes[14].append('candle')

# Swap the earring in Box 12 with the skirt in Box 3.
boxes[12].remove('earring')
boxes[3].remove('skirt')
boxes[12].append('skirt')
boxes[3].append('earring')

# Swap the fish in Box 0 with the star in Box 7.
boxes[0].remove('fish')
boxes[7].remove('star')
boxes[0].append('star')
boxes[7].append('fish')

# Move the toothpaste from Box 5 to Box 12.
boxes[5].remove('toothpaste')
boxes[12].append('toothpaste')

# Move the sculpture and the car from Box 0 to Box 9.
items_to_move = ['sculpture', 'car']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Swap the tree in Box 10 with the shoes in Box 12.
boxes[10].remove('tree')
boxes[12].remove('shoes')
boxes[10].append('shoes')
boxes[12].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")