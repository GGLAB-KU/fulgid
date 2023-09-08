# Initial state of boxes
boxes = {
    0: ['blanket'],
    1: ['paint'],
    2: ['speaker', 'crown', 'ship', 'wallet', 'harmonica'],
    3: ['lipstick', 'toothpaste', 'submarine', 'perfume', 'truck'],
    4: ['table'],
    5: ['fish', 'controller', 'pants', 'forest', 'motorcycle'],
    6: ['leaf', 'lightning'],
    7: ['bell', 'soap', 'necklace', 'jacket', 'plane'],
    8: ['microwave', 'frame', 'candle', 'thunder']
}

# Remove the table from Box 4.
boxes[4].remove('table')

# Move the paint from Box 1 to Box 8.
boxes[1].remove('paint')
boxes[8].append('paint')

# Move the crown and the speaker and the wallet from Box 2 to Box 0.
items_to_move = ['crown', 'speaker', 'wallet']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the microwave in Box 8 with the necklace in Box 7.
boxes[8].remove('microwave')
boxes[7].remove('necklace')
boxes[8].append('necklace')
boxes[7].append('microwave')

# Swap the necklace in Box 8 with the speaker in Box 0.
boxes[8].remove('necklace')
boxes[0].remove('speaker')
boxes[8].append('speaker')
boxes[0].append('necklace')

# Remove the harmonica and the ship from Box 2.
boxes[2].remove('harmonica')
boxes[2].remove('ship')

# Replace the fish with the sun in Box 5.
boxes[5].remove('fish')
boxes[5].append('sun')

# Replace the lipstick with the seaweed in Box 3.
boxes[3].remove('lipstick')
boxes[3].append('seaweed')

# Remove the lightning and the leaf from Box 6.
boxes[6].remove('lightning')
boxes[6].remove('leaf')

# Replace the seaweed and the submarine and the toothpaste with the hat and the wallet and the zipper in Box 3.
boxes[3].remove('seaweed')
boxes[3].remove('submarine')
boxes[3].remove('toothpaste')
boxes[3].append('hat')
boxes[3].append('wallet')
boxes[3].append('zipper')

# Move the candle and the paint from Box 8 to Box 7.
boxes[8].remove('candle')
boxes[8].remove('paint')
boxes[7].append('candle')
boxes[7].append('paint')

# Swap the controller in Box 5 with the microwave in Box 7.
boxes[5].remove('controller')
boxes[7].remove('microwave')
boxes[5].append('microwave')
boxes[7].append('controller')

# Swap the frame in Box 8 with the perfume in Box 3.
boxes[8].remove('frame')
boxes[3].remove('perfume')
boxes[8].append('perfume')
boxes[3].append('frame')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")