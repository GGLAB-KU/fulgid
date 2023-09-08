# Initial state of boxes
boxes = {
    0: ['wire', 'fridge'],
    1: [],
    2: [],
    3: [],
    4: [],
    5: ['piano', 'cloud', 'car'],
    6: [],
    7: ['dolphin', 'butterfly', 'oven', 'guitar', 'lightning'],
    8: ['pan', 'coat', 'comet', 'harmonica', 'desert'],
    9: ['horn', 'bear', 'seaweed']
}

# Swap the butterfly in Box 7 with the bear in Box 9.
boxes[7].remove('butterfly')
boxes[9].remove('bear')
boxes[7].append('bear')
boxes[9].append('butterfly')

# Put the book and the island and the moon into Box 7.
boxes[7].extend(['book', 'island', 'moon'])

# Empty Box 7.
boxes[7] = []

# Swap the fridge in Box 0 with the coat in Box 8.
boxes[0].remove('fridge')
boxes[8].remove('coat')
boxes[0].append('coat')
boxes[8].append('fridge')

# Move the fridge from Box 8 to Box 6.
boxes[8].remove('fridge')
boxes[6].append('fridge')

# Swap the cloud in Box 5 with the butterfly in Box 9.
boxes[5].remove('cloud')
boxes[9].remove('butterfly')
boxes[5].append('butterfly')
boxes[9].append('cloud')

# Replace the comet and the harmonica with the plane and the basket in Box 8.
boxes[8].remove('comet')
boxes[8].remove('harmonica')
boxes[8].append('plane')
boxes[8].append('basket')

# Replace the wire and the coat with the lion and the earring in Box 0.
boxes[0].remove('wire')
boxes[0].remove('coat')
boxes[0].append('lion')
boxes[0].append('earring')

# Replace the fridge with the cloud in Box 6.
boxes[6].remove('fridge')
boxes[6].append('cloud')

# Swap the desert in Box 8 with the earring in Box 0.
boxes[8].remove('desert')
boxes[0].remove('earring')
boxes[8].append('earring')
boxes[0].append('desert')

# Put the coat and the glasses into Box 5.
boxes[5].extend(['coat', 'glasses'])

# Move the plane and the pan from Box 8 to Box 1.
boxes[8].remove('plane')
boxes[8].remove('pan')
boxes[1].extend(['plane', 'pan'])

# Put the comb into Box 7.
boxes[7].append('comb')

# Replace the comb with the pen in Box 7.
boxes[7].remove('comb')
boxes[7].append('pen')

# Replace the cloud with the pot in Box 6.
boxes[6].remove('cloud')
boxes[6].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")