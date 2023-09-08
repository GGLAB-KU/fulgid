# Initial state of boxes
boxes = {
    0: ['bell', 'coat', 'toaster', 'lamp'],
    1: ['meteor'],
    2: ['usb', 'ship'],
    3: ['jacket', 'puzzle', 'scissors', 'island', 'bracelet'],
    4: ['flute', 'microscope'],
    5: [],
    6: ['plate']
}

# Replace the microscope and the flute with the bear and the tape in Box 4.
boxes[4].remove('microscope')
boxes[4].remove('flute')
boxes[4].append('bear')
boxes[4].append('tape')

# Move the bell and the coat and the lamp from Box 0 to Box 2.
items_to_move = ['bell', 'coat', 'lamp']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Swap the meteor in Box 1 with the plate in Box 6.
boxes[1].remove('meteor')
boxes[6].remove('plate')
boxes[1].append('plate')
boxes[6].append('meteor')

# Remove the meteor from Box 6.
boxes[6].remove('meteor')

# Put the leaf into Box 4.
boxes[4].append('leaf')

# Replace the plate with the dress in Box 1.
boxes[1].remove('plate')
boxes[1].append('dress')

# Put the needle into Box 4.
boxes[4].append('needle')

# Replace the island with the train in Box 3.
boxes[3].remove('island')
boxes[3].append('train')

# Swap the toaster in Box 0 with the needle in Box 4.
boxes[0].remove('toaster')
boxes[4].remove('needle')
boxes[0].append('needle')
boxes[4].append('toaster')

# Replace the usb and the ship with the submarine and the lock in Box 2.
boxes[2].remove('usb')
boxes[2].remove('ship')
boxes[2].append('submarine')
boxes[2].append('lock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")