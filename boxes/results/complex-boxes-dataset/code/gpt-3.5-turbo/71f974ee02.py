# Initial state of boxes
boxes = {
    0: ['bird', 'key', 'jacket'],
    1: [],
    2: ['tree', 'shark', 'lipstick'],
    3: ['candle'],
    4: ['storm', 'wallet', 'scissors'],
    5: ['boot', 'paint'],
    6: ['comb', 'pillow'],
    7: [],
    8: ['tie'],
    9: [],
    10: ['crown', 'elephant'],
    11: ['headphone', 'snow', 'console', 'comet', 'violin'],
    12: ['polish', 'truck', 'butterfly', 'battery'],
    13: ['horn'],
    14: ['bus', 'mixer', 'frame', 'dice']
}

# Swap the horn in Box 13 with the candle in Box 3.
boxes[13].remove('horn')
boxes[3].remove('candle')
boxes[13].append('candle')
boxes[3].append('horn')

# Remove the pillow and the comb from Box 6.
boxes[6].remove('pillow')
boxes[6].remove('comb')

# Empty Box 4.
boxes[4] = []

# Remove the horn from Box 3.
boxes[3].remove('horn')

# Remove the battery and the truck from Box 12.
boxes[12].remove('battery')
boxes[12].remove('truck')

# Put the jacket and the shark into Box 7.
boxes[7].append('jacket')
boxes[7].append('shark')

# Remove the boot and the paint from Box 5.
boxes[5].remove('boot')
boxes[5].remove('paint')

# Empty Box 2.
boxes[2] = []

# Remove the shark and the jacket from Box 7.
boxes[7].remove('shark')
boxes[7].remove('jacket')

# Empty Box 14.
boxes[14] = []

# Remove the candle from Box 13.
boxes[13].remove('candle')

# Move the tie from Box 8 to Box 3.
boxes[8].remove('tie')
boxes[3].append('tie')

# Replace the tie with the wig in Box 3.
boxes[3].remove('tie')
boxes[3].append('wig')

# Replace the butterfly and the polish with the usb and the necklace in Box 12.
boxes[12].remove('butterfly')
boxes[12].remove('polish')
boxes[12].append('usb')
boxes[12].append('necklace')

# Replace the wig with the coin in Box 3.
boxes[3].remove('wig')
boxes[3].append('coin')

# Remove the coin from Box 3.
boxes[3].remove('coin')

# Swap the headphone in Box 11 with the necklace in Box 12.
boxes[11].remove('headphone')
boxes[12].remove('necklace')
boxes[11].append('necklace')
boxes[12].append('headphone')

# Move the key from Box 0 to Box 14.
boxes[0].remove('key')
boxes[14].append('key')

# Remove the comet and the snow from Box 11.
boxes[11].remove('comet')
boxes[11].remove('snow')

# Replace the console with the zipper in Box 11.
boxes[11].remove('console')
boxes[11].append('zipper')

# Remove the bird and the jacket from Box 0.
boxes[0].remove('bird')
boxes[0].remove('jacket')

# Remove the usb and the headphone from Box 12.
boxes[12].remove('usb')
boxes[12].remove('headphone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")