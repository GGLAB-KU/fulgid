box_0 = ['truck', 'bicycle', 'drum', 'microscope']
box_1 = ['mixer', 'plane']
box_2 = ['shelf', 'scarf', 'guitar']
box_3 = ['starfish', 'hat']
box_4 = ['horse', 'usb', 'storm']
box_5 = ['bear', 'soap', 'basket', 'butterfly']
box_6 = []
box_7 = ['game', 'wire', 'pan', 'bag']
box_8 = ['frame', 'mountain']
box_9 = ['river', 'submarine', 'makeup', 'perfume']
box_10 = ['shoes', 'freezer']

# Remove the pan and the wire from Box 7
box_7.remove('pan')
box_7.remove('wire')

# Put the fish into Box 10
box_10.append('fish')

# Empty Box 9
box_9 = []

# Put the motorcycle and the umbrella and the dog into Box 2
box_2.extend(['motorcycle', 'umbrella', 'dog'])

# Put the mountain into Box 7
box_7.append('mountain')

# Move the motorcycle and the scarf and the dog from Box 2 to Box 7
box_7.extend(box_2[:3])
box_2 = box_2[3:]

# Put the scarf and the horse and the jungle into Box 10
box_10.extend(['scarf', 'horse', 'jungle'])

# Replace the mountain with the tape in Box 8
box_8 = ['tape']

# Swap the hat in Box 3 with the jungle in Box 10
box_3[1], box_10[box_10.index('jungle')] = box_10[box_10.index('jungle')], box_3[1]

# Remove the bear from Box 5
box_5.remove('bear')

# Swap the horse in Box 4 with the umbrella in Box 2
box_4[0], box_2[box_2.index('umbrella')] = box_2[box_2.index('umbrella')], box_4[0]

# Move the fish from Box 10 to Box 0
box_0.append(box_10.pop(box_10.index('fish')))

# Empty Box 1
box_1 = []

# Put the glasses and the whistle and the toy into Box 7
box_7.extend(['glasses', 'whistle', 'toy'])

# Remove the shelf and the guitar and the horse from Box 2
box_2 = []

# Put the crown and the grass into Box 2
box_2.extend(['crown', 'grass'])

# Put the horn and the makeup into Box 1
box_1.extend(['horn', 'makeup'])

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