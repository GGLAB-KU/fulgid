# Initial state of boxes
boxes = {
    0: ['dolphin', 'butterfly'],
    1: ['microscope', 'bicycle', 'tree', 'microwave', 'spoon'],
    2: ['earring', 'cloud', 'scarf', 'crown', 'cup'],
    3: ['branch', 'laptop', 'doll', 'drum', 'bell'],
    4: ['button', 'polish', 'coat', 'bowl'],
    5: ['lightning', 'oven'],
    6: ['lamp', 'fridge', 'camera', 'moon', 'sculpture'],
    7: ['whistle'],
    8: ['ship', 'dress'],
    9: ['glasses', 'charger', 'bag', 'book', 'umbrella'],
    10: ['mixer']
}

# Remove the lamp and the sculpture from Box 6.
boxes[6].remove('lamp')
boxes[6].remove('sculpture')

# Remove the umbrella from Box 9.
boxes[9].remove('umbrella')

# Move the fridge from Box 6 to Box 5.
boxes[6].remove('fridge')
boxes[5].append('fridge')

# Move the moon from Box 6 to Box 7.
boxes[6].remove('moon')
boxes[7].append('moon')

# Replace the fridge with the ocean in Box 5.
boxes[5].remove('fridge')
boxes[5].append('ocean')

# Remove the microwave and the bicycle and the microscope from Box 1.
items_to_remove = ['microscope', 'bicycle', 'microwave']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the cloud and the earring and the scarf from Box 2 to Box 10.
items_to_move = ['cloud', 'earring', 'scarf']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Remove the butterfly from Box 0.
boxes[0].remove('butterfly')

# Replace the scarf and the mixer with the sandals and the clock in Box 10.
boxes[10].remove('scarf')
boxes[10].remove('mixer')
boxes[10].append('sandals')
boxes[10].append('clock')

# Move the bag and the charger from Box 9 to Box 6.
boxes[9].remove('bag')
boxes[9].remove('charger')
boxes[6].append('bag')
boxes[6].append('charger')

# Move the doll and the bell from Box 3 to Box 1.
boxes[3].remove('doll')
boxes[3].remove('bell')
boxes[1].append('doll')
boxes[1].append('bell')

# Empty Box 9.
boxes[9] = []

# Empty Box 3.
boxes[3] = []

# Remove the oven from Box 5.
boxes[5].remove('oven')

# Put the apple into Box 8.
boxes[8].append('apple')

# Put the guitar and the speaker and the bracelet into Box 7.
items_to_move = ['guitar', 'speaker', 'bracelet']
for item in items_to_move:
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")