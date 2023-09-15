box_0 = ['bicycle', 'comb', 'camera', 'forest', 'leaf']
box_1 = ['needle']
box_2 = []
box_3 = ['wire', 'sock', 'microscope']
box_4 = ['scissors', 'game', 'spoon']
box_5 = ['ship', 'paint', 'octopus', 'phone']
box_6 = ['usb']
box_7 = []
box_8 = ['headphone']

# Replace the usb with the speaker in Box 6
box_6.remove('usb')
box_6.append('speaker')

# Empty Box 4
box_4.clear()

# Remove the sock and the wire and the microscope from Box 3
box_3.remove('sock')
box_3.remove('wire')
box_3.remove('microscope')

# Remove the speaker from Box 6
box_6.remove('speaker')

# Put the lamp and the elephant and the dog into Box 4
box_4.extend(['lamp', 'elephant', 'dog'])

# Swap the phone in Box 5 with the comb in Box 0
box_0.remove('comb')
box_5.remove('phone')
box_0.append('phone')
box_5.append('comb')

# Put the necklace and the card and the train into Box 8
box_8.extend(['necklace', 'card', 'train'])

# Move the card from Box 8 to Box 7
box_8.remove('card')
box_7.append('card')

# Remove the train and the headphone and the necklace from Box 8
box_8.remove('train')
box_8.remove('headphone')
box_8.remove('necklace')

# Move the card from Box 7 to Box 2
box_7.remove('card')
box_2.append('card')

# Replace the card with the cloud in Box 2
box_2.remove('card')
box_2.append('cloud')

# Remove the needle from Box 1
box_1.remove('needle')

# Replace the elephant and the dog with the ship and the apple in Box 4
box_4.remove('elephant')
box_4.remove('dog')
box_4.append('ship')
box_4.append('apple')

# Empty Box 0
box_0.clear()

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)