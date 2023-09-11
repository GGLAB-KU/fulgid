# Initial state of boxes
boxes = {
    0: ['sun', 'phone', 'comb', 'lock'],
    1: ['needle', 'guitar', 'car', 'tape'],
    2: ['truck', 'basket', 'star', 'planet', 'shoes'],
    3: [],
    4: ['leaf'],
    5: ['octopus', 'train', 'toothbrush', 'cat'],
    6: ['laptop'],
    7: ['bowl'],
    8: ['grinder', 'key', 'rain', 'lamp'],
    9: [],
    10: []
}

# Move the bowl from Box 7 to Box 8.
boxes[7].remove('bowl')
boxes[8].append('bowl')

# Remove the laptop from Box 6.
boxes[6].remove('laptop')

# Remove the leaf from Box 4.
boxes[4].remove('leaf')

# Move the guitar and the car from Box 1 to Box 3.
items_to_move = ['guitar', 'car']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the jungle into Box 1.
boxes[1].append('jungle')

# Remove the comb and the lock and the sun from Box 0.
items_to_remove = ['comb', 'lock', 'sun']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the bowl and the rain and the key with the telescope and the zipper and the moon in Box 8.
boxes[8].remove('bowl')
boxes[8].remove('rain')
boxes[8].remove('key')
boxes[8].append('telescope')
boxes[8].append('zipper')
boxes[8].append('moon')

# Swap the telescope in Box 8 with the octopus in Box 5.
boxes[8].remove('telescope')
boxes[5].remove('octopus')
boxes[8].append('octopus')
boxes[5].append('telescope')

# Move the jungle from Box 1 to Box 9.
boxes[1].remove('jungle')
boxes[9].append('jungle')

# Remove the phone from Box 0.
boxes[0].remove('phone')

# Swap the planet in Box 2 with the train in Box 5.
boxes[2].remove('planet')
boxes[5].remove('train')
boxes[2].append('train')
boxes[5].append('planet')

# Remove the lamp and the octopus from Box 8.
boxes[8].remove('lamp')
boxes[8].remove('octopus')

# Put the zipper and the button and the ring into Box 9.
items_to_put = ['zipper', 'button', 'ring']
for item in items_to_put:
    boxes[9].append(item)

# Put the submarine and the shampoo into Box 3.
boxes[3].append('submarine')
boxes[3].append('shampoo')

# Put the spoon and the bear and the toy into Box 4.
items_to_put = ['spoon', 'bear', 'toy']
for item in items_to_put:
    boxes[4].append(item)

# Move the ring and the zipper and the jungle from Box 9 to Box 8.
items_to_move = ['ring', 'zipper', 'jungle']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[8].append(item)

# Replace the needle and the tape with the tiger and the razor in Box 1.
boxes[1].remove('needle')
boxes[1].remove('tape')
boxes[1].append('tiger')
boxes[1].append('razor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")