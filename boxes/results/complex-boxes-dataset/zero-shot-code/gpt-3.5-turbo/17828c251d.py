box_0 = ['train', 'usb', 'makeup', 'cat', 'toy']
box_1 = ['desert', 'mirror', 'necklace', 'zipper', 'book']
box_2 = ['pot']
box_3 = []
box_4 = ['mountain', 'bicycle', 'puzzle']
box_5 = ['coin', 'violin', 'pants', 'swimsuit']
box_6 = []

# Move the cat from Box 0 to Box 2
box_2.append(box_0.pop(box_0.index('cat')))

# Empty Box 2
box_2 = []

# Move the mountain from Box 4 to Box 6
box_6.append(box_4.pop(box_4.index('mountain')))

# Replace the train and the toy and the makeup with the polish and the meteor and the comet in Box 0
box_0 = ['polish', 'meteor', 'comet']

# Replace the book and the mirror and the zipper with the toaster and the makeup and the sandals in Box 1
box_1 = ['toaster', 'makeup', 'sandals']

# Put the paint and the hat and the beach into Box 3
box_3 = ['paint', 'hat', 'beach']

# Swap the beach in Box 3 with the usb in Box 0
box_0[box_0.index('usb')], box_3[box_3.index('beach')] = box_3[box_3.index('beach')], box_0[box_0.index('usb')]

# Move the meteor and the polish from Box 0 to Box 1
box_1.append(box_0.pop(box_0.index('meteor')))
box_1.append(box_0.pop(box_0.index('polish')))

# Put the lion into Box 5
box_5.append('lion')

# Swap the hat in Box 3 with the beach in Box 0
box_0[box_0.index('beach')], box_3[box_3.index('hat')] = box_3[box_3.index('hat')], box_0[box_0.index('beach')]

# Empty Box 6
box_6 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)