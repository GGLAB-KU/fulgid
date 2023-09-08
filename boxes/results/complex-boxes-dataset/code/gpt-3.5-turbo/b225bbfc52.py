# Initial state of boxes
boxes = {
    0: ['toy', 'whistle', 'table'],
    1: ['watch', 'shorts', 'violin', 'brush', 'sun'],
    2: ['rain', 'charger', 'coin', 'puzzle'],
    3: ['dog', 'wire', 'lamp'],
    4: ['star', 'helmet', 'piano', 'pillow'],
    5: ['horse', 'hat', 'book'],
    6: ['scarf', 'thread', 'comb'],
    7: ['storm', 'river'],
    8: ['grass', 'cup', 'card', 'flute', 'mixer'],
    9: [],
    10: ['blanket', 'polish', 'dice', 'ring'],
    11: ['butterfly'],
    12: ['needle'],
    13: ['glove', 'necklace']
}

# Swap the needle in Box 12 with the charger in Box 2.
boxes[12], boxes[2] = boxes[2], boxes[12]

# Put the console and the shoe into Box 12.
boxes[12].append('console')
boxes[12].append('shoe')

# Replace the necklace with the mirror in Box 13.
boxes[13].remove('necklace')
boxes[13].append('mirror')

# Move the butterfly from Box 11 to Box 12.
boxes[11].remove('butterfly')
boxes[12].append('butterfly')

# Put the note and the watch and the storm into Box 2.
boxes[2].append('note')
boxes[2].append('watch')
boxes[2].append('storm')

# Swap the watch in Box 2 with the shorts in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Empty Box 13.
boxes[13] = []

# Put the truck into Box 10.
boxes[10].append('truck')

# Replace the shoe and the butterfly with the controller and the thread in Box 12.
boxes[12].remove('shoe')
boxes[12].remove('butterfly')
boxes[12].append('controller')
boxes[12].append('thread')

# Swap the console in Box 12 with the lamp in Box 3.
boxes[12], boxes[3] = boxes[3], boxes[12]

# Put the fish and the dice into Box 6.
boxes[6].append('fish')
boxes[6].append('dice')

# Replace the needle with the jungle in Box 2.
boxes[2].remove('needle')
boxes[2].append('jungle')

# Replace the jungle and the rain and the note with the coin and the butterfly and the bicycle in Box 2.
boxes[2].remove('jungle')
boxes[2].remove('rain')
boxes[2].remove('note')
boxes[2].append('coin')
boxes[2].append('butterfly')
boxes[2].append('bicycle')

# Move the storm and the river from Box 7 to Box 10.
boxes[7].remove('storm')
boxes[7].remove('river')
boxes[10].append('storm')
boxes[10].append('river')

# Swap the storm in Box 2 with the grass in Box 8.
boxes[2], boxes[8] = boxes[8], boxes[2]

# Swap the hat in Box 5 with the console in Box 3.
boxes[5], boxes[3] = boxes[3], boxes[5]

# Move the comb and the scarf from Box 6 to Box 12.
boxes[6].remove('comb')
boxes[6].remove('scarf')
boxes[12].append('comb')
boxes[12].append('scarf')

# Replace the controller and the thread and the lamp with the laptop and the shampoo and the car in Box 12.
boxes[12].remove('controller')
boxes[12].remove('thread')
boxes[12].remove('lamp')
boxes[12].append('laptop')
boxes[12].append('shampoo')
boxes[12].append('car')

# Replace the helmet with the phone in Box 4.
boxes[4].remove('helmet')
boxes[4].append('phone')

# Remove the truck and the blanket and the storm from Box 10.
boxes[10].remove('truck')
boxes[10].remove('blanket')
boxes[10].remove('storm')

# Put the brush and the elephant into Box 4.
boxes[4].append('brush')
boxes[4].append('elephant')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")