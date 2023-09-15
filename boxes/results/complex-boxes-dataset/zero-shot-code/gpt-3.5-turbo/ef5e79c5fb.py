box_0 = []
box_1 = ['star', 'shoe', 'perfume', 'rock', 'shirt']
box_2 = ['toy', 'dolphin', 'drum', 'swimsuit']
box_3 = []
box_4 = []
box_5 = ['button', 'scissors', 'storm']
box_6 = ['bear', 'horn', 'ship', 'whistle']
box_7 = ['fridge', 'tape', 'telescope', 'key']
box_8 = ['camera', 'toaster']

# Move the bear from Box 6 to Box 5
box_5.append(box_6.pop(0))

# Empty Box 6
box_6 = []

# Replace the perfume and the star with the pants and the wig in Box 1
box_1.remove('perfume')
box_1.remove('star')
box_1.extend(['pants', 'wig'])

# Move the camera from Box 8 to Box 0
box_0.append(box_8.pop(0))

# Replace the toaster with the pants in Box 8
box_8.remove('toaster')
box_8.append('pants')

# Move the camera from Box 0 to Box 6
box_6.append(box_0.pop(0))

# Swap the button in Box 5 with the pants in Box 8
box_5.remove('button')
box_8.remove('pants')
box_5.append('pants')
box_8.append('button')

# Replace the shoe with the toothpaste in Box 1
box_1.remove('shoe')
box_1.append('toothpaste')

# Move the toy from Box 2 to Box 5
box_5.append(box_2.pop(0))

# Put the phone into Box 8
box_8.append('phone')

# Swap the wig in Box 1 with the dolphin in Box 2
box_1.remove('wig')
box_2.remove('dolphin')
box_1.append('dolphin')
box_2.append('wig')

# Move the button and the phone from Box 8 to Box 0
box_0.extend([box_8.pop(0), box_8.pop(0)])

# Move the tape and the telescope from Box 7 to Box 0
box_0.extend([box_7.pop(1), box_7.pop(1)])

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