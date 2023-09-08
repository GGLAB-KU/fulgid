# Initial state of boxes
boxes = {
    0: ['scarf', 'wig', 'ring', 'butterfly'],
    1: ['seaweed'],
    2: ['pen', 'grinder', 'table', 'cow', 'bicycle'],
    3: ['plane', 'umbrella', 'bell', 'drum'],
    4: ['mountain'],
    5: ['mirror'],
    6: ['meteor', 'battery', 'telescope'],
    7: ['microwave', 'submarine'],
    8: ['island', 'card', 'helmet', 'usb', 'boat'],
    9: ['motorcycle', 'snow', 'vase'],
    10: ['candle', 'fridge', 'flute', 'wallet']
}

# Move the table from Box 2 to Box 3.
boxes[2].remove('table')
boxes[3].append('table')

# Replace the bell and the umbrella with the bag and the beach in Box 3.
boxes[3].remove('bell')
boxes[3].remove('umbrella')
boxes[3].append('bag')
boxes[3].append('beach')

# Remove the seaweed from Box 1.
boxes[1].remove('seaweed')

# Remove the mountain from Box 4.
boxes[4].remove('mountain')

# Move the usb and the island from Box 8 to Box 3.
boxes[8].remove('usb')
boxes[8].remove('island')
boxes[3].append('usb')
boxes[3].append('island')

# Move the bag from Box 3 to Box 1.
boxes[3].remove('bag')
boxes[1].append('bag')

# Remove the mirror from Box 5.
boxes[5].remove('mirror')

# Move the bag from Box 1 to Box 2.
boxes[1].remove('bag')
boxes[2].append('bag')

# Move the snow from Box 9 to Box 5.
boxes[9].remove('snow')
boxes[5].append('snow')

# Move the usb from Box 3 to Box 2.
boxes[3].remove('usb')
boxes[2].append('usb')

# Remove the ring from Box 0.
boxes[0].remove('ring')

# Swap the drum in Box 3 with the wig in Box 0.
boxes[3].remove('drum')
boxes[0].remove('wig')
boxes[3].append('wig')
boxes[0].append('drum')

# Replace the helmet with the wire in Box 8.
boxes[8].remove('helmet')
boxes[8].append('wire')

# Replace the motorcycle and the vase with the mirror and the coat in Box 9.
boxes[9].remove('motorcycle')
boxes[9].remove('vase')
boxes[9].append('mirror')
boxes[9].append('coat')

# Remove the microwave from Box 7.
boxes[7].remove('microwave')

# Put the rock and the pot into Box 7.
boxes[7].append('rock')
boxes[7].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")