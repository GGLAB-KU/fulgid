# Initial state of boxes
boxes = {
    0: [],
    1: ['oven', 'flower', 'pillow', 'umbrella', 'guitar'],
    2: ['toothpaste', 'pen', 'polish', 'sun', 'blender'],
    3: ['vase', 'shorts', 'plane', 'bird', 'thunder'],
    4: ['swimsuit', 'river', 'dress', 'coat', 'forest'],
    5: ['meteor', 'charger'],
    6: ['controller'],
    7: ['bag', 'card'],
    8: ['mask', 'zipper', 'toaster', 'piano', 'shirt']
}

# Remove the bird from Box 3.
boxes[3].remove('bird')

# Swap the coat in Box 4 with the charger in Box 5.
boxes[4].remove('coat')
boxes[5].remove('charger')
boxes[4].append('charger')
boxes[5].append('coat')

# Swap the bag in Box 7 with the controller in Box 6.
boxes[7].remove('bag')
boxes[6].remove('controller')
boxes[7].append('controller')
boxes[6].append('bag')

# Remove the bag from Box 6.
boxes[6].remove('bag')

# Move the flower from Box 1 to Box 0.
boxes[1].remove('flower')
boxes[0].append('flower')

# Put the rock and the table into Box 4.
boxes[4].append('rock')
boxes[4].append('table')

# Move the flower from Box 0 to Box 5.
boxes[0].remove('flower')
boxes[5].append('flower')

# Swap the toothpaste in Box 2 with the flower in Box 5.
boxes[2].remove('toothpaste')
boxes[5].remove('flower')
boxes[2].append('flower')
boxes[5].append('toothpaste')

# Swap the pillow in Box 1 with the plane in Box 3.
boxes[1].remove('pillow')
boxes[3].remove('plane')
boxes[1].append('plane')
boxes[3].append('pillow')

# Remove the sun and the polish from Box 2.
boxes[2].remove('sun')
boxes[2].remove('polish')

# Move the controller and the card from Box 7 to Box 5.
boxes[7].remove('card')
boxes[5].append('card')
boxes[6].remove('controller')
boxes[5].append('controller')

# Put the necklace into Box 7.
boxes[7].append('necklace')

# Remove the necklace from Box 7.
boxes[7].remove('necklace')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")