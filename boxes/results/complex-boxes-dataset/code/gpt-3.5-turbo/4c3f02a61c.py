# Initial state of boxes
boxes = {
    0: ['bird', 'umbrella'],
    1: ['violin', 'towel', 'beach'],
    2: ['desert', 'glasses', 'submarine', 'coral'],
    3: ['swimsuit', 'zipper'],
    4: ['plate', 'thunder', 'glove'],
    5: ['toaster'],
    6: ['bag', 'tape'],
    7: ['piano', 'wallet'],
    8: ['microscope', 'jacket', 'rock', 'mask', 'cloud'],
    9: ['shelf', 'butterfly', 'clock', 'paint'],
    10: ['candle', 'harmonica', 'shark'],
    11: ['whistle'],
    12: ['sculpture', 'brush', 'grass', 'guitar'],
    13: ['bus', 'sock'],
    14: ['usb']
}

# Replace the usb with the scarf in Box 14.
boxes[14].remove('usb')
boxes[14].append('scarf')

# Swap the butterfly in Box 9 with the grass in Box 12.
boxes[9].remove('butterfly')
boxes[12].remove('grass')
boxes[9].append('grass')
boxes[12].append('butterfly')

# Put the leaf into Box 11.
boxes[11].append('leaf')

# Replace the sculpture with the needle in Box 12.
boxes[12].remove('sculpture')
boxes[12].append('needle')

# Replace the shark and the candle and the harmonica with the pants and the necklace and the rain in Box 10.
boxes[10].remove('shark')
boxes[10].remove('candle')
boxes[10].remove('harmonica')
boxes[10].append('pants')
boxes[10].append('necklace')
boxes[10].append('rain')

# Swap the wallet in Box 7 with the grass in Box 9.
boxes[7].remove('wallet')
boxes[9].remove('grass')
boxes[7].append('grass')
boxes[9].append('wallet')

# Put the wallet and the cloud and the lightning into Box 7.
boxes[7].append('wallet')
boxes[7].append('cloud')
boxes[7].append('lightning')

# Swap the scarf in Box 14 with the bag in Box 6.
boxes[14].remove('scarf')
boxes[6].remove('bag')
boxes[14].append('bag')
boxes[6].append('scarf')

# Swap the toaster in Box 5 with the bag in Box 14.
boxes[5].remove('toaster')
boxes[14].remove('bag')
boxes[5].append('bag')
boxes[14].append('toaster')

# Replace the brush with the necklace in Box 12.
boxes[12].remove('brush')
boxes[12].append('necklace')

# Remove the cloud and the mask and the jacket from Box 8.
boxes[8].remove('cloud')
boxes[8].remove('mask')
boxes[8].remove('jacket')

# Put the battery and the charger and the grass into Box 12.
boxes[12].append('battery')
boxes[12].append('charger')
boxes[12].append('grass')

# Put the wallet into Box 13.
boxes[13].append('wallet')

# Remove the scarf from Box 6.
boxes[6].remove('scarf')

# Swap the microscope in Box 8 with the plate in Box 4.
boxes[8].remove('microscope')
boxes[4].remove('plate')
boxes[8].append('plate')
boxes[4].append('microscope')

# Replace the butterfly and the needle and the charger with the bus and the soap and the umbrella in Box 12.
boxes[12].remove('butterfly')
boxes[12].remove('needle')
boxes[12].remove('charger')
boxes[12].append('bus')
boxes[12].append('soap')
boxes[12].append('umbrella')

# Swap the beach in Box 1 with the umbrella in Box 0.
boxes[1].remove('beach')
boxes[0].remove('umbrella')
boxes[1].append('umbrella')
boxes[0].append('beach')

# Put the ocean and the cat and the vase into Box 14.
boxes[14].append('ocean')
boxes[14].append('cat')
boxes[14].append('vase')

# Put the tiger into Box 12.
boxes[12].append('tiger')

# Put the card and the shoe and the usb into Box 1.
boxes[1].append('card')
boxes[1].append('shoe')
boxes[1].append('usb')

# Remove the microscope and the thunder and the glove from Box 4.
boxes[4].remove('microscope')
boxes[4].remove('thunder')
boxes[4].remove('glove')

# Swap the wallet in Box 13 with the cloud in Box 7.
boxes[13].remove('wallet')
boxes[7].remove('cloud')
boxes[13].append('cloud')
boxes[7].append('wallet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")