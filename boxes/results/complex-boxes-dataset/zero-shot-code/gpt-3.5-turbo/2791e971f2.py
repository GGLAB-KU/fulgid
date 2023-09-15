box_0 = ['earring', 'star']
box_1 = ['frame', 'toothpaste']
box_2 = ['shoes', 'beach', 'mountain', 'pants']
box_3 = ['branch', 'crown', 'storm', 'towel']

# Move the storm from Box 3 to Box 2
box_2.append(box_3.pop(box_3.index('storm')))

# Remove the frame from Box 1
box_1.remove('frame')

# Replace the star with the plane in Box 0
box_0[box_0.index('star')] = 'plane'

# Remove the towel and the crown from Box 3
box_3.remove('towel')
box_3.remove('crown')

# Remove the shoes and the mountain and the pants from Box 2
box_2.remove('shoes')
box_2.remove('mountain')
box_2.remove('pants')

# Put the blanket and the lipstick and the helmet into Box 3
box_3.extend(['blanket', 'lipstick', 'helmet'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)