# Initial state of boxes
boxes = {
    0: ['vase', 'wallet'],
    1: ['coin', 'puzzle', 'ship', 'bell', 'keyboard'],
    2: ['console', 'scarf'],
    3: [],
    4: ['cup'],
    5: [],
    6: ['thread', 'dice', 'flute', 'grinder', 'leaf'],
    7: ['grass', 'cat', 'gloves', 'comb', 'mirror'],
    8: ['fish'],
    9: [],
    10: ['horn', 'magnet', 'usb', 'comet', 'crown']
}

# Move the console from Box 2 to Box 4.
boxes[2].remove('console')
boxes[4].append('console')

# Move the fish from Box 8 to Box 2.
boxes[8].remove('fish')
boxes[2].append('fish')

# Remove the scarf and the fish from Box 2.
boxes[2].remove('scarf')
boxes[2].remove('fish')

# Put the speaker and the ring into Box 5.
boxes[5].append('speaker')
boxes[5].append('ring')

# Replace the ship and the puzzle and the coin with the desert and the lamp and the lipstick in Box 1.
boxes[1].remove('ship')
boxes[1].remove('puzzle')
boxes[1].remove('coin')
boxes[1].append('desert')
boxes[1].append('lamp')
boxes[1].append('lipstick')

# Move the ring and the speaker from Box 5 to Box 10.
boxes[5].remove('ring')
boxes[5].remove('speaker')
boxes[10].append('ring')
boxes[10].append('speaker')

# Put the pants into Box 0.
boxes[0].append('pants')

# Swap the console in Box 4 with the magnet in Box 10.
boxes[4].remove('console')
boxes[10].remove('magnet')
boxes[4].append('magnet')
boxes[10].append('console')

# Replace the gloves with the jacket in Box 7.
boxes[7].remove('gloves')
boxes[7].append('jacket')

# Move the leaf and the grinder from Box 6 to Box 8.
boxes[6].remove('leaf')
boxes[6].remove('grinder')
boxes[8].append('leaf')
boxes[8].append('grinder')

# Swap the horn in Box 10 with the leaf in Box 8.
boxes[10].remove('horn')
boxes[8].remove('leaf')
boxes[10].append('leaf')
boxes[8].append('horn')

# Put the violin into Box 5.
boxes[5].append('violin')

# Swap the pants in Box 0 with the grass in Box 7.
boxes[0].remove('pants')
boxes[7].remove('grass')
boxes[0].append('grass')
boxes[7].append('pants')

# Move the lamp from Box 1 to Box 8.
boxes[1].remove('lamp')
boxes[8].append('lamp')

# Remove the violin from Box 5.
boxes[5].remove('violin')

# Replace the wallet and the grass and the vase with the charger and the usb and the toothpaste in Box 0.
boxes[0].remove('wallet')
boxes[0].remove('grass')
boxes[0].remove('vase')
boxes[0].append('charger')
boxes[0].append('usb')
boxes[0].append('toothpaste')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")