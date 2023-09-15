box_0 = ['desert', 'shelf', 'fish', 'glasses', 'grass']
box_1 = ['mixer']
box_2 = ['polish', 'shark', 'mountain', 'necklace', 'flute']
box_3 = ['seaweed', 'controller', 'dice', 'button']
box_4 = ['bracelet', 'needle', 'harmonica', 'sandals', 'meteor']
box_5 = ['elephant', 'moon', 'ring', 'console', 'shampoo']
box_6 = ['leaf']
box_7 = ['shoes', 'piano', 'paint', 'microscope']
box_8 = []

# Put the toaster and the usb into Box 6
box_6.extend(['toaster', 'usb'])

# Swap the shoes in Box 7 with the grass in Box 0
box_0[box_0.index('grass')], box_7[box_7.index('shoes')] = box_7[box_7.index('shoes')], box_0[box_0.index('grass')]

# Put the crown and the controller into Box 2
box_2.extend(['crown', 'controller'])

# Move the moon and the ring and the console from Box 5 to Box 2
box_2.extend([box_5.pop(box_5.index('moon')), box_5.pop(box_5.index('ring')), box_5.pop(box_5.index('console'))])

# Replace the dice and the controller and the button with the chair and the blender and the pan in Box 3
box_3[box_3.index('dice')] = 'chair'
box_3[box_3.index('controller')] = 'blender'
box_3[box_3.index('button')] = 'pan'

# Swap the mixer in Box 1 with the harmonica in Box 4
box_1[box_1.index('mixer')], box_4[box_4.index('harmonica')] = box_4[box_4.index('harmonica')], box_1[box_1.index('mixer')]

# Put the octopus into Box 4
box_4.append('octopus')

# Put the flute into Box 2
box_2.append('flute')

# Replace the ring with the pen in Box 2
box_2[box_2.index('ring')] = 'pen'

# Swap the meteor in Box 4 with the shark in Box 2
box_4[box_4.index('meteor')], box_2[box_2.index('shark')] = box_2[box_2.index('shark')], box_4[box_4.index('meteor')]

# Remove the shampoo and the elephant from Box 5
box_5.remove('shampoo')
box_5.remove('elephant')

# Move the microscope and the paint and the piano from Box 7 to Box 1
box_1.extend([box_7.pop(box_7.index('microscope')), box_7.pop(box_7.index('paint')), box_7.pop(box_7.index('piano'))])

# Remove the shoes and the shelf from Box 0
box_0.remove('shoes')
box_0.remove('shelf')

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