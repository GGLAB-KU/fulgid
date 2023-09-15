box_0 = ['harmonica', 'boat', 'cup', 'dress']
box_1 = []
box_2 = ['candle', 'tie', 'sock', 'keyboard', 'puzzle']
box_3 = []
box_4 = []
box_5 = []
box_6 = ['bowl', 'river', 'mask', 'shark']
box_7 = ['storm', 'pan', 'laptop']
box_8 = ['cloud', 'zipper', 'microwave', 'chair', 'mountain']

# Move the keyboard and the sock and the tie from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('keyboard')), box_2.pop(box_2.index('sock')), box_2.pop(box_2.index('tie'))])

# Remove the candle from Box 2
box_2.remove('candle')

# Move the cloud from Box 8 to Box 6
box_6.append(box_8.pop(box_8.index('cloud')))

# Put the mountain and the grinder and the bell into Box 3
box_3.extend(['mountain', 'grinder', 'bell'])

# Move the microwave and the zipper from Box 8 to Box 5
box_5.extend([box_8.pop(box_8.index('microwave')), box_8.pop(box_8.index('zipper'))])

# Remove the grinder and the bell and the mountain from Box 3
box_3 = []

# Swap the pan in Box 7 with the chair in Box 8
box_7[box_7.index('pan')], box_8[box_8.index('chair')] = box_8[box_8.index('chair')], box_7[box_7.index('pan')]

# Put the helmet and the river into Box 4
box_4.extend(['helmet', 'river'])

# Move the helmet and the river from Box 4 to Box 5
box_5.extend([box_4.pop(box_4.index('helmet')), box_4.pop(box_4.index('river'))])

# Move the harmonica and the keyboard from Box 0 to Box 5
box_5.extend([box_0.pop(box_0.index('harmonica')), box_0.pop(box_0.index('keyboard'))])

# Remove the boat and the cup and the dress from Box 0
box_0 = []

# Move the helmet and the keyboard and the river from Box 5 to Box 1
box_1.extend([box_5.pop(box_5.index('helmet')), box_5.pop(box_5.index('keyboard')), box_5.pop(box_5.index('river'))])

# Put the branch into Box 2
box_2.append('branch')

# Put the shirt and the charger into Box 8
box_8.extend(['shirt', 'charger'])

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