box0 = ['clock', 'shark', 'tape', 'train']
box1 = []
box2 = ['bell', 'battery', 'magnet', 'candle', 'earring']
box3 = ['plane', 'mixer']
box4 = ['bear']
box5 = ['bag', 'pillow', 'scissors']
box6 = ['cow', 'tiger']
box7 = ['violin']

# Move the violin from Box 7 to Box 5
box5.append(box7.pop(box7.index('violin')))

# Swap the magnet in Box 2 with the clock in Box 0
box0[box0.index('clock')], box2[box2.index('magnet')] = box2[box2.index('magnet')], box0[box0.index('clock')]

# Swap the tiger in Box 6 with the mixer in Box 3
box3[box3.index('mixer')], box6[box6.index('tiger')] = box6[box6.index('tiger')], box3[box3.index('mixer')]

# Put the toaster and the clock and the sock into Box 7
box7.extend(['toaster', 'clock', 'sock'])

# Remove the cow and the mixer from Box 6
box6.remove('cow')
box6.remove('mixer')

# Put the towel and the freezer into Box 7
box7.extend(['towel', 'freezer'])

# Remove the towel and the clock from Box 7
box7.remove('towel')
box7.remove('clock')

# Swap the pillow in Box 5 with the sock in Box 7
box5[box5.index('pillow')], box7[box7.index('sock')] = box7[box7.index('sock')], box5[box5.index('pillow')]

# Put the shampoo and the grass into Box 5
box5.extend(['shampoo', 'grass'])

# Swap the train in Box 0 with the bell in Box 2
box0[box0.index('train')], box2[box2.index('bell')] = box2[box2.index('bell')], box0[box0.index('train')]

# Put the apple and the bicycle and the horse into Box 7
box7.extend(['apple', 'bicycle', 'horse'])

# Move the bear from Box 4 to Box 5
box5.append(box4.pop(box4.index('bear')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
print("Box 7:", box7)