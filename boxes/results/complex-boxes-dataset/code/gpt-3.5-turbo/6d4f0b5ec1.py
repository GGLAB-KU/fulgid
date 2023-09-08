# Initial state of boxes
boxes = {
    0: ['earring', 'microscope', 'island', 'forest'],
    1: [],
    2: ['bicycle', 'key', 'submarine', 'usb', 'rock'],
    3: ['wig'],
    4: ['book', 'moon', 'toy', 'drum', 'vase'],
    5: []
}

# Put the spoon into Box 2.
boxes[2].append('spoon')

# Put the ocean and the planet and the button into Box 3.
boxes[3].append('ocean')
boxes[3].append('planet')
boxes[3].append('button')

# Put the chair and the towel and the shirt into Box 3.
boxes[3].append('chair')
boxes[3].append('towel')
boxes[3].append('shirt')

# Remove the microscope from Box 0.
boxes[0].remove('microscope')

# Replace the book and the toy with the button and the leaf in Box 4.
boxes[4].remove('book')
boxes[4].remove('toy')
boxes[4].append('button')
boxes[4].append('leaf')

# Replace the drum and the button with the microscope and the butterfly in Box 4.
boxes[4].remove('drum')
boxes[4].remove('button')
boxes[4].append('microscope')
boxes[4].append('butterfly')

# Put the shirt and the drum and the pot into Box 1.
boxes[1].append('shirt')
boxes[1].append('drum')
boxes[1].append('pot')

# Swap the bicycle in Box 2 with the forest in Box 0.
boxes[0].remove('forest')
boxes[2].remove('bicycle')
boxes[0].append('bicycle')
boxes[2].append('forest')

# Replace the planet and the shirt and the chair with the wallet and the fish and the horn in Box 3.
boxes[3].remove('planet')
boxes[3].remove('shirt')
boxes[3].remove('chair')
boxes[3].append('wallet')
boxes[3].append('fish')
boxes[3].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")