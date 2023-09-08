# Initial state of boxes
boxes = {
    0: ['pants', 'shoe', 'towel'],
    1: ['toaster', 'bowl', 'blender', 'lion', 'coat'],
    2: ['fridge', 'wallet'],
    3: [],
    4: ['comb', 'sculpture'],
    5: ['desert', 'dog', 'lipstick', 'violin'],
    6: ['scarf', 'vase', 'usb'],
    7: ['lock', 'cloud', 'oven', 'meteor', 'fish'],
    8: ['dolphin', 'zipper'],
    9: ['bag', 'microwave'],
    10: ['chair', 'cat', 'bear', 'jungle', 'tie'],
    11: ['crown', 'razor'],
    12: ['leaf', 'magnet', 'tiger', 'moon', 'doll']
}

# Put the fish and the candle into Box 4.
boxes[4].append('fish')
boxes[4].append('candle')

# Replace the sculpture and the comb with the piano and the doll in Box 4.
boxes[4].remove('sculpture')
boxes[4].remove('comb')
boxes[4].append('piano')
boxes[4].append('doll')

# Remove the violin and the lipstick from Box 5.
boxes[5].remove('violin')
boxes[5].remove('lipstick')

# Swap the moon in Box 12 with the oven in Box 7.
boxes[12].remove('moon')
boxes[7].remove('oven')
boxes[12].append('oven')
boxes[7].append('moon')

# Replace the chair with the needle in Box 10.
boxes[10].remove('chair')
boxes[10].append('needle')

# Swap the moon in Box 7 with the fish in Box 4.
boxes[7].remove('moon')
boxes[4].remove('fish')
boxes[7].append('fish')
boxes[4].append('moon')

# Put the cup and the storm into Box 3.
boxes[3].append('cup')
boxes[3].append('storm')

# Move the desert and the dog from Box 5 to Box 8.
boxes[5].remove('desert')
boxes[5].remove('dog')
boxes[8].append('desert')
boxes[8].append('dog')

# Move the crown from Box 11 to Box 1.
boxes[11].remove('crown')
boxes[1].append('crown')

# Put the bicycle into Box 10.
boxes[10].append('bicycle')

# Remove the towel and the shoe from Box 0.
boxes[0].remove('towel')
boxes[0].remove('shoe')

# Move the wallet and the fridge from Box 2 to Box 11.
boxes[2].remove('wallet')
boxes[2].remove('fridge')
boxes[11].append('wallet')
boxes[11].append('fridge')

# Put the shorts into Box 5.
boxes[5].append('shorts')

# Swap the bicycle in Box 10 with the microwave in Box 9.
boxes[10].remove('bicycle')
boxes[9].remove('microwave')
boxes[10].append('microwave')
boxes[9].append('bicycle')

# Replace the coat with the shorts in Box 1.
boxes[1].remove('coat')
boxes[1].append('shorts')

# Put the wallet and the microscope and the card into Box 5.
boxes[5].append('wallet')
boxes[5].append('microscope')
boxes[5].append('card')

# Replace the dolphin and the dog and the desert with the seaweed and the cat and the puzzle in Box 8.
boxes[8].remove('dolphin')
boxes[8].remove('dog')
boxes[8].remove('desert')
boxes[8].append('seaweed')
boxes[8].append('cat')
boxes[8].append('puzzle')

# Put the towel into Box 3.
boxes[3].append('towel')

# Move the oven from Box 12 to Box 7.
boxes[12].remove('oven')
boxes[7].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")