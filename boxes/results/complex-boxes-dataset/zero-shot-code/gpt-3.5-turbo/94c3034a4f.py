box_0 = ['oven', 'usb', 'grinder']
box_1 = []
box_2 = ['train', 'comet', 'razor', 'harmonica', 'coat']
box_3 = ['sun', 'ocean', 'chair', 'mask', 'note']
box_4 = []

# Remove train, coat, and razor from box 2
box_2.remove('train')
box_2.remove('coat')
box_2.remove('razor')

# Swap oven in box 0 with sun in box 3
box_0.remove('oven')
box_3.remove('sun')
box_0.append('sun')
box_3.append('oven')

# Replace usb with blender in box 0
box_0.remove('usb')
box_0.append('blender')

# Move comet from box 2 to box 1
box_1.append(box_2.pop(box_2.index('comet')))

# Put flute into box 1
box_1.append('flute')

# Put dolphin into box 3
box_3.append('dolphin')

# Remove harmonica from box 2
box_2.remove('harmonica')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)