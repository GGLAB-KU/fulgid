box_0 = ['basket', 'candle', 'pan', 'hat', 'brush']
box_1 = ['toy', 'crown', 'jacket']
box_2 = ['mixer', 'shirt', 'cloud']
box_3 = ['coral', 'fork']
box_4 = ['fridge', 'island', 'bird', 'coat', 'book']
box_5 = ['sculpture', 'console']
box_6 = ['rock', 'sock', 'frame', 'butterfly', 'skirt']
box_7 = []
box_8 = ['flower', 'ocean', 'lipstick', 'dog', 'perfume']
box_9 = ['spoon']

# Swap the basket in Box 0 with the fork in Box 3
box_0[box_0.index('basket')], box_3[box_3.index('fork')] = box_3[box_3.index('fork')], box_0[box_0.index('basket')]

# Replace the coat with the bracelet in Box 4
box_4[box_4.index('coat')] = 'bracelet'

# Put the lipstick into Box 7
box_7.append('lipstick')

# Put the perfume and the plane into Box 3
box_3.extend(['perfume', 'plane'])

# Remove the sculpture from Box 5
box_5.remove('sculpture')

# Swap the brush in Box 0 with the butterfly in Box 6
box_0[box_0.index('brush')], box_6[box_6.index('butterfly')] = box_6[box_6.index('butterfly')], box_0[box_0.index('brush')]

# Remove the fridge and the bracelet from Box 4
box_4.remove('fridge')
box_4.remove('bracelet')

# Replace the lipstick with the bird in Box 7
box_7[box_7.index('lipstick')] = 'bird'

# Move the mixer and the shirt from Box 2 to Box 6
box_6.extend(['mixer', 'shirt'])
box_2.remove('mixer')
box_2.remove('shirt')

# Empty Box 9
box_9 = []

# Move the island from Box 4 to Box 5
box_5.append('island')
box_4.remove('island')

# Swap the frame in Box 6 with the console in Box 5
box_6[box_6.index('frame')], box_5[box_5.index('console')] = box_5[box_5.index('console')], box_6[box_6.index('frame')]

# Move the bird and the book from Box 4 to Box 0
box_0.extend(['bird', 'book'])
box_4.remove('bird')
box_4.remove('book')

# Swap the console in Box 6 with the crown in Box 1
box_6[box_6.index('console')], box_1[box_1.index('crown')] = box_1[box_1.index('crown')], box_6[box_6.index('console')]

# Remove the cloud from Box 2
box_2.remove('cloud')

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