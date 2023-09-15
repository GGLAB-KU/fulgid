box = {
    0: ['river', 'plane', 'lipstick', 'whistle', 'tree'],
    1: [],
    2: ['polish', 'forest', 'pants', 'storm'],
    3: ['comb'],
    4: ['battery'],
    5: [],
    6: ['cow', 'shorts', 'seaweed', 'toy', 'jacket'],
    7: ['makeup', 'wire', 'spoon', 'book', 'shoe'],
    8: ['bicycle', 'wallet', 'flower', 'train', 'vase'],
    9: ['magnet'],
    10: ['sandals', 'grinder', 'comet', 'grass']
}

# Empty Box 8
box[8] = []

# Remove the shorts and the toy and the jacket from Box 6
box[6].remove('shorts')
box[6].remove('toy')
box[6].remove('jacket')

# Remove the wire from Box 7
box[7].remove('wire')

# Remove the comet from Box 10
box[10].remove('comet')

# Move the whistle from Box 0 to Box 2
box[2].append('whistle')
box[0].remove('whistle')

# Swap the spoon in Box 7 with the whistle in Box 2
box[7].remove('spoon')
box[2].remove('whistle')
box[7].append('whistle')
box[2].append('spoon')

# Swap the spoon in Box 2 with the battery in Box 4
box[2].remove('spoon')
box[4].remove('battery')
box[2].append('battery')
box[4].append('spoon')

# Move the storm from Box 2 to Box 4
box[4].append('storm')
box[2].remove('storm')

# Move the whistle and the book from Box 7 to Box 8
box[8].append('whistle')
box[8].append('book')
box[7].remove('whistle')
box[7].remove('book')

# Swap the pants in Box 2 with the book in Box 8
box[2].remove('pants')
box[8].remove('book')
box[2].append('book')
box[8].append('pants')

# Remove the storm from Box 4
box[4].remove('storm')

# Move the spoon from Box 4 to Box 0
box[0].append('spoon')
box[4].remove('spoon')

# Move the pants and the whistle from Box 8 to Box 10
box[10].append('pants')
box[10].append('whistle')
box[8].remove('pants')
box[8].remove('whistle')

# Put the lightning and the polish into Box 9
box[9].append('lightning')
box[9].append('polish')

# Move the grass from Box 10 to Box 6
box[6].append('grass')
box[10].remove('grass')

# Move the shoe from Box 7 to Box 4
box[4].append('shoe')
box[7].remove('shoe')

# Print the contents of each box
for i in range(11):
    print(f"Box {i}: {box[i]}")