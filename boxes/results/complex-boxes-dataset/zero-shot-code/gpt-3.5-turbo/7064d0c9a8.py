box_0 = ['usb', 'frame', 'perfume', 'vase']
box_1 = ['pan', 'sock', 'battery']
box_2 = ['zipper']
box_3 = ['fish', 'cow']
box_4 = ['telescope', 'mask', 'scarf']

# Replace cow and fish with cat and comet in Box 3
box_3.remove('fish')
box_3.remove('cow')
box_3.extend(['cat', 'comet'])

# Move scarf, telescope, and mask from Box 4 to Box 0
box_0.extend(box_4)
box_4.clear()

# Swap zipper in Box 2 with sock in Box 1
box_2[0], box_1[1] = box_1[1], box_2[0]

# Put leaf into Box 0
box_0.append('leaf')

# Remove frame from Box 0
box_0.remove('frame')

# Replace comet and cat with motorcycle and umbrella in Box 3
box_3.remove('comet')
box_3.remove('cat')
box_3.extend(['motorcycle', 'umbrella'])

# Remove sock from Box 2
box_2.remove('sock')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)