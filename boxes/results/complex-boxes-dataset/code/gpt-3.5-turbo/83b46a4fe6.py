# Initial state of boxes
boxes = {
    0: ['bicycle', 'comb', 'camera', 'forest', 'leaf'],
    1: ['needle'],
    2: [],
    3: ['wire', 'sock', 'microscope'],
    4: ['scissors', 'game', 'spoon'],
    5: ['ship', 'paint', 'octopus', 'phone'],
    6: ['usb'],
    7: [],
    8: ['headphone']
}

# Replace the usb with the speaker in Box 6.
boxes[6].remove('usb')
boxes[6].append('speaker')

# Empty Box 4.
boxes[4] = []

# Remove the sock and the wire and the microscope from Box 3.
items_to_remove = ['sock', 'wire', 'microscope']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the speaker from Box 6.
boxes[6].remove('speaker')

# Put the lamp and the elephant and the dog into Box 4.
items_to_move = ['lamp', 'elephant', 'dog']
for item in items_to_move:
    boxes[4].append(item)

# Swap the phone in Box 5 with the comb in Box 0.
boxes[0].remove('comb')
boxes[5].remove('phone')
boxes[0].append('phone')
boxes[5].append('comb')

# Put the necklace and the card and the train into Box 8.
items_to_move = ['necklace', 'card', 'train']
for item in items_to_move:
    boxes[8].append(item)

# Move the card from Box 8 to Box 7.
boxes[8].remove('card')
boxes[7].append('card')

# Remove the train and the headphone and the necklace from Box 8.
items_to_remove = ['train', 'headphone', 'necklace']
for item in items_to_remove:
    boxes[8].remove(item)

# Move the card from Box 7 to Box 2.
boxes[7].remove('card')
boxes[2].append('card')

# Replace the card with the cloud in Box 2.
boxes[2].remove('card')
boxes[2].append('cloud')

# Remove the needle from Box 1.
boxes[1].remove('needle')

# Replace the elephant and the dog with the ship and the apple in Box 4.
boxes[4].remove('elephant')
boxes[4].remove('dog')
boxes[4].append('ship')
boxes[4].append('apple')

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")