box0 = ['branch']
box1 = ['plane', 'bus']
box2 = ['battery']
box3 = ['pen', 'toothpaste', 'toothbrush', 'beach']
box4 = ['thunder', 'controller', 'clock', 'rain']

# Swap rain in Box 4 with toothbrush in Box 3
box3.remove('toothbrush')
box4.remove('rain')
box3.append('rain')
box4.append('toothbrush')

# Replace battery with ocean in Box 2
box2.remove('battery')
box2.append('ocean')

# Put mask into Box 1
box1.append('mask')

# Put tape into Box 3
box3.append('tape')

# Replace plane, mask, and bus with dolphin, laptop, and violin in Box 1
box1.remove('plane')
box1.remove('mask')
box1.remove('bus')
box1.append('dolphin')
box1.append('laptop')
box1.append('violin')

# Move branch from Box 0 to Box 2
box0.remove('branch')
box2.append('branch')

# Move controller, thunder, and clock from Box 4 to Box 2
box4.remove('controller')
box4.remove('thunder')
box4.remove('clock')
box2.append('controller')
box2.append('thunder')
box2.append('clock')

# Replace dolphin and laptop with whistle and candle in Box 1
box1.remove('dolphin')
box1.remove('laptop')
box1.append('whistle')
box1.append('candle')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)