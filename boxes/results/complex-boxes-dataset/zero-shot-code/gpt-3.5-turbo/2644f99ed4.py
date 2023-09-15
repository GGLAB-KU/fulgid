box_0 = []
box_1 = ['camera', 'meteor']
box_2 = ['lock']
box_3 = []
box_4 = ['sandals', 'lion', 'horse']
box_5 = ['soap', 'comet', 'microscope']
box_6 = ['rain', 'earring', 'shoe', 'piano', 'bag']
box_7 = []
box_8 = ['ocean']
box_9 = ['bowl', 'mask']
box_10 = ['pillow']

# Remove the lock from Box 2
box_2.remove('lock')

# Replace the earring and the bag with the shoes and the camera in Box 6
box_6.remove('earring')
box_6.remove('bag')
box_6.append('shoes')
box_6.append('camera')

# Move the lion and the horse from Box 4 to Box 5
box_5.append(box_4.pop(box_4.index('lion')))
box_5.append(box_4.pop(box_4.index('horse')))

# Replace the ocean with the battery in Box 8
box_8.remove('ocean')
box_8.append('battery')

# Move the sandals from Box 4 to Box 8
box_8.append(box_4.pop(box_4.index('sandals')))

# Swap the lion in Box 5 with the sandals in Box 8
box_5.append(box_8.pop(box_8.index('lion')))
box_8.append(box_5.pop(box_5.index('sandals')))

# Swap the soap in Box 5 with the camera in Box 1
box_5.append(box_1.pop(box_1.index('soap')))
box_1.append(box_5.pop(box_5.index('camera')))

# Move the bowl from Box 9 to Box 5
box_5.append(box_9.pop(box_9.index('bowl')))

# Move the piano and the shoe from Box 6 to Box 7
box_7.append(box_6.pop(box_6.index('piano')))
box_7.append(box_6.pop(box_6.index('shoe')))

# Put the cow and the fridge into Box 1
box_1.append('cow')
box_1.append('fridge')

# Move the camera from Box 5 to Box 3
box_3.append(box_5.pop(box_5.index('camera')))

# Put the plate into Box 2
box_2.append('plate')

# Put the fish and the elephant into Box 1
box_1.append('fish')
box_1.append('elephant')

# Replace the cow and the fridge and the fish with the microscope and the cup and the coral in Box 1
box_1.remove('cow')
box_1.remove('fridge')
box_1.remove('fish')
box_1.append('microscope')
box_1.append('cup')
box_1.append('coral')

# Remove the plate from Box 2
box_2.remove('plate')

# Move the camera from Box 3 to Box 10
box_10.append(box_3.pop(box_3.index('camera')))

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
print("Box 9:", box_9)
print("Box 10:", box_10)