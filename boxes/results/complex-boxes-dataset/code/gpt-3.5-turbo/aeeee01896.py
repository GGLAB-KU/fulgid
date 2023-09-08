# Initial state of boxes
boxes = {
    0: ['violin', 'lightning', 'battery'],
    1: [],
    2: ['coin', 'blender', 'island'],
    3: ['basket', 'bear', 'motorcycle', 'leaf', 'tie'],
    4: ['car', 'charger', 'sun', 'belt', 'candle'],
    5: ['comet', 'octopus', 'bus', 'phone'],
    6: ['coral', 'shampoo', 'needle', 'planet'],
    7: [],
    8: [],
    9: ['whistle', 'rocket', 'lipstick', 'microscope'],
    10: ['storm'],
    11: ['polish'],
    12: ['guitar', 'watch', 'scarf'],
    13: ['keyboard']
}

# Remove the whistle and the rocket and the microscope from Box 9.
items_to_remove = ['whistle', 'rocket', 'microscope']
for item in items_to_remove:
    boxes[9].remove(item)

# Move the storm from Box 10 to Box 12.
boxes[10].remove('storm')
boxes[12].append('storm')

# Remove the leaf from Box 3.
boxes[3].remove('leaf')

# Swap the polish in Box 11 with the planet in Box 6.
boxes[11].remove('polish')
boxes[6].remove('planet')
boxes[11].append('planet')
boxes[6].append('polish')

# Move the storm and the scarf and the watch from Box 12 to Box 4.
items_to_move = ['storm', 'scarf', 'watch']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[4].append(item)

# Replace the keyboard with the harmonica in Box 13.
boxes[13].remove('keyboard')
boxes[13].append('harmonica')

# Put the boot into Box 0.
boxes[0].append('boot')

# Put the swimsuit and the perfume into Box 6.
boxes[6].append('swimsuit')
boxes[6].append('perfume')

# Swap the lightning in Box 0 with the guitar in Box 12.
boxes[0].remove('lightning')
boxes[12].remove('guitar')
boxes[0].append('guitar')
boxes[12].append('lightning')

# Swap the lipstick in Box 9 with the tie in Box 3.
boxes[9].remove('lipstick')
boxes[3].remove('tie')
boxes[9].append('tie')
boxes[3].append('lipstick')

# Empty Box 9.
boxes[9] = []

# Swap the polish in Box 6 with the belt in Box 4.
boxes[6].remove('polish')
boxes[4].remove('belt')
boxes[6].append('belt')
boxes[4].append('polish')

# Swap the swimsuit in Box 6 with the bus in Box 5.
boxes[6].remove('swimsuit')
boxes[5].remove('bus')
boxes[6].append('bus')
boxes[5].append('swimsuit')

# Remove the octopus from Box 5.
boxes[5].remove('octopus')

# Move the planet from Box 11 to Box 8.
boxes[11].remove('planet')
boxes[8].append('planet')

# Replace the island with the mask in Box 2.
boxes[2].remove('island')
boxes[2].append('mask')

# Swap the needle in Box 6 with the motorcycle in Box 3.
boxes[6].remove('needle')
boxes[3].remove('motorcycle')
boxes[6].append('motorcycle')
boxes[3].append('needle')

# Put the glasses into Box 9.
boxes[9].append('glasses')

# Swap the boot in Box 0 with the planet in Box 8.
boxes[0].remove('boot')
boxes[8].remove('planet')
boxes[0].append('planet')
boxes[8].append('boot')

# Replace the mask with the tie in Box 2.
boxes[2].remove('mask')
boxes[2].append('tie')

# Swap the blender in Box 2 with the phone in Box 5.
boxes[2].remove('blender')
boxes[5].remove('phone')
boxes[2].append('phone')
boxes[5].append('blender')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")