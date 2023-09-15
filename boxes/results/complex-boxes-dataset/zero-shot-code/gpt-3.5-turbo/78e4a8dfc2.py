box0 = ['ocean', 'key', 'tiger', 'whistle']
box1 = ['forest', 'chair', 'telescope', 'tree']
box2 = ['shark']
box3 = ['mirror', 'paint', 'snow', 'microwave', 'scarf']

# Remove items from Box 0
box0.remove('ocean')
box0.remove('key')
box0.remove('whistle')

# Move shark from Box 2 to Box 3
box3.append(box2.pop(0))

# Replace telescope with whistle in Box 1
box1.remove('telescope')
box1.append('whistle')

# Remove items from Box 1
box1.remove('forest')
box1.remove('chair')
box1.remove('tree')

# Remove items from Box 3
box3.remove('shark')
box3.remove('scarf')
box3.remove('paint')

# Move whistle from Box 1 to Box 2
box2.append(box1.pop(box1.index('whistle')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)