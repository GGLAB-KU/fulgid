# Initial state of boxes
boxes = {
    0: ['toothbrush', 'bus'],
    1: ['wig', 'fork', 'candle', 'swimsuit', 'key'],
    2: ['umbrella', 'blanket', 'pot'],
    3: ['rocket', 'frame'],
    4: [],
    5: ['rock', 'controller', 'planet'],
    6: ['elephant', 'game', 'moon', 'shelf', 'shirt'],
    7: ['perfume'],
    8: [],
    9: ['note', 'necklace', 'pan', 'console'],
    10: ['horn', 'river', 'wallet'],
    11: ['mask', 'glove', 'drum', 'razor', 'dress'],
    12: ['lightning', 'bird']
}

# Move the frame from Box 3 to Box 0.
boxes[3].remove('frame')
boxes[0].append('frame')

# Swap the wallet in Box 10 with the drum in Box 11.
boxes[10].remove('wallet')
boxes[11].remove('drum')
boxes[10].append('drum')
boxes[11].append('wallet')

# Empty Box 0.
boxes[0] = []

# Replace the controller and the rock and the planet with the bag and the river and the fridge in Box 5.
boxes[5].remove('controller')
boxes[5].remove('rock')
boxes[5].remove('planet')
boxes[5].append('bag')
boxes[5].append('river')
boxes[5].append('fridge')

# Remove the bag and the fridge from Box 5.
boxes[5].remove('bag')
boxes[5].remove('fridge')

# Move the river from Box 5 to Box 7.
boxes[5].remove('river')
boxes[7].append('river')

# Remove the horn from Box 10.
boxes[10].remove('horn')

# Move the bird and the lightning from Box 12 to Box 4.
boxes[12].remove('bird')
boxes[12].remove('lightning')
boxes[4].append('bird')
boxes[4].append('lightning')

# Put the keyboard and the charger and the boat into Box 6.
boxes[6].append('keyboard')
boxes[6].append('charger')
boxes[6].append('boat')

# Move the rocket from Box 3 to Box 7.
boxes[3].remove('rocket')
boxes[7].append('rocket')

# Replace the river with the fish in Box 7.
boxes[7].remove('river')
boxes[7].append('fish')

# Remove the keyboard from Box 6.
boxes[6].remove('keyboard')

# Replace the wig and the key and the candle with the bracelet and the spoon and the mountain in Box 1.
boxes[1].remove('wig')
boxes[1].remove('key')
boxes[1].remove('candle')
boxes[1].append('bracelet')
boxes[1].append('spoon')
boxes[1].append('mountain')

# Put the soap into Box 7.
boxes[7].append('soap')

# Remove the dress and the razor and the mask from Box 11.
boxes[11].remove('dress')
boxes[11].remove('razor')
boxes[11].remove('mask')

# Swap the mountain in Box 1 with the perfume in Box 7.
boxes[1].remove('mountain')
boxes[7].remove('perfume')
boxes[1].append('perfume')
boxes[7].append('mountain')

# Swap the spoon in Box 1 with the shirt in Box 6.
boxes[1].remove('spoon')
boxes[6].remove('shirt')
boxes[1].append('shirt')
boxes[6].append('spoon')

# Move the perfume and the bracelet and the fork from Box 1 to Box 9.
boxes[1].remove('perfume')
boxes[1].remove('bracelet')
boxes[1].remove('fork')
boxes[9].append('perfume')
boxes[9].append('bracelet')
boxes[9].append('fork')

# Move the drum from Box 10 to Box 3.
boxes[10].remove('drum')
boxes[3].append('drum')

# Remove the bird from Box 4.
boxes[4].remove('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")