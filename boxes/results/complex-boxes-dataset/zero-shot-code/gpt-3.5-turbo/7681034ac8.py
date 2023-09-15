box_0 = ['rocket', 'tiger', 'tree']
box_1 = ['boat', 'skirt', 'brush', 'grinder', 'battery']
box_2 = ['blender', 'dolphin', 'laptop']
box_3 = ['planet', 'train', 'book', 'paint', 'blanket']
box_4 = ['moon', 'phone', 'mountain', 'speaker']
box_5 = ['microscope', 'ocean', 'scarf', 'cup', 'bicycle']
box_6 = ['freezer', 'glasses']
box_7 = ['desert', 'rock', 'zipper']
box_8 = ['cow']
box_9 = ['sock']
box_10 = ['coral', 'plate', 'charger', 'clock']

def print_boxes():
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

print_boxes()

# Move the clock from Box 10 to Box 6
box_6.append(box_10.pop(box_10.index('clock')))
print_boxes()

# Move the clock from Box 6 to Box 2
box_2.append(box_6.pop(box_6.index('clock')))
print_boxes()

# Move the rock from Box 7 to Box 5
box_5.append(box_7.pop(box_7.index('rock')))
print_boxes()

# Empty Box 4
box_4 = []
print_boxes()

# Remove the book and the paint and the train from Box 3
box_3.remove('book')
box_3.remove('paint')
box_3.remove('train')
print_boxes()

# Move the plate and the charger and the coral from Box 10 to Box 9
box_9.extend([box_10.pop(box_10.index('plate')), box_10.pop(box_10.index('charger')), box_10.pop(box_10.index('coral'))])
print_boxes()

# Swap the tree in Box 0 with the zipper in Box 7
box_0[box_0.index('tree')], box_7[box_7.index('zipper')] = box_7[box_7.index('zipper')], box_0[box_0.index('tree')]
print_boxes()

# Move the planet from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('planet')))
print_boxes()

# Move the clock and the blender from Box 2 to Box 7
box_7.extend([box_2.pop(box_2.index('clock')), box_2.pop(box_2.index('blender'))])
print_boxes()

# Put the whistle and the mask and the cup into Box 5
box_5.extend(['whistle', 'mask', 'cup'])
print_boxes()

# Move the freezer and the glasses from Box 6 to Box 0
box_0.extend([box_6.pop(box_6.index('freezer')), box_6.pop(box_6.index('glasses'))])
print_boxes()

# Empty Box 0
box_0 = []
print_boxes()

# Replace the coral with the elephant in Box 9
box_9[box_9.index('coral')] = 'elephant'
print_boxes()

# Move the scarf and the mask from Box 5 to Box 2
box_2.extend([box_5.pop(box_5.index('scarf')), box_5.pop(box_5.index('mask'))])
print_boxes()

# Put the lion and the microwave and the bear into Box 10
box_10.extend(['lion', 'microwave', 'bear'])
print_boxes()

# Swap the mask in Box 2 with the planet in Box 7
box_2[box_2.index('mask')], box_7[box_7.index('planet')] = box_7[box_7.index('planet')], box_2[box_2.index('mask')]
print_boxes()

# Replace the cup with the watch in Box 5
box_5[box_5.index('cup')] = 'watch'
print_boxes()