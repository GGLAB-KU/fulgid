box_0 = ['train', 'bird', 'whistle', 'perfume']
box_1 = ['pan', 'rock', 'ocean']
box_2 = ['cloud', 'ship', 'truck', 'scissors']
box_3 = ['laptop', 'fork', 'book', 'car']
box_4 = ['glove', 'fish', 'wire', 'vase', 'tie']
box_5 = []
box_6 = ['mirror', 'motorcycle']
box_7 = ['shark', 'key', 'lightning', 'mixer', 'bear']

# Move items from Box 4 to Box 2
box_2.extend([box_4.pop(box_4.index('vase')), box_4.pop(box_4.index('tie')), box_4.pop(box_4.index('fish'))])

# Remove wire from Box 4
box_4.remove('wire')

# Replace items in Box 7
box_7[box_7.index('shark')] = 'toaster'
box_7[box_7.index('lightning')] = 'coral'
box_7[box_7.index('bear')] = 'headphone'

# Swap key in Box 7 with fork in Box 3
box_7[box_7.index('key')], box_3[box_3.index('fork')] = box_3[box_3.index('fork')], box_7[box_7.index('key')]

# Remove glove from Box 4
box_4.remove('glove')

# Remove pan and ocean from Box 1
box_1.remove('pan')
box_1.remove('ocean')

# Remove book, car, and key from Box 3
box_3.remove('book')
box_3.remove('car')
box_3.remove('key')

# Replace rock with star in Box 1
box_1[box_1.index('rock')] = 'star'

# Replace star with lipstick in Box 1
box_1[box_1.index('star')] = 'lipstick'

# Replace motorcycle with dice in Box 6
box_6[box_6.index('motorcycle')] = 'dice'

# Replace lipstick with bird in Box 1
box_1[box_1.index('lipstick')] = 'bird'

# Replace laptop with clock in Box 3
box_3[box_3.index('laptop')] = 'clock'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)