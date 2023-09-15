box_0 = ['butterfly', 'shoes', 'shark']
box_1 = ['tie', 'note', 'towel', 'thread']
box_2 = ['doll', 'telescope', 'necklace', 'violin']
box_3 = ['mask', 'whistle', 'shelf', 'boat']
box_4 = []
box_5 = ['lipstick', 'chair', 'watch']
box_6 = []
box_7 = ['flute', 'cup']
box_8 = ['phone', 'submarine', 'beach']
box_9 = ['rain']
box_10 = ['swimsuit', 'polish']
box_11 = ['candle', 'table', 'glove', 'island']
box_12 = ['rocket', 'elephant', 'razor', 'speaker', 'umbrella']
box_13 = ['zipper', 'needle']
box_14 = []

# Replace the needle with the toothpaste in Box 13
box_13.remove('needle')
box_13.append('toothpaste')

# Swap the flute in Box 7 with the shark in Box 0
box_0.remove('shark')
box_0.append('flute')
box_7.remove('flute')
box_7.append('shark')

# Move the towel from Box 1 to Box 5
box_1.remove('towel')
box_5.append('towel')

# Move the tie and the note and the thread from Box 1 to Box 2
box_1.remove('tie')
box_1.remove('note')
box_1.remove('thread')
box_2.append('tie')
box_2.append('note')
box_2.append('thread')

# Put the bracelet and the sculpture into Box 6
box_6.append('bracelet')
box_6.append('sculpture')

# Swap the umbrella in Box 12 with the sculpture in Box 6
box_12.remove('umbrella')
box_12.append('sculpture')
box_6.remove('sculpture')
box_6.append('umbrella')

# Swap the towel in Box 5 with the umbrella in Box 6
box_5.remove('towel')
box_5.append('umbrella')
box_6.remove('umbrella')
box_6.append('towel')

# Move the shoes and the flute from Box 0 to Box 9
box_0.remove('shoes')
box_0.remove('flute')
box_9.append('shoes')
box_9.append('flute')

# Replace the watch with the camera in Box 5
box_5.remove('watch')
box_5.append('camera')

# Move the glove from Box 11 to Box 12
box_11.remove('glove')
box_12.append('glove')

# Move the table and the candle from Box 11 to Box 5
box_11.remove('table')
box_11.remove('candle')
box_5.append('table')
box_5.append('candle')

# Swap the cup in Box 7 with the island in Box 11
box_7.remove('cup')
box_7.append('island')
box_11.remove('island')
box_11.append('cup')

# Remove the cup from Box 11
box_11.remove('cup')

# Empty Box 0
box_0.clear()

# Replace the zipper and the toothpaste with the tree and the spoon in Box 13
box_13.remove('zipper')
box_13.remove('toothpaste')
box_13.append('tree')
box_13.append('spoon')

# Move the chair and the umbrella from Box 5 to Box 1
box_5.remove('chair')
box_5.remove('umbrella')
box_1.append('chair')
box_1.append('umbrella')

# Put the flower and the mirror into Box 1
box_1.append('flower')
box_1.append('mirror')

# Remove the swimsuit and the polish from Box 10
box_10.remove('swimsuit')
box_10.remove('polish')

# Swap the shark in Box 7 with the flute in Box 9
box_7.remove('shark')
box_7.append('flute')
box_9.remove('flute')
box_9.append('shark')

# Put the tape and the planet into Box 8
box_8.append('tape')
box_8.append('planet')

# Empty Box 13
box_13.clear()

# Swap the flute in Box 7 with the rain in Box 9
box_7.remove('flute')
box_7.append('rain')
box_9.remove('rain')
box_9.append('flute')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)
print("Box 13:", box_13)
print("Box 14:", box_14)