# Initial state of boxes
boxes = {
    0: ['plate', 'branch', 'starfish', 'chair'],
    1: ['microscope', 'guitar', 'fridge'],
    2: [],
    3: ['button'],
    4: ['soap'],
    5: ['violin', 'laptop', 'dog', 'helmet'],
    6: ['planet', 'telescope'],
    7: ['toaster', 'table', 'dress', 'island', 'glove'],
    8: [],
    9: ['bell', 'pants', 'frame'],
    10: ['bowl', 'fork', 'shorts', 'mountain', 'cup'],
    11: ['gloves']
}

# Remove the fridge and the guitar from Box 1.
boxes[1].remove('fridge')
boxes[1].remove('guitar')

# Swap the microscope in Box 1 with the soap in Box 4.
boxes[1].remove('microscope')
boxes[4].remove('soap')
boxes[1].append('soap')
boxes[4].append('microscope')

# Remove the button from Box 3.
boxes[3].remove('button')

# Put the pillow and the helmet into Box 8.
boxes[8].append('pillow')
boxes[8].append('helmet')

# Put the sandals and the crown and the clock into Box 8.
boxes[8].append('sandals')
boxes[8].append('crown')
boxes[8].append('clock')

# Empty Box 7.
boxes[7] = []

# Put the island into Box 0.
boxes[0].append('island')

# Replace the frame and the pants with the microscope and the usb in Box 9.
boxes[9].remove('frame')
boxes[9].remove('pants')
boxes[9].append('microscope')
boxes[9].append('usb')

# Put the octopus into Box 11.
boxes[11].append('octopus')

# Move the gloves from Box 11 to Box 0.
boxes[11].remove('gloves')
boxes[0].append('gloves')

# Swap the mountain in Box 10 with the octopus in Box 11.
boxes[10].remove('mountain')
boxes[11].remove('octopus')
boxes[10].append('octopus')
boxes[11].append('mountain')

# Remove the mountain from Box 11.
boxes[11].remove('mountain')

# Move the microscope from Box 4 to Box 6.
boxes[4].remove('microscope')
boxes[6].append('microscope')

# Swap the soap in Box 1 with the chair in Box 0.
boxes[1].remove('soap')
boxes[0].remove('chair')
boxes[1].append('chair')
boxes[0].append('soap')

# Move the dog from Box 5 to Box 9.
boxes[5].remove('dog')
boxes[9].append('dog')

# Replace the pillow and the crown with the basket and the sculpture in Box 8.
boxes[8].remove('pillow')
boxes[8].remove('crown')
boxes[8].append('basket')
boxes[8].append('sculpture')

# Put the scarf and the charger and the whistle into Box 5.
boxes[5].append('scarf')
boxes[5].append('charger')
boxes[5].append('whistle')

# Swap the clock in Box 8 with the chair in Box 1.
boxes[8].remove('clock')
boxes[1].remove('chair')
boxes[8].append('chair')
boxes[1].append('clock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")