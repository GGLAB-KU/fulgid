# Initial state of boxes
boxes = {
    0: ['razor', 'tree', 'harmonica', 'rocket', 'bell'],
    1: ['rock', 'candle', 'note', 'charger', 'submarine'],
    2: ['cow', 'spoon', 'tape'],
    3: ['cup', 'controller', 'beach'],
    4: ['basket', 'guitar', 'lock']
}

# Swap the basket in Box 4 with the cup in Box 3.
boxes[4].remove('basket')
boxes[3].remove('cup')
boxes[4].append('cup')
boxes[3].append('basket')

# Replace the rocket and the tree with the microscope and the lipstick in Box 0.
boxes[0].remove('rocket')
boxes[0].remove('tree')
boxes[0].append('microscope')
boxes[0].append('lipstick')

# Put the scissors and the magnet into Box 1.
boxes[1].append('scissors')
boxes[1].append('magnet')

# Swap the tape in Box 2 with the microscope in Box 0.
boxes[2].remove('tape')
boxes[0].remove('microscope')
boxes[2].append('microscope')
boxes[0].append('tape')

# Replace the razor and the harmonica and the tape with the toy and the laptop and the crown in Box 0.
boxes[0].remove('razor')
boxes[0].remove('harmonica')
boxes[0].remove('tape')
boxes[0].append('toy')
boxes[0].append('laptop')
boxes[0].append('crown')

# Swap the crown in Box 0 with the guitar in Box 4.
boxes[0].remove('crown')
boxes[4].remove('guitar')
boxes[0].append('guitar')
boxes[4].append('crown')

# Put the coral and the dice and the sculpture into Box 3.
boxes[3].append('coral')
boxes[3].append('dice')
boxes[3].append('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")