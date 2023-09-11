# Initial state of boxes
boxes = {
    0: ['lightning', 'boot'],
    1: ['perfume', 'boat'],
    2: ['note', 'clock', 'vase', 'bear', 'comb'],
    3: ['glasses', 'cat', 'harmonica'],
    4: [],
    5: ['piano', 'bowl'],
    6: ['coral', 'planet', 'shampoo', 'bus', 'beach'],
    7: ['laptop', 'shoe'],
    8: ['pillow']
}

# Remove the pillow from Box 8.
boxes[8].remove('pillow')

# Move the boat from Box 1 to Box 7.
boxes[1].remove('boat')
boxes[7].append('boat')

# Move the planet from Box 6 to Box 5.
boxes[6].remove('planet')
boxes[5].append('planet')

# Remove the perfume from Box 1.
boxes[1].remove('perfume')

# Put the leaf and the planet into Box 7.
boxes[7].append('leaf')
boxes[7].append('planet')

# Move the lightning and the boot from Box 0 to Box 6.
boxes[0].remove('lightning')
boxes[0].remove('boot')
boxes[6].append('lightning')
boxes[6].append('boot')

# Replace the lightning with the crown in Box 6.
boxes[6].remove('lightning')
boxes[6].append('crown')

# Replace the piano and the bowl and the planet with the octopus and the river and the towel in Box 5.
boxes[5].remove('piano')
boxes[5].remove('bowl')
boxes[5].remove('planet')
boxes[5].append('octopus')
boxes[5].append('river')
boxes[5].append('towel')

# Put the flower into Box 5.
boxes[5].append('flower')

# Put the butterfly into Box 4.
boxes[4].append('butterfly')

# Empty Box 2.
boxes[2] = []

# Move the laptop and the planet from Box 7 to Box 1.
boxes[7].remove('laptop')
boxes[7].remove('planet')
boxes[1].append('laptop')
boxes[1].append('planet')

# Replace the planet with the comb in Box 1.
boxes[1].remove('planet')
boxes[1].append('comb')

# Move the leaf from Box 7 to Box 5.
boxes[7].remove('leaf')
boxes[5].append('leaf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")