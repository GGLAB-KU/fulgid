box_0 = ['earring', 'microscope', 'island', 'forest']
box_1 = []
box_2 = ['bicycle', 'key', 'submarine', 'usb', 'rock']
box_3 = ['wig']
box_4 = ['book', 'moon', 'toy', 'drum', 'vase']
box_5 = []

# Put the spoon into Box 2
box_2.append('spoon')

# Put the ocean and the planet and the button into Box 3
box_3.extend(['ocean', 'planet', 'button'])

# Put the chair and the towel and the shirt into Box 3
box_3.extend(['chair', 'towel', 'shirt'])

# Remove the microscope from Box 0
box_0.remove('microscope')

# Replace the book and the toy with the button and the leaf in Box 4
box_4.remove('book')
box_4.remove('toy')
box_4.extend(['button', 'leaf'])

# Replace the drum and the button with the microscope and the butterfly in Box 4
box_4.remove('drum')
box_4.remove('button')
box_4.extend(['microscope', 'butterfly'])

# Put the shirt and the drum and the pot into Box 1
box_1.extend(['shirt', 'drum', 'pot'])

# Swap the bicycle in Box 2 with the forest in Box 0
box_2.remove('bicycle')
box_0.remove('forest')
box_2.append('forest')
box_0.append('bicycle')

# Replace the planet and the shirt and the chair with the wallet and the fish and the horn in Box 3
box_3.remove('planet')
box_3.remove('shirt')
box_3.remove('chair')
box_3.extend(['wallet', 'fish', 'horn'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)