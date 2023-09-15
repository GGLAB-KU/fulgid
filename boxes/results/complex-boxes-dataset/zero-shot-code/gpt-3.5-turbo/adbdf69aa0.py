box0 = ['grinder']
box1 = ['planet', 'toy', 'toaster', 'star']
box2 = []
box3 = ['note', 'microscope', 'coat', 'butterfly', 'bowl']
box4 = ['dolphin', 'phone', 'rain', 'bell', 'button']
box5 = ['river']
box6 = ['clock', 'pants', 'towel', 'train', 'submarine']

# Remove phone and bell from box4
box4.remove('phone')
box4.remove('bell')

# Swap grinder in box0 with note in box3
box0[0], box3[0] = box3[0], box0[0]

# Put paint and candle into box2
box2.extend(['paint', 'candle'])

# Put thunder and earring into box0
box0.extend(['thunder', 'earring'])

# Remove toy from box1
box1.remove('toy')

# Replace planet and toaster with helmet and storm in box1
box1.remove('planet')
box1.remove('toaster')
box1.extend(['helmet', 'storm'])

# Move coat from box3 to box6
box6.append(box3.pop(box3.index('coat')))

# Remove river from box5
box5.remove('river')

# Remove pants, coat, and train from box6
box6.remove('pants')
box6.remove('coat')
box6.remove('train')

# Put magnet into box2
box2.append('magnet')

# Put table, key, and bicycle into box2
box2.extend(['table', 'key', 'bicycle'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)