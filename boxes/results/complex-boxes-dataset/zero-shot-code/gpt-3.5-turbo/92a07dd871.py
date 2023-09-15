box_0 = ['ship', 'ring', 'towel']
box_1 = ['truck', 'wig', 'shoes']
box_2 = ['drum']
box_3 = ['doll', 'glasses']
box_4 = ['piano', 'pan', 'coin']
box_5 = []
box_6 = ['octopus']
box_7 = []
box_8 = ['butterfly', 'seaweed', 'lightning']

# Replace the plane with the harmonica in Box 0
box_0[1] = 'harmonica'

# Swap the tree in Box 3 with the skirt in Box 4
box_3[1], box_4[1] = box_4[1], box_3[1]

# Move the storm from Box 4 to Box 5
box_5.append(box_4.pop(0))

# Put the keyboard and the rain into Box 7
box_7.extend(['keyboard', 'rain'])

# Move the butterfly from Box 8 to Box 4
box_4.append(box_8.pop(0))

# Move the octopus and the sock and the river from Box 6 to Box 7
box_7.extend(box_6.pop(0))
box_7.extend(box_6.pop(0))
box_7.extend(box_6.pop(0))

# Remove the storm from Box 5
box_5.pop(0)

# Replace the piano with the spoon in Box 4
box_4[0] = 'spoon'

# Swap the branch in Box 2 with the swimsuit in Box 0
box_2[0], box_0[2] = box_0[2], box_2[0]

# Move the watch from Box 6 to Box 0
box_0.append(box_6.pop(0))

# Put the horn and the sock and the bracelet into Box 8
box_8.extend(['horn', 'sock', 'bracelet'])

# Remove the horn from Box 1
box_1.remove('horn')

# Swap the drum in Box 2 with the rain in Box 7
box_2[0], box_7[1] = box_7[1], box_2[0]

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