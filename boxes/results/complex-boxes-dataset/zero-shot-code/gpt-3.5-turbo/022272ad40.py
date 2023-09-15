box_0 = ['tree']
box_1 = ['battery', 'candle', 'cloud']
box_2 = ['card', 'pillow', 'blender', 'charger', 'pants']
box_3 = ['mask', 'soap', 'dog']
box_4 = ['thread', 'snow']
box_5 = ['puzzle', 'vase']
box_6 = ['boot']
box_7 = ['bus', 'usb']
box_8 = ['flute', 'glasses', 'spoon']
box_9 = []
box_10 = []
box_11 = ['bag', 'brush', 'wallet', 'microscope', 'seaweed']
box_12 = ['ocean']

# Swap battery in Box 1 with ocean in Box 12
box_1.remove('battery')
box_12.remove('ocean')
box_1.append('ocean')
box_12.append('battery')

# Remove vase from Box 5
box_5.remove('vase')

# Remove blender from Box 2
box_2.remove('blender')

# Remove puzzle from Box 5
box_5.remove('puzzle')

# Replace soap with key in Box 3
box_3.remove('soap')
box_3.append('key')

# Move usb and bus from Box 7 to Box 1
box_7.remove('usb')
box_7.remove('bus')
box_1.append('usb')
box_1.append('bus')

# Move pillow from Box 2 to Box 12
box_2.remove('pillow')
box_12.append('pillow')

# Replace thread with toothbrush in Box 4
box_4.remove('thread')
box_4.append('toothbrush')

# Swap pillow in Box 12 with seaweed in Box 11
box_12.remove('pillow')
box_11.remove('seaweed')
box_12.append('seaweed')
box_11.append('pillow')

# Swap pillow in Box 11 with snow in Box 4
box_11.remove('pillow')
box_4.remove('snow')
box_11.append('snow')
box_4.append('pillow')

# Swap tree in Box 0 with mask in Box 3
box_0.remove('tree')
box_3.remove('mask')
box_0.append('mask')
box_3.append('tree')

# Swap mask in Box 0 with pillow in Box 4
box_0.remove('mask')
box_4.remove('pillow')
box_0.append('pillow')
box_4.append('mask')

# Put vase into Box 6
box_6.append('vase')

# Put moon into Box 12
box_12.append('moon')

# Remove toothbrush from Box 4
box_4.remove('toothbrush')

# Remove cloud from Box 1
box_1.remove('cloud')

# Swap vase in Box 6 with key in Box 3
box_6.remove('vase')
box_3.remove('key')
box_6.append('key')
box_3.append('vase')

# Remove candle and bus from Box 1
box_1.remove('candle')
box_1.remove('bus')

# Put cat and tape into Box 10
box_10.append('cat')
box_10.append('tape')

# Replace spoon and flute with planet and basket in Box 8
box_8.remove('spoon')
box_8.remove('flute')
box_8.append('planet')
box_8.append('basket')

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