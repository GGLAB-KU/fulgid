# Initial state of boxes
boxes = {
    0: ['cat'],
    1: ['makeup', 'clock', 'leaf'],
    2: ['butterfly'],
    3: [],
    4: ['zipper'],
    5: ['earring', 'shoes', 'car', 'hat', 'octopus'],
    6: ['fridge'],
    7: ['note', 'planet', 'headphone', 'horse', 'glove'],
    8: ['tiger', 'island', 'helmet', 'sandals']
}

# Remove the cat from Box 0.
boxes[0].remove('cat')

# Put the boot and the violin into Box 3.
boxes[3].append('boot')
boxes[3].append('violin')

# Replace the car and the earring and the octopus with the meteor and the glove and the shoes in Box 5.
boxes[5].remove('car')
boxes[5].remove('earring')
boxes[5].remove('octopus')
boxes[5].append('meteor')
boxes[5].append('glove')
boxes[5].append('shoes')

# Remove the butterfly from Box 2.
boxes[2].remove('butterfly')

# Replace the island with the planet in Box 8.
boxes[8].remove('island')
boxes[8].append('planet')

# Swap the glove in Box 7 with the fridge in Box 6.
boxes[7].remove('glove')
boxes[6].remove('fridge')
boxes[7].append('fridge')
boxes[6].append('glove')

# Swap the note in Box 7 with the sandals in Box 8.
boxes[7].remove('note')
boxes[8].remove('sandals')
boxes[7].append('sandals')
boxes[8].append('note')

# Replace the glove with the storm in Box 6.
boxes[6].remove('glove')
boxes[6].append('storm')

# Move the shoes from Box 5 to Box 4.
boxes[5].remove('shoes')
boxes[4].append('shoes')

# Move the helmet and the note and the tiger from Box 8 to Box 0.
items_to_move = ['helmet', 'note', 'tiger']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[0].append(item)

# Move the tiger from Box 0 to Box 3.
boxes[0].remove('tiger')
boxes[3].append('tiger')

# Move the shoes and the hat and the glove from Box 5 to Box 1.
items_to_move = ['shoes', 'hat', 'glove']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Swap the storm in Box 6 with the planet in Box 8.
boxes[6].remove('storm')
boxes[8].remove('planet')
boxes[6].append('planet')
boxes[8].append('storm')

# Replace the meteor with the plate in Box 5.
boxes[5].remove('meteor')
boxes[5].append('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")