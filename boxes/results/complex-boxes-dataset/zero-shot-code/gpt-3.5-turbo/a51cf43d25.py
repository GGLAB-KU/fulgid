box0 = []
box1 = ['violin', 'phone', 'chair', 'toothbrush']
box2 = ['zipper']
box3 = ['lipstick', 'clock', 'lightning']
box4 = ['cat', 'cloud', 'table', 'polish']

# Remove items from Box 4
box4.remove('cat')
box4.remove('cloud')
box4.remove('polish')
box4.remove('table')

# Swap items between Box 1 and Box 3
box1.remove('violin')
box3.remove('clock')
box1.append('clock')
box3.append('violin')

# Swap items between Box 2 and Box 3
box2.remove('zipper')
box3.remove('lipstick')
box2.append('lipstick')
box3.append('zipper')

# Replace toothbrush with truck in Box 1
box1.remove('toothbrush')
box1.append('truck')

# Remove truck from Box 1
box1.remove('truck')

# Move lipstick from Box 2 to Box 0
box0.append(box2.pop(0))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)