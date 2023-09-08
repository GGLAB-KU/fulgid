# Initial state of boxes
boxes = {
    0: [],
    1: ['oven', 'microwave'],
    2: ['shorts', 'bell', 'branch', 'ring', 'beach'],
    3: ['shampoo', 'butterfly', 'ocean', 'perfume'],
    4: ['moon', 'ship', 'bracelet', 'wallet'],
    5: ['planet', 'starfish', 'grass', 'crown']
}

# Swap the starfish in Box 5 with the ocean in Box 3.
boxes[5].remove('starfish')
boxes[3].remove('ocean')
boxes[5].append('ocean')
boxes[3].append('starfish')

# Remove the bracelet and the wallet and the ship from Box 4.
items_to_remove = ['bracelet', 'wallet', 'ship']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the moon from Box 4.
boxes[4].remove('moon')

# Swap the beach in Box 2 with the perfume in Box 3.
boxes[2].remove('beach')
boxes[3].remove('perfume')
boxes[2].append('perfume')
boxes[3].append('beach')

# Replace the ocean and the planet with the star and the tiger in Box 5.
boxes[5].remove('ocean')
boxes[5].remove('planet')
boxes[5].append('star')
boxes[5].append('tiger')

# Swap the oven in Box 1 with the ring in Box 2.
boxes[1].remove('oven')
boxes[2].remove('ring')
boxes[1].append('ring')
boxes[2].append('oven')

# Swap the butterfly in Box 3 with the branch in Box 2.
boxes[3].remove('butterfly')
boxes[2].remove('branch')
boxes[3].append('branch')
boxes[2].append('butterfly')

# Remove the microwave and the ring from Box 1.
boxes[1].remove('microwave')
boxes[1].remove('ring')

# Swap the bell in Box 2 with the shampoo in Box 3.
boxes[2].remove('bell')
boxes[3].remove('shampoo')
boxes[2].append('shampoo')
boxes[3].append('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")