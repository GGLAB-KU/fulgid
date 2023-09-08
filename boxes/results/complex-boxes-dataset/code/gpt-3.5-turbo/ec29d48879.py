# Initial state of boxes
boxes = {
    0: ['magnet', 'bell', 'mixer', 'moon'],
    1: ['drum', 'keyboard', 'oven', 'lock'],
    2: ['mirror', 'bowl', 'headphone', 'razor'],
    3: ['table'],
    4: ['forest', 'butterfly', 'frame', 'wig', 'lightning'],
    5: [],
    6: ['violin', 'button', 'controller'],
    7: ['coat', 'bicycle', 'mask', 'pillow'],
    8: ['car', 'dress'],
    9: [],
    10: ['phone'],
    11: [],
    12: ['earring', 'hat', 'meteor'],
    13: []
}

# Remove the dress and the car from Box 8.
boxes[8].remove('dress')
boxes[8].remove('car')

# Remove the table from Box 3.
boxes[3].remove('table')

# Move the bicycle from Box 7 to Box 5.
boxes[7].remove('bicycle')
boxes[5].append('bicycle')

# Move the wig and the lightning and the forest from Box 4 to Box 6.
items_to_move = ['wig', 'lightning', 'forest']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Remove the bicycle from Box 5.
boxes[5].remove('bicycle')

# Move the phone from Box 10 to Box 6.
boxes[10].remove('phone')
boxes[6].append('phone')

# Move the drum and the lock and the oven from Box 1 to Box 13.
items_to_move = ['drum', 'lock', 'oven']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[13].append(item)

# Move the magnet and the moon from Box 0 to Box 9.
items_to_move = ['magnet', 'moon']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Put the doll and the watch into Box 8.
items_to_put = ['doll', 'watch']
for item in items_to_put:
    boxes[8].append(item)

# Replace the keyboard with the controller in Box 1.
boxes[1].remove('keyboard')
boxes[1].append('controller')

# Put the train into Box 8.
boxes[8].append('train')

# Empty Box 6.
boxes[6] = []

# Move the mirror from Box 2 to Box 0.
boxes[2].remove('mirror')
boxes[0].append('mirror')

# Replace the magnet and the moon with the watch and the microwave in Box 9.
boxes[9].remove('magnet')
boxes[9].remove('moon')
boxes[9].append('watch')
boxes[9].append('microwave')

# Replace the oven and the drum with the sock and the leaf in Box 13.
boxes[13].remove('oven')
boxes[13].remove('drum')
boxes[13].append('sock')
boxes[13].append('leaf')

# Put the car and the gloves and the shelf into Box 11.
items_to_put = ['car', 'gloves', 'shelf']
for item in items_to_put:
    boxes[11].append(item)

# Empty Box 0.
boxes[0] = []

# Swap the sock in Box 13 with the razor in Box 2.
boxes[13].remove('sock')
boxes[2].remove('razor')
boxes[13].append('razor')
boxes[2].append('sock')

# Remove the frame and the butterfly from Box 4.
boxes[4].remove('frame')
boxes[4].remove('butterfly')

# Replace the coat and the pillow with the zipper and the skirt in Box 7.
boxes[7].remove('coat')
boxes[7].remove('pillow')
boxes[7].append('zipper')
boxes[7].append('skirt')

# Remove the earring from Box 12.
boxes[12].remove('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")