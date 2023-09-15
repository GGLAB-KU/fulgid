box_0 = ['brush', 'bicycle', 'starfish']
box_1 = ['crown', 'shark', 'mirror', 'button']
box_2 = []
box_3 = ['zipper', 'plane']
box_4 = ['needle', 'shoes', 'cow', 'octopus']
box_5 = ['ring', 'comb', 'gloves', 'spoon']
box_6 = ['polish', 'pants', 'laptop']
box_7 = ['scissors', 'flute', 'watch', 'drum']
box_8 = []
box_9 = ['vase', 'necklace', 'microscope']

# Remove the bicycle from Box 0
box_0.remove('bicycle')

# Move the comb and the gloves and the spoon from Box 5 to Box 7
box_7.extend(box_5[1:])
box_5 = box_5[:1]

# Move the laptop and the pants and the polish from Box 6 to Box 3
box_3.extend(box_6[1:])
box_6 = box_6[:1]

# Swap the pants in Box 3 with the comb in Box 7
box_3[1], box_7[1] = box_7[1], box_3[1]

# Put the towel and the harmonica into Box 8
box_8.extend(['towel', 'harmonica'])

# Move the harmonica from Box 8 to Box 4
box_4.append(box_8.pop(1))

# Put the train into Box 4
box_4.append('train')

# Move the starfish and the brush from Box 0 to Box 4
box_4.extend(box_0)
box_0 = []

# Put the soap into Box 6
box_6.append('soap')

# Move the polish and the zipper from Box 3 to Box 6
box_6.extend(box_3[1:])
box_3 = box_3[:1]

# Remove the comb and the laptop and the plane from Box 3
box_3 = []

# Swap the crown in Box 1 with the vase in Box 9
box_1[0], box_9[0] = box_9[0], box_1[0]

# Replace the microscope and the crown and the necklace with the rocket and the bear and the boot in Box 9
box_9 = ['rocket', 'bear', 'boot']

# Move the ring from Box 5 to Box 4
box_4.append(box_5.pop(0))

# Remove the vase from Box 1
box_1 = box_1[1:]

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