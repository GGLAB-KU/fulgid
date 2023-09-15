box_0 = ['razor', 'laptop', 'dress']
box_1 = ['car', 'submarine']
box_2 = ['fridge', 'apple', 'rocket', 'pen', 'chair']
box_3 = []
box_4 = ['card', 'bell', 'lion']
box_5 = ['cat']
box_6 = ['lipstick', 'blender', 'sculpture', 'usb']
box_7 = ['ship', 'bicycle', 'telescope', 'makeup']
box_8 = ['microscope']
box_9 = []
box_10 = ['spoon', 'boot', 'frame']
box_11 = []
box_12 = ['needle']

# Swap the chair in Box 2 with the cat in Box 5
box_2.remove('chair')
box_5.remove('cat')
box_2.append('cat')
box_5.append('chair')

# Replace the submarine and the car with the glasses and the pillow in Box 1
box_1.remove('car')
box_1.remove('submarine')
box_1.append('glasses')
box_1.append('pillow')

# Move the bell and the lion from Box 4 to Box 9
box_4.remove('bell')
box_4.remove('lion')
box_9.append('bell')
box_9.append('lion')

# Swap the needle in Box 12 with the dress in Box 0
box_12.remove('needle')
box_0.remove('dress')
box_12.append('dress')
box_0.append('needle')

# Move the lion from Box 9 to Box 1
box_9.remove('lion')
box_1.append('lion')

# Empty Box 10
box_10 = []

# Move the chair from Box 5 to Box 1
box_5.remove('chair')
box_1.append('chair')

# Put the coat into Box 6
box_6.append('coat')

# Swap the card in Box 4 with the makeup in Box 7
box_4.remove('card')
box_7.remove('makeup')
box_4.append('makeup')
box_7.append('card')

# Move the microscope from Box 8 to Box 5
box_8.remove('microscope')
box_5.append('microscope')

# Move the pillow and the lion from Box 1 to Box 8
box_1.remove('pillow')
box_1.remove('lion')
box_8.append('pillow')
box_8.append('lion')

# Move the bicycle and the ship and the telescope from Box 7 to Box 11
box_7.remove('bicycle')
box_7.remove('ship')
box_7.remove('telescope')
box_11.append('bicycle')
box_11.append('ship')
box_11.append('telescope')

# Move the bell from Box 9 to Box 7
box_9.remove('bell')
box_7.append('bell')

# Swap the dress in Box 12 with the card in Box 7
box_12.remove('dress')
box_7.remove('card')
box_12.append('card')
box_7.append('dress')

# Replace the makeup with the shorts in Box 4
box_4.remove('makeup')
box_4.append('shorts')

# Put the boot and the glove into Box 3
box_3.append('boot')
box_3.append('glove')

# Replace the needle and the razor and the laptop with the wig and the blender and the phone in Box 0
box_0.remove('needle')
box_0.remove('razor')
box_0.remove('laptop')
box_0.append('wig')
box_0.append('blender')
box_0.append('phone')

# Replace the card with the flute in Box 12
box_12.remove('card')
box_12.append('flute')

# Remove the telescope and the ship and the bicycle from Box 11
box_11.remove('telescope')
box_11.remove('ship')
box_11.remove('bicycle')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")