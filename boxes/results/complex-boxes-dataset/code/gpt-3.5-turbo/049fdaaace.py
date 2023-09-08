# Initial state of boxes
boxes = {
    0: ['fridge', 'wig', 'glove'],
    1: ['sun', 'doll'],
    2: [],
    3: [],
    4: ['key', 'jungle', 'usb', 'train'],
    5: ['lock', 'rocket'],
    6: ['microwave', 'freezer', 'meteor', 'mountain'],
    7: ['tree', 'coral', 'needle'],
    8: [],
    9: ['headphone'],
    10: ['bear', 'grass'],
    11: ['river', 'butterfly']
}

# Move the microwave and the mountain and the meteor from Box 6 to Box 2.
items_to_move = ['microwave', 'mountain', 'meteor']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Remove the sun and the doll from Box 1.
items_to_remove = ['sun', 'doll']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the meteor from Box 2.
boxes[2].remove('meteor')

# Replace the bear with the shorts in Box 10.
boxes[10].remove('bear')
boxes[10].append('shorts')

# Put the lamp into Box 5.
boxes[5].append('lamp')

# Swap the lamp in Box 5 with the freezer in Box 6.
boxes[5].remove('lamp')
boxes[6].remove('freezer')
boxes[5].append('freezer')
boxes[6].append('lamp')

# Put the magnet and the horse into Box 7.
boxes[7].append('magnet')
boxes[7].append('horse')

# Empty Box 0.
boxes[0] = []

# Move the headphone from Box 9 to Box 5.
boxes[9].remove('headphone')
boxes[5].append('headphone')

# Swap the shorts in Box 10 with the key in Box 4.
boxes[10].remove('shorts')
boxes[4].remove('key')
boxes[10].append('key')
boxes[4].append('shorts')

# Remove the coral from Box 7.
boxes[7].remove('coral')

# Move the lamp from Box 6 to Box 5.
boxes[6].remove('lamp')
boxes[5].append('lamp')

# Move the needle from Box 7 to Box 11.
boxes[7].remove('needle')
boxes[11].append('needle')

# Swap the microwave in Box 2 with the butterfly in Box 11.
boxes[2].remove('microwave')
boxes[11].remove('butterfly')
boxes[2].append('butterfly')
boxes[11].append('microwave')

# Remove the microwave and the needle from Box 11.
boxes[11].remove('microwave')
boxes[11].remove('needle')

# Remove the shorts and the usb from Box 4.
boxes[4].remove('shorts')
boxes[4].remove('usb')

# Remove the grass from Box 10.
boxes[10].remove('grass')

# Put the table into Box 6.
boxes[6].append('table')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")