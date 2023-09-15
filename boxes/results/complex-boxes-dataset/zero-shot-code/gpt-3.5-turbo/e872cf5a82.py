box0 = ['helmet', 'sock', 'violin']
box1 = ['bracelet', 'coat', 'bus', 'camera']
box2 = ['bicycle', 'ship', 'spoon']
box3 = ['fridge', 'bear', 'game']
box4 = ['coin', 'grass', 'razor', 'snow']
box5 = ['chair', 'motorcycle', 'cup']
box6 = []

# Move snow, grass, and coin from Box 4 to Box 0
box0.extend([box4.pop(box4.index('snow')), box4.pop(box4.index('grass')), box4.pop(box4.index('coin'))])

# Remove bear from Box 3
box3.remove('bear')

# Replace razor with mask in Box 4
box4[box4.index('razor')] = 'mask'

# Move fridge from Box 3 to Box 6
box6.append(box3.pop(box3.index('fridge')))

# Remove motorcycle and chair from Box 5
box5.remove('motorcycle')
box5.remove('chair')

# Put dolphin, candle, and laptop into Box 1
box1.extend(['dolphin', 'candle', 'laptop'])

# Swap bus in Box 1 with ship in Box 2
box1[box1.index('bus')], box2[box2.index('ship')] = box2[box2.index('ship')], box1[box1.index('bus')]

# Swap bicycle in Box 2 with fridge in Box 6
box2[box2.index('bicycle')], box6[box6.index('fridge')] = box6[box6.index('fridge')], box2[box2.index('bicycle')]

# Swap bicycle in Box 6 with camera in Box 1
box6[box6.index('bicycle')], box1[box1.index('camera')] = box1[box1.index('camera')], box6[box6.index('bicycle')]

# Move fridge and spoon from Box 2 to Box 6
box6.extend([box2.pop(box2.index('fridge')), box2.pop(box2.index('spoon'))])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)