box_0 = ['umbrella', 'comb', 'phone', 'lightning', 'shirt']
box_1 = ['cloud', 'train', 'jungle']
box_2 = ['meteor', 'laptop', 'candle', 'towel']
box_3 = ['comet', 'flower', 'planet', 'chair']

# Remove train from Box 1
box_1.remove('train')

# Replace cloud and jungle with card and piano in Box 1
box_1.remove('cloud')
box_1.remove('jungle')
box_1.extend(['card', 'piano'])

# Remove meteor and candle from Box 2
box_2.remove('meteor')
box_2.remove('candle')

# Remove towel from Box 2
box_2.remove('towel')

# Move piano from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('piano')))

# Replace laptop with microscope in Box 2
box_2[box_2.index('laptop')] = 'microscope'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)