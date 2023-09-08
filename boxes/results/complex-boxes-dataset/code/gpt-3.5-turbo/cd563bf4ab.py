# Initial state of boxes
boxes = {
    0: ['fridge'],
    1: ['mountain', 'planet', 'whistle', 'grass', 'bear'],
    2: ['pants', 'polish', 'freezer', 'soap', 'sun'],
    3: ['zipper', 'lipstick', 'crown', 'comb'],
    4: ['tiger', 'tie', 'cloud', 'swimsuit', 'gloves'],
    5: [],
    6: ['ocean', 'guitar', 'car', 'octopus']
}

# Replace the fridge with the zipper in Box 0.
boxes[0].remove('fridge')
boxes[0].append('zipper')

# Move the zipper from Box 0 to Box 5.
boxes[0].remove('zipper')
boxes[5].append('zipper')

# Swap the crown in Box 3 with the polish in Box 2.
boxes[3].remove('crown')
boxes[2].remove('polish')
boxes[3].append('polish')
boxes[2].append('crown')

# Replace the whistle with the keyboard in Box 1.
boxes[1].remove('whistle')
boxes[1].append('keyboard')

# Swap the cloud in Box 4 with the zipper in Box 5.
boxes[4].remove('cloud')
boxes[5].remove('zipper')
boxes[4].append('zipper')
boxes[5].append('cloud')

# Move the crown from Box 2 to Box 6.
boxes[2].remove('crown')
boxes[6].append('crown')

# Remove the crown from Box 6.
boxes[6].remove('crown')

# Swap the freezer in Box 2 with the cloud in Box 5.
boxes[2].remove('freezer')
boxes[5].remove('cloud')
boxes[2].append('cloud')
boxes[5].append('freezer')

# Empty Box 6.
boxes[6] = []

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")