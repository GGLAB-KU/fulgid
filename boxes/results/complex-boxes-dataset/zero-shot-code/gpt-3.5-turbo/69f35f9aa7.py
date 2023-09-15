box = {
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

# Remove the pillow from Box 8
box[8] = []

# Move the boat from Box 1 to Box 7
box[7].append(box[1].pop(box[1].index('boat')))

# Move the planet from Box 6 to Box 5
box[5].append(box[6].pop(box[6].index('planet')))

# Remove the perfume from Box 1
box[1].remove('perfume')

# Put the leaf and the planet into Box 7
box[7].extend(['leaf', 'planet'])

# Move the lightning and the boot from Box 0 to Box 6
box[6].extend(box[0].pop(box[0].index('lightning')))
box[6].extend(box[0].pop(box[0].index('boot')))

# Replace the lightning with the crown in Box 6
box[6].remove('lightning')
box[6].append('crown')

# Replace the piano and the bowl and the planet with the octopus and the river and the towel in Box 5
box[5].remove('piano')
box[5].remove('bowl')
box[5].remove('planet')
box[5].extend(['octopus', 'river', 'towel'])

# Put the flower into Box 5
box[5].append('flower')

# Put the butterfly into Box 4
box[4].append('butterfly')

# Empty Box 2
box[2] = []

# Move the laptop and the planet from Box 7 to Box 1
box[1].extend(box[7].pop(box[7].index('laptop')))
box[1].extend(box[7].pop(box[7].index('planet')))

# Replace the planet with the comb in Box 1
box[1].remove('planet')
box[1].append('comb')

# Move the leaf from Box 7 to Box 5
box[5].append(box[7].pop(box[7].index('leaf')))

# Print the contents of each box
for i in range(9):
    print(f"Box {i}: {box[i]}")