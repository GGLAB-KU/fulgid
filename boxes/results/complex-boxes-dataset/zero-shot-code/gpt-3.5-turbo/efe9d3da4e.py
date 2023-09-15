box_0 = ['tape', 'headphone', 'tie', 'lightning', 'comet']
box_1 = ['mixer', 'swimsuit']
box_2 = ['belt', 'desert', 'keyboard', 'cloud']
box_3 = ['pan', 'towel', 'mask', 'dolphin', 'horn']
box_4 = ['river', 'apple']
box_5 = ['card', 'microscope', 'controller']
box_6 = ['fridge']
box_7 = []
box_8 = ['sun', 'guitar', 'rock', 'whistle', 'cup']
box_9 = ['leaf', 'laptop', 'sock', 'forest']
box_10 = ['tiger', 'tree', 'shelf', 'usb', 'hat']
box_11 = []
box_12 = ['shorts']

# Swap the controller in Box 5 with the dolphin in Box 3
box_5.remove('controller')
box_3.remove('dolphin')
box_5.append('dolphin')
box_3.append('controller')

# Move the towel and the pan and the controller from Box 3 to Box 8
box_3.remove('towel')
box_3.remove('pan')
box_3.remove('controller')
box_8.extend(['towel', 'pan', 'controller'])

# Remove the keyboard and the cloud from Box 2
box_2.remove('keyboard')
box_2.remove('cloud')

# Move the laptop and the leaf from Box 9 to Box 5
box_9.remove('laptop')
box_9.remove('leaf')
box_5.extend(['laptop', 'leaf'])

# Put the telescope and the razor and the pot into Box 0
box_0.extend(['telescope', 'razor', 'pot'])

# Put the phone and the bell and the necklace into Box 5
box_5.extend(['phone', 'bell', 'necklace'])

# Swap the horn in Box 3 with the swimsuit in Box 1
box_3.remove('horn')
box_1.remove('swimsuit')
box_3.append('swimsuit')
box_1.append('horn')

# Replace the sock with the horn in Box 9
box_9.remove('sock')
box_9.append('horn')

# Put the crown and the rocket and the horse into Box 8
box_8.extend(['crown', 'rocket', 'horse'])

# Move the horn and the forest from Box 9 to Box 5
box_9.remove('horn')
box_9.remove('forest')
box_5.extend(['horn', 'forest'])

# Replace the tiger and the hat with the scissors and the cup in Box 10
box_10.remove('tiger')
box_10.remove('hat')
box_10.append('scissors')
box_10.append('cup')

# Put the shampoo and the flute and the train into Box 0
box_0.extend(['shampoo', 'flute', 'train'])

# Move the shorts from Box 12 to Box 11
box_12.remove('shorts')
box_11.append('shorts')

# Remove the lightning and the train from Box 0
box_0.remove('lightning')
box_0.remove('train')

# Put the truck and the grass into Box 7
box_7.extend(['truck', 'grass'])

# Move the horn and the mixer from Box 1 to Box 0
box_1.remove('horn')
box_1.remove('mixer')
box_0.extend(['horn', 'mixer'])

# Swap the grass in Box 7 with the tree in Box 10
box_7.remove('grass')
box_10.remove('tree')
box_7.append('tree')
box_10.append('grass')

# Swap the guitar in Box 8 with the headphone in Box 0
box_8.remove('guitar')
box_0.remove('headphone')
box_8.append('headphone')
box_0.append('guitar')

# Swap the guitar in Box 0 with the desert in Box 2
box_0.remove('guitar')
box_2.remove('desert')
box_0.append('desert')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")