box_0 = ['sun', 'bracelet', 'island']
box_1 = ['coat', 'oven']
box_2 = ['guitar', 'horn', 'thunder']
box_3 = ['microscope', 'pot']
box_4 = ['planet', 'bird', 'comb']
box_5 = ['branch']
box_6 = ['spoon', 'dog', 'card']
box_7 = ['ring', 'leaf', 'lock', 'hat', 'tiger']
box_8 = ['pants']
box_9 = ['cloud', 'microscope', 'microscope', 'pot']
box_10 = []
box_11 = ['octopus', 'fork', 'freezer']
box_12 = []

# Replace the violin and the boot with the bracelet and the island in Box 0
box_0.remove('bracelet')
box_0.remove('island')
box_0.append('violin')
box_0.append('boot')

# Replace the planet with the sun in Box 0
box_0.remove('planet')
box_0.append('sun')

# Put the cloud into Box 9
box_9.append('cloud')

# Put the tree and the island and the desert into Box 6
box_6.append('tree')
box_6.append('island')
box_6.append('desert')

# Swap the laptop in Box 12 with the shoes in Box 5
box_12.remove('laptop')
box_5.remove('shoes')
box_12.append('shoes')
box_5.append('laptop')

# Replace the button and the dice with the oven and the coat in Box 1
box_1.remove('button')
box_1.remove('dice')
box_1.append('oven')
box_1.append('coat')

# Move the butterfly from Box 10 to Box 4
box_10.remove('butterfly')
box_4.append('butterfly')

# Move the branch from Box 5 to Box 0
box_5.remove('branch')
box_0.append('branch')

# Remove the pen and the dolphin and the headphone from Box 4
box_4.remove('pen')
box_4.remove('dolphin')
box_4.remove('headphone')

# Put the coin and the usb into Box 11
box_11.append('coin')
box_11.append('usb')

# Replace the submarine and the butterfly and the cup with the planet and the bird and the comb in Box 4
box_4.remove('submarine')
box_4.remove('butterfly')
box_4.remove('cup')
box_4.append('planet')
box_4.append('bird')
box_4.append('comb')

# Remove the shoes from Box 12
box_12.remove('shoes')

# Swap the bracelet in Box 0 with the pants in Box 8
box_0.remove('bracelet')
box_8.remove('pants')
box_0.append('pants')
box_8.append('bracelet')

# Replace the skirt and the desert and the starfish with the spoon and the dog and the card in Box 6
box_6.remove('skirt')
box_6.remove('desert')
box_6.remove('starfish')
box_6.append('spoon')
box_6.append('dog')
box_6.append('card')

# Put the guitar and the horn and the thunder into Box 2
box_2.append('guitar')
box_2.append('horn')
box_2.append('thunder')

# Remove the oven from Box 1
box_1.remove('oven')

# Remove the comb from Box 4
box_4.remove('comb')

# Replace the crown with the microscope in Box 3
box_3.remove('crown')
box_3.append('microscope')

# Move the microscope and the microscope and the pot from Box 3 to Box 9
box_3.remove('microscope')
box_3.remove('microscope')
box_3.remove('pot')
box_9.append('microscope')
box_9.append('microscope')
box_9.append('pot')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")