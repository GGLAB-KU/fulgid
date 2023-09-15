box_0 = ['toothbrush', 'bus']
box_1 = ['wig', 'fork', 'candle', 'swimsuit', 'key']
box_2 = ['umbrella', 'blanket', 'pot']
box_3 = ['rocket', 'frame']
box_4 = []
box_5 = ['rock', 'controller', 'planet']
box_6 = ['elephant', 'game', 'moon', 'shelf', 'shirt']
box_7 = ['perfume']
box_8 = []
box_9 = ['note', 'necklace', 'pan', 'console']
box_10 = ['horn', 'river', 'wallet']
box_11 = ['mask', 'glove', 'drum', 'razor', 'dress']
box_12 = ['lightning', 'bird']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

# Move the frame from Box 3 to Box 0
box_0.append(box_3.pop(box_3.index('frame')))

# Swap the wallet in Box 10 with the drum in Box 11
box_10[box_10.index('wallet')], box_11[box_11.index('drum')] = box_11[box_11.index('drum')], box_10[box_10.index('wallet')]

# Empty Box 0
box_0 = []

# Replace the controller and the rock and the planet with the bag and the river and the fridge in Box 5
box_5 = ['bag', 'river', 'fridge']

# Remove the bag and the fridge from Box 5
box_5 = []

# Move the river from Box 5 to Box 7
box_7.append(box_5.pop(box_5.index('river')))

# Remove the horn from Box 10
box_10.remove('horn')

# Move the bird and the lightning from Box 12 to Box 4
box_4.extend([box_12.pop(box_12.index('bird')), box_12.pop(box_12.index('lightning'))])

# Put the keyboard and the charger and the boat into Box 6
box_6.extend(['keyboard', 'charger', 'boat'])

# Move the rocket from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('rocket')))

# Replace the river with the fish in Box 7
box_7[box_7.index('river')] = 'fish'

# Remove the keyboard from Box 6
box_6.remove('keyboard')

# Replace the wig and the key and the candle with the bracelet and the spoon and the mountain in Box 1
box_1 = ['bracelet', 'spoon', 'mountain']

# Put the soap into Box 7
box_7.append('soap')

# Remove the dress and the razor and the mask from Box 11
box_11.remove('dress')
box_11.remove('razor')
box_11.remove('mask')

# Swap the mountain in Box 1 with the perfume in Box 7
box_1[box_1.index('mountain')], box_7[box_7.index('perfume')] = box_7[box_7.index('perfume')], box_1[box_1.index('mountain')]

# Swap the spoon in Box 1 with the shirt in Box 6
box_1[box_1.index('spoon')], box_6[box_6.index('shirt')] = box_6[box_6.index('shirt')], box_1[box_1.index('spoon')]

# Move the perfume and the bracelet and the fork from Box 1 to Box 9
box_9.extend([box_1.pop(box_1.index('perfume')), box_1.pop(box_1.index('bracelet')), box_1.pop(box_1.index('fork'))])

# Move the drum from Box 10 to Box 3
box_3.append(box_10.pop(box_10.index('drum')))

# Remove the bird from Box 4
box_4.remove('bird')

print_boxes()