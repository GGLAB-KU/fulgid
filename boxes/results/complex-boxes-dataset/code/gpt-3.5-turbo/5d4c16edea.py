# Initial state of boxes
boxes = {
    0: ['guitar'],
    1: ['earring'],
    2: ['dog', 'ship'],
    3: ['candle'],
    4: ['harmonica', 'star', 'basket'],
    5: ['blender', 'pants', 'cow', 'planet', 'wallet'],
    6: ['card', 'plate', 'laptop', 'wire'],
    7: ['makeup'],
    8: [],
    9: ['desert', 'needle'],
    10: [],
    11: ['car', 'grinder', 'key'],
    12: ['lamp', 'submarine', 'bag', 'microscope']
}

# Replace the earring with the ship in Box 1.
boxes[1].remove('earring')
boxes[1].append('ship')

# Replace the ship with the storm in Box 1.
boxes[1].remove('ship')
boxes[1].append('storm')

# Remove the basket and the harmonica from Box 4.
boxes[4].remove('basket')
boxes[4].remove('harmonica')

# Move the candle from Box 3 to Box 4.
boxes[3].remove('candle')
boxes[4].append('candle')

# Put the mirror and the button and the freezer into Box 0.
boxes[0].extend(['mirror', 'button', 'freezer'])

# Put the shirt and the gloves into Box 5.
boxes[5].extend(['shirt', 'gloves'])

# Replace the microscope and the bag and the lamp with the skirt and the dress and the zipper in Box 12.
boxes[12].remove('microscope')
boxes[12].remove('bag')
boxes[12].remove('lamp')
boxes[12].extend(['skirt', 'dress', 'zipper'])

# Put the lightning and the starfish and the cloud into Box 8.
boxes[8].extend(['lightning', 'starfish', 'cloud'])

# Swap the storm in Box 1 with the ship in Box 2.
boxes[1].remove('storm')
boxes[2].remove('ship')
boxes[1].append('ship')
boxes[2].append('storm')

# Empty Box 9.
boxes[9] = []

# Move the submarine and the skirt and the dress from Box 12 to Box 9.
items_to_move = ['submarine', 'skirt', 'dress']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[9].append(item)

# Put the lipstick and the grinder and the jacket into Box 11.
boxes[11].extend(['lipstick', 'grinder', 'jacket'])

# Put the harmonica and the shelf into Box 6.
boxes[6].extend(['harmonica', 'shelf'])

# Remove the candle and the star from Box 4.
boxes[4].remove('candle')
boxes[4].remove('star')

# Move the dress from Box 9 to Box 3.
boxes[9].remove('dress')
boxes[3].append('dress')

# Swap the dog in Box 2 with the ship in Box 1.
boxes[2].remove('dog')
boxes[1].remove('ship')
boxes[2].append('ship')
boxes[1].append('dog')

# Replace the makeup with the grinder in Box 7.
boxes[7].remove('makeup')
boxes[7].append('grinder')

# Move the zipper from Box 12 to Box 6.
boxes[12].remove('zipper')
boxes[6].append('zipper')

# Swap the submarine in Box 9 with the dog in Box 1.
boxes[9].remove('submarine')
boxes[1].remove('dog')
boxes[9].append('dog')
boxes[1].append('submarine')

# Put the violin into Box 9.
boxes[9].append('violin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")