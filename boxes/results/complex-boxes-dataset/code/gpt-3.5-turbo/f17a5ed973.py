# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: [],
    3: ['cat', 'chair', 'fish'],
    4: ['fridge', 'shorts', 'toaster', 'island'],
    5: ['headphone', 'lion', 'wig'],
    6: ['bus', 'mirror', 'gloves', 'piano'],
    7: ['snow', 'soap', 'bear'],
    8: ['toothbrush'],
    9: ['razor', 'car'],
    10: ['thread', 'pan'],
    11: ['storm', 'shirt', 'dog', 'bird']
}

# Put the lion and the planet and the button into Box 6.
boxes[6].append('lion')
boxes[6].append('planet')
boxes[6].append('button')

# Move the piano and the gloves and the button from Box 6 to Box 2.
items_to_move = ['piano', 'gloves', 'button']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Remove the bus and the planet from Box 6.
boxes[6].remove('bus')
boxes[6].remove('planet')

# Empty Box 8.
boxes[8] = []

# Move the thread from Box 10 to Box 2.
boxes[10].remove('thread')
boxes[2].append('thread')

# Remove the piano from Box 2.
boxes[2].remove('piano')

# Put the sun and the plate into Box 9.
boxes[9].append('sun')
boxes[9].append('plate')

# Replace the shirt and the dog and the storm with the seaweed and the mixer and the sculpture in Box 11.
boxes[11].remove('shirt')
boxes[11].remove('dog')
boxes[11].remove('storm')
boxes[11].append('seaweed')
boxes[11].append('mixer')
boxes[11].append('sculpture')

# Replace the mixer and the sculpture and the bird with the bell and the mask and the basket in Box 11.
boxes[11].remove('mixer')
boxes[11].remove('sculpture')
boxes[11].remove('bird')
boxes[11].append('bell')
boxes[11].append('mask')
boxes[11].append('basket')

# Replace the bell and the mask and the seaweed with the coin and the grinder and the basket in Box 11.
boxes[11].remove('bell')
boxes[11].remove('mask')
boxes[11].remove('seaweed')
boxes[11].append('coin')
boxes[11].append('grinder')
boxes[11].append('basket')

# Move the snow and the soap and the bear from Box 7 to Box 5.
items_to_move = ['snow', 'soap', 'bear']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Swap the fish in Box 3 with the wig in Box 5.
boxes[3].remove('fish')
boxes[5].remove('wig')
boxes[3].append('wig')
boxes[5].append('fish')

# Empty Box 6.
boxes[6] = []

# Move the island and the toaster from Box 4 to Box 5.
boxes[4].remove('island')
boxes[4].remove('toaster')
boxes[5].append('island')
boxes[5].append('toaster')

# Swap the sun in Box 9 with the basket in Box 11.
boxes[9].remove('sun')
boxes[11].remove('basket')
boxes[9].append('basket')
boxes[11].append('sun')

# Move the gloves and the button and the thread from Box 2 to Box 0.
items_to_move = ['gloves', 'button', 'thread']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the car in Box 9 with the wig in Box 3.
boxes[9].remove('car')
boxes[3].remove('wig')
boxes[9].append('wig')
boxes[3].append('car')

# Put the keyboard and the bracelet and the seaweed into Box 6.
boxes[6].append('keyboard')
boxes[6].append('bracelet')
boxes[6].append('seaweed')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")