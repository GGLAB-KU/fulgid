# Initial state of boxes
boxes = {
    0: ['mountain', 'oven', 'shorts', 'star'],
    1: ['ring', 'jacket', 'camera', 'violin'],
    2: ['ship'],
    3: ['cloud'],
    4: ['dolphin', 'shirt'],
    5: ['bag', 'note', 'chair', 'lion'],
    6: ['soap', 'motorcycle', 'speaker', 'fridge'],
    7: ['phone'],
    8: ['dress'],
    9: ['dice', 'jungle', 'controller', 'usb']
}

# Move the controller and the dice and the usb from Box 9 to Box 0.
items_to_move = ['controller', 'dice', 'usb']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[0].append(item)

# Move the lion and the chair from Box 5 to Box 9.
items_to_move = ['lion', 'chair']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[9].append(item)

# Move the phone from Box 7 to Box 0.
boxes[7].remove('phone')
boxes[0].append('phone')

# Put the mirror into Box 7.
boxes[7].append('mirror')

# Replace the ship with the earring in Box 2.
boxes[2].remove('ship')
boxes[2].append('earring')

# Put the beach and the microscope into Box 5.
boxes[5].append('beach')
boxes[5].append('microscope')

# Put the car and the tiger into Box 2.
boxes[2].append('car')
boxes[2].append('tiger')

# Replace the cloud with the charger in Box 3.
boxes[3].remove('cloud')
boxes[3].append('charger')

# Swap the mirror in Box 7 with the earring in Box 2.
boxes[7].remove('mirror')
boxes[2].remove('earring')
boxes[7].append('earring')
boxes[2].append('mirror')

# Remove the motorcycle and the speaker and the fridge from Box 6.
items_to_remove = ['motorcycle', 'speaker', 'fridge']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the shirt and the dolphin from Box 4.
boxes[4].remove('shirt')
boxes[4].remove('dolphin')

# Move the tiger and the car from Box 2 to Box 5.
items_to_move = ['tiger', 'car']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Replace the lion and the jungle with the ring and the wallet in Box 9.
boxes[9].remove('lion')
boxes[9].remove('jungle')
boxes[9].append('ring')
boxes[9].append('wallet')

# Move the microscope from Box 5 to Box 8.
boxes[5].remove('microscope')
boxes[8].append('microscope')

# Move the soap from Box 6 to Box 7.
boxes[6].remove('soap')
boxes[7].append('soap')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")