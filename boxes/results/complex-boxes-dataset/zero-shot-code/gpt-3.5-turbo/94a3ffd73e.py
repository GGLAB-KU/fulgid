box_0 = ['forest', 'tiger', 'shoe', 'towel', 'wallet']
box_1 = ['bus', 'seaweed', 'rocket', 'speaker', 'river']
box_2 = []
box_3 = ['plane', 'horn', 'mountain', 'laptop', 'button']
box_4 = ['bear', 'necklace']
box_5 = ['shelf', 'game', 'starfish', 'glove']
box_6 = []
box_7 = ['note', 'motorcycle', 'boat', 'perfume']
box_8 = ['coat', 'pot', 'bell', 'comb']
box_9 = ['console']
box_10 = ['coral', 'chair', 'jacket', 'sock']
box_11 = ['belt', 'glasses']
box_12 = ['jungle', 'ring', 'horse', 'polish', 'ocean']

# Replace the console with the cat in Box 9
box_9.remove('console')
box_9.append('cat')

# Move the glasses from Box 11 to Box 0
box_0.append(box_11.pop())

# Remove the jungle and the ocean and the ring from Box 12
box_12.remove('jungle')
box_12.remove('ocean')
box_12.remove('ring')

# Move the cat from Box 9 to Box 1
box_1.append(box_9.pop())

# Remove the glove from Box 5
box_5.remove('glove')

# Empty Box 0
box_0.clear()

# Move the pot and the coat and the comb from Box 8 to Box 6
box_6.extend([box_8.pop(), box_8.pop(), box_8.pop()])

# Replace the boat and the note and the perfume with the bowl and the candle and the bear in Box 7
box_7.remove('boat')
box_7.remove('note')
box_7.remove('perfume')
box_7.extend(['bowl', 'candle', 'bear'])

# Put the guitar and the toothpaste and the star into Box 4
box_4.extend(['guitar', 'toothpaste', 'star'])

# Put the hat and the crown and the flute into Box 3
box_3.extend(['hat', 'crown', 'flute'])

# Replace the polish and the horse with the planet and the glove in Box 12
box_12.remove('polish')
box_12.remove('horse')
box_12.extend(['planet', 'glove'])

# Put the chair and the magnet and the bracelet into Box 4
box_4.extend(['chair', 'magnet', 'bracelet'])

# Put the sculpture into Box 9
box_9.append('sculpture')

# Move the belt from Box 11 to Box 1
box_1.append(box_11.pop())

# Put the plate into Box 9
box_9.append('plate')

# Replace the shelf with the speaker in Box 5
box_5.remove('shelf')
box_5.append('speaker')

# Move the comb and the pot from Box 6 to Box 8
box_8.extend([box_6.pop(), box_6.pop()])

# Move the starfish and the game from Box 5 to Box 11
box_11.extend([box_5.pop(), box_5.pop()])

# Replace the magnet with the controller in Box 4
box_4.remove('magnet')
box_4.append('controller')

# Print the contents of each box
boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")