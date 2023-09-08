# Initial state of boxes
boxes = {
    0: [],
    1: ['wallet'],
    2: [],
    3: ['scarf', 'bracelet', 'coin', 'guitar', 'island'],
    4: ['shoes', 'apple', 'pants', 'submarine'],
    5: [],
    6: ['glove', 'shelf', 'vase', 'dog'],
    7: ['sun', 'tiger', 'doll'],
    8: ['bell', 'beach', 'zipper', 'candle'],
    9: ['wig', 'horse', 'coral']
}

# Move the glove and the dog from Box 6 to Box 3.
boxes[6].remove('glove')
boxes[6].remove('dog')
boxes[3].append('glove')
boxes[3].append('dog')

# Replace the guitar and the scarf and the glove with the octopus and the mountain and the game in Box 3.
boxes[3].remove('guitar')
boxes[3].remove('scarf')
boxes[3].remove('glove')
boxes[3].append('octopus')
boxes[3].append('mountain')
boxes[3].append('game')

# Put the wire and the mask into Box 7.
boxes[7].append('wire')
boxes[7].append('mask')

# Empty Box 6.
boxes[6] = []

# Put the violin into Box 3.
boxes[3].append('violin')

# Move the pants from Box 4 to Box 9.
boxes[4].remove('pants')
boxes[9].append('pants')

# Replace the pants with the rain in Box 9.
boxes[9].remove('pants')
boxes[9].append('rain')

# Swap the horse in Box 9 with the shoes in Box 4.
boxes[9].remove('horse')
boxes[4].remove('shoes')
boxes[9].append('shoes')
boxes[4].append('horse')

# Remove the horse and the apple from Box 4.
boxes[4].remove('horse')
boxes[4].remove('apple')

# Replace the island with the fridge in Box 3.
boxes[3].remove('island')
boxes[3].append('fridge')

# Put the scarf and the branch into Box 0.
boxes[0].append('scarf')
boxes[0].append('branch')

# Remove the bell and the beach from Box 8.
boxes[8].remove('bell')
boxes[8].remove('beach')

# Move the candle from Box 8 to Box 9.
boxes[8].remove('candle')
boxes[9].append('candle')

# Replace the wallet with the sock in Box 1.
boxes[1].remove('wallet')
boxes[1].append('sock')

# Put the shoes and the mountain into Box 0.
boxes[0].append('shoes')
boxes[0].append('mountain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")