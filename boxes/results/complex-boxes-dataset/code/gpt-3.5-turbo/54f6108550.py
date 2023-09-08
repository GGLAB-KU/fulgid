# Initial state of boxes
boxes = {
    0: ['paint', 'polish'],
    1: ['brush', 'pan', 'soap', 'cloud', 'coin'],
    2: ['gloves', 'apple', 'motorcycle', 'branch', 'bicycle'],
    3: ['shark', 'plane'],
    4: [],
    5: ['plate', 'shampoo', 'necklace', 'fridge', 'seaweed'],
    6: ['coral', 'grinder', 'drum', 'headphone'],
    7: ['key', 'mountain', 'pants'],
    8: ['shoe', 'harmonica', 'earring', 'comb'],
    9: ['starfish', 'bell'],
    10: ['island', 'charger', 'cat', 'fork'],
    11: [],
    12: []
}

# Swap the pan in Box 1 with the pants in Box 7.
boxes[1].remove('pan')
boxes[7].remove('pants')
boxes[1].append('pants')
boxes[7].append('pan')

# Replace the apple and the gloves and the bicycle with the belt and the perfume and the plate in Box 2.
boxes[2].remove('apple')
boxes[2].remove('gloves')
boxes[2].remove('bicycle')
boxes[2].append('belt')
boxes[2].append('perfume')
boxes[2].append('plate')

# Move the shampoo from Box 5 to Box 9.
boxes[5].remove('shampoo')
boxes[9].append('shampoo')

# Put the fish and the elephant and the dice into Box 2.
boxes[2].append('fish')
boxes[2].append('elephant')
boxes[2].append('dice')

# Swap the dice in Box 2 with the shampoo in Box 9.
boxes[2].remove('dice')
boxes[9].remove('shampoo')
boxes[2].append('shampoo')
boxes[9].append('dice')

# Replace the branch and the plate and the elephant with the storm and the moon and the tape in Box 2.
boxes[2].remove('branch')
boxes[2].remove('plate')
boxes[2].remove('elephant')
boxes[2].append('storm')
boxes[2].append('moon')
boxes[2].append('tape')

# Move the mountain and the pan and the key from Box 7 to Box 0.
boxes[7].remove('mountain')
boxes[7].remove('pan')
boxes[7].remove('key')
boxes[0].append('mountain')
boxes[0].append('pan')
boxes[0].append('key')

# Put the lightning into Box 8.
boxes[8].append('lightning')

# Put the lightning and the island and the pants into Box 2.
boxes[2].append('lightning')
boxes[2].append('island')
boxes[2].append('pants')

# Replace the fork and the island with the submarine and the shorts in Box 10.
boxes[10].remove('fork')
boxes[10].remove('island')
boxes[10].append('submarine')
boxes[10].append('shorts')

# Replace the polish and the key with the piano and the wire in Box 0.
boxes[0].remove('polish')
boxes[0].remove('key')
boxes[0].append('piano')
boxes[0].append('wire')

# Swap the fridge in Box 5 with the lightning in Box 8.
boxes[5].remove('fridge')
boxes[8].remove('lightning')
boxes[5].append('lightning')
boxes[8].append('fridge')

# Put the moon into Box 12.
boxes[12].append('moon')

# Replace the pants with the dice in Box 1.
boxes[1].remove('pants')
boxes[1].append('dice')

# Empty Box 8.
boxes[8] = []

# Remove the dice from Box 9.
boxes[9].remove('dice')

# Remove the lightning from Box 2.
boxes[2].remove('lightning')

# Remove the moon from Box 12.
boxes[12].remove('moon')

# Empty Box 2.
boxes[2] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")