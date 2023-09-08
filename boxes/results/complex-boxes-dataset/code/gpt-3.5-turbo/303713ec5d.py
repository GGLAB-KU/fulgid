# Initial state of boxes
boxes = {
    0: ['lightning', 'crown', 'tape', 'shorts', 'horse'],
    1: ['shoes', 'whistle', 'scarf', 'basket', 'shirt'],
    2: [],
    3: ['dolphin', 'moon', 'bowl', 'perfume'],
    4: ['leaf'],
    5: ['wire', 'jungle', 'cow', 'magnet', 'toy'],
    6: ['brush', 'coat', 'forest', 'paint', 'vase'],
    7: ['microscope', 'guitar', 'branch', 'necklace', 'motorcycle'],
    8: ['puzzle'],
    9: ['usb', 'dog', 'lamp', 'dice'],
    10: ['keyboard'],
    11: [],
    12: ['coin', 'lion'],
    13: [],
    14: ['scissors', 'makeup']
}

# Replace the coin and the lion with the frame and the soap in Box 12.
boxes[12].remove('coin')
boxes[12].remove('lion')
boxes[12].append('frame')
boxes[12].append('soap')

# Put the needle into Box 1.
boxes[1].append('needle')

# Move the necklace from Box 7 to Box 11.
boxes[7].remove('necklace')
boxes[11].append('necklace')

# Remove the bowl from Box 3.
boxes[3].remove('bowl')

# Move the soap and the frame from Box 12 to Box 11.
boxes[12].remove('soap')
boxes[12].remove('frame')
boxes[11].append('soap')
boxes[11].append('frame')

# Remove the frame and the necklace from Box 11.
boxes[11].remove('frame')
boxes[11].remove('necklace')

# Replace the cow with the mixer in Box 5.
boxes[5].remove('cow')
boxes[5].append('mixer')

# Swap the crown in Box 0 with the branch in Box 7.
boxes[0].remove('crown')
boxes[7].remove('branch')
boxes[0].append('branch')
boxes[7].append('crown')

# Move the leaf from Box 4 to Box 3.
boxes[4].remove('leaf')
boxes[3].append('leaf')

# Move the leaf and the perfume and the dolphin from Box 3 to Box 10.
items_to_move = ['leaf', 'perfume', 'dolphin']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[10].append(item)

# Put the blanket into Box 0.
boxes[0].append('blanket')

# Replace the microscope and the motorcycle and the crown with the cow and the shoes and the cup in Box 7.
boxes[7].remove('microscope')
boxes[7].remove('motorcycle')
boxes[7].remove('crown')
boxes[7].append('cow')
boxes[7].append('shoes')
boxes[7].append('cup')

# Swap the moon in Box 3 with the paint in Box 6.
boxes[3].remove('moon')
boxes[6].remove('paint')
boxes[3].append('paint')
boxes[6].append('moon')

# Put the note and the clock and the horse into Box 9.
items_to_move = ['note', 'clock', 'horse']
for item in items_to_move:
    boxes[9].append(item)

# Put the bear and the branch and the thread into Box 9.
items_to_move = ['bear', 'branch', 'thread']
for item in items_to_move:
    boxes[9].append(item)

# Swap the shoes in Box 1 with the tape in Box 0.
boxes[1].remove('shoes')
boxes[0].remove('tape')
boxes[1].append('tape')
boxes[0].append('shoes')

# Put the lion and the train and the island into Box 5.
items_to_move = ['lion', 'train', 'island']
for item in items_to_move:
    boxes[5].append(item)

# Put the scissors into Box 3.
boxes[3].append('scissors')

# Move the magnet and the jungle and the toy from Box 5 to Box 8.
items_to_move = ['magnet', 'jungle', 'toy']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Put the mirror and the lamp and the table into Box 7.
items_to_move = ['mirror', 'lamp', 'table']
for item in items_to_move:
    boxes[7].append(item)

# Put the car and the branch and the island into Box 11.
items_to_move = ['car', 'branch', 'island']
for item in items_to_move:
    boxes[11].append(item)

# Replace the branch and the horse and the shorts with the sun and the flute and the bus in Box 0.
boxes[0].remove('branch')
boxes[0].remove('horse')
boxes[0].remove('shorts')
boxes[0].append('sun')
boxes[0].append('flute')
boxes[0].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")