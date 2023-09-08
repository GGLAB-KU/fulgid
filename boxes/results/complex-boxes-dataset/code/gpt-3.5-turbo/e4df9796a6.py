# Initial state of boxes
boxes = {
    0: ['lion', 'wallet', 'violin', 'bell'],
    1: ['grass', 'tie', 'sun', 'umbrella'],
    2: ['plane', 'console', 'ship', 'charger', 'desert'],
    3: ['bowl', 'towel'],
    4: ['perfume', 'butterfly', 'island', 'book', 'crown'],
    5: ['submarine', 'clock', 'glasses', 'keyboard'],
    6: ['river', 'wig', 'pan'],
    7: ['comet', 'pillow', 'leaf', 'phone', 'cow']
}

# Swap the glasses in Box 5 with the violin in Box 0.
boxes[0].remove('violin')
boxes[5].remove('glasses')
boxes[0].append('glasses')
boxes[5].append('violin')

# Swap the violin in Box 5 with the desert in Box 2.
boxes[2].remove('desert')
boxes[5].remove('violin')
boxes[2].append('violin')
boxes[5].append('desert')

# Replace the sun and the umbrella and the tie with the plate and the ring and the pot in Box 1.
boxes[1].remove('sun')
boxes[1].remove('umbrella')
boxes[1].remove('tie')
boxes[1].append('plate')
boxes[1].append('ring')
boxes[1].append('pot')

# Swap the bowl in Box 3 with the desert in Box 5.
boxes[3].remove('bowl')
boxes[5].remove('desert')
boxes[3].append('desert')
boxes[5].append('bowl')

# Remove the island from Box 4.
boxes[4].remove('island')

# Replace the crown and the book and the perfume with the shelf and the wallet and the coin in Box 4.
boxes[4].remove('crown')
boxes[4].remove('book')
boxes[4].remove('perfume')
boxes[4].append('shelf')
boxes[4].append('wallet')
boxes[4].append('coin')

# Remove the wig and the river from Box 6.
boxes[6].remove('wig')
boxes[6].remove('river')

# Replace the violin and the plane with the grinder and the toothpaste in Box 2.
boxes[2].remove('violin')
boxes[2].remove('plane')
boxes[2].append('grinder')
boxes[2].append('toothpaste')

# Replace the towel with the whistle in Box 3.
boxes[3].remove('towel')
boxes[3].append('whistle')

# Put the coat and the candle and the razor into Box 0.
items_to_put = ['coat', 'candle', 'razor']
for item in items_to_put:
    boxes[0].append(item)

# Replace the shelf and the coin with the dice and the elephant in Box 4.
boxes[4].remove('shelf')
boxes[4].remove('coin')
boxes[4].append('dice')
boxes[4].append('elephant')

# Swap the grinder in Box 2 with the grass in Box 1.
boxes[1].remove('grass')
boxes[2].remove('grinder')
boxes[1].append('grinder')
boxes[2].append('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")