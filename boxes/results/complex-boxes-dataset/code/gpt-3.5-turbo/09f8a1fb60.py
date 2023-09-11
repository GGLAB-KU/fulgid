# Initial state of boxes
boxes = {
    0: ['crown'],
    1: ['toothbrush', 'rain'],
    2: ['shorts', 'magnet', 'plane', 'comb', 'mountain'],
    3: ['octopus', 'soap'],
    4: ['horn', 'razor', 'glove'],
    5: ['seaweed', 'wire', 'dog'],
    6: ['fork', 'note'],
    7: ['butterfly', 'perfume', 'boat', 'train', 'jacket'],
    8: ['coin', 'belt', 'jungle', 'shampoo']
}

# Put the towel and the umbrella and the planet into Box 0.
boxes[0].extend(['towel', 'umbrella', 'planet'])

# Replace the boat and the jacket with the speaker and the motorcycle in Box 7.
boxes[7].remove('boat')
boxes[7].remove('jacket')
boxes[7].append('speaker')
boxes[7].append('motorcycle')

# Empty Box 2.
boxes[2] = []

# Remove the umbrella and the planet from Box 0.
boxes[0].remove('umbrella')
boxes[0].remove('planet')

# Move the note from Box 6 to Box 7.
boxes[6].remove('note')
boxes[7].append('note')

# Move the fork from Box 6 to Box 1.
boxes[6].remove('fork')
boxes[1].append('fork')

# Put the comet and the book and the sculpture into Box 7.
boxes[7].extend(['comet', 'book', 'sculpture'])

# Put the starfish and the submarine and the sun into Box 7.
boxes[7].extend(['starfish', 'submarine', 'sun'])

# Put the meteor and the sandals into Box 3.
boxes[3].extend(['meteor', 'sandals'])

# Swap the horn in Box 4 with the book in Box 7.
boxes[4].remove('horn')
boxes[7].remove('book')
boxes[4].append('book')
boxes[7].append('horn')

# Swap the jungle in Box 8 with the razor in Box 4.
boxes[8].remove('jungle')
boxes[4].remove('razor')
boxes[8].append('razor')
boxes[4].append('jungle')

# Swap the meteor in Box 3 with the wire in Box 5.
boxes[3].remove('meteor')
boxes[5].remove('wire')
boxes[3].append('wire')
boxes[5].append('meteor')

# Remove the rain from Box 1.
boxes[1].remove('rain')

# Swap the jungle in Box 4 with the towel in Box 0.
boxes[4].remove('jungle')
boxes[0].remove('towel')
boxes[4].append('towel')
boxes[0].append('jungle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")