# Initial state of boxes
boxes = {
    0: ['perfume'],
    1: ['sock', 'scarf', 'shark', 'toaster'],
    2: ['blender', 'moon'],
    3: ['pot', 'seaweed', 'ocean'],
    4: ['elephant'],
    5: ['scissors', 'freezer', 'cup']
}

# Put the leaf and the starfish and the ocean into Box 1.
boxes[1].append('leaf')
boxes[1].append('starfish')
boxes[1].append('ocean')

# Swap the leaf in Box 1 with the moon in Box 2.
boxes[1].remove('leaf')
boxes[2].remove('moon')
boxes[1].append('moon')
boxes[2].append('leaf')

# Replace the elephant with the magnet in Box 4.
boxes[4].remove('elephant')
boxes[4].append('magnet')

# Replace the scarf with the charger in Box 1.
boxes[1].remove('scarf')
boxes[1].append('charger')

# Swap the perfume in Box 0 with the magnet in Box 4.
boxes[0].remove('perfume')
boxes[4].remove('magnet')
boxes[0].append('magnet')
boxes[4].append('perfume')

# Replace the leaf and the blender with the horse and the fridge in Box 2.
boxes[2].remove('leaf')
boxes[2].remove('blender')
boxes[2].append('horse')
boxes[2].append('fridge')

# Put the shorts and the bear into Box 1.
boxes[1].append('shorts')
boxes[1].append('bear')

# Remove the fridge and the horse from Box 2.
boxes[2].remove('fridge')
boxes[2].remove('horse')

# Put the mixer into Box 4.
boxes[4].append('mixer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")