box_0 = ['forest', 'makeup', 'comet', 'jungle', 'bowl']
box_1 = []
box_2 = ['blender']
box_3 = []
box_4 = ['umbrella']
box_5 = ['storm', 'toy', 'tape', 'moon']
box_6 = ['bicycle', 'cow', 'cup', 'lock', 'skirt']
box_7 = ['button', 'shelf']
box_8 = ['drum']
box_9 = []
box_10 = ['game', 'ocean', 'sandals', 'coral']
box_11 = []
box_12 = ['dice', 'lipstick']

# Move the bowl and the makeup from Box 0 to Box 1
box_1.extend([box_0.pop(box_0.index('bowl')), box_0.pop(box_0.index('makeup'))])

# Move the jungle and the comet from Box 0 to Box 3
box_3.extend([box_0.pop(box_0.index('jungle')), box_0.pop(box_0.index('comet'))])

# Move the cup from Box 6 to Box 7
box_7.append(box_6.pop(box_6.index('cup')))

# Move the dice and the lipstick from Box 12 to Box 7
box_7.extend([box_12.pop(box_12.index('dice')), box_12.pop(box_12.index('lipstick'))])

# Put the hat and the needle into Box 9
box_9.extend(['hat', 'needle'])

# Swap the storm in Box 5 with the bicycle in Box 6
box_5[box_5.index('storm')], box_6[box_6.index('bicycle')] = box_6[box_6.index('bicycle')], box_5[box_5.index('storm')]

# Replace the makeup and the bowl with the pillow and the mirror in Box 1
box_1[box_1.index('makeup')] = 'mirror'
box_1[box_1.index('bowl')] = 'pillow'

# Remove the blender from Box 2
box_2.remove('blender')

# Swap the drum in Box 8 with the forest in Box 0
box_8[box_8.index('drum')], box_0[box_0.index('forest')] = box_0[box_0.index('forest')], box_8[box_8.index('drum')]

# Put the lion and the soap and the car into Box 10
box_10.extend(['lion', 'soap', 'car'])

# Put the puzzle and the book and the mountain into Box 4
box_4.extend(['puzzle', 'book', 'mountain'])

# Remove the cup and the dice from Box 7
box_7.remove('cup')
box_7.remove('dice')

# Move the bicycle from Box 5 to Box 9
box_9.append(box_5.pop(box_5.index('bicycle')))

# Put the camera and the makeup and the bicycle into Box 8
box_8.extend(['camera', 'makeup', 'bicycle'])

# Remove the umbrella and the mountain and the book from Box 4
box_4.remove('umbrella')
box_4.remove('mountain')
box_4.remove('book')

# Put the telescope and the island into Box 7
box_7.extend(['telescope', 'island'])

# Replace the island and the telescope with the card and the apple in Box 7
box_7[box_7.index('island')] = 'apple'
box_7[box_7.index('telescope')] = 'card'

# Move the storm and the skirt and the lock from Box 6 to Box 0
box_0.extend([box_6.pop(box_6.index('storm')), box_6.pop(box_6.index('skirt')), box_6.pop(box_6.index('lock'))])

# Remove the puzzle from Box 4
box_4.remove('puzzle')

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
print("Box 11:", box_11)
print("Box 12:", box_12)