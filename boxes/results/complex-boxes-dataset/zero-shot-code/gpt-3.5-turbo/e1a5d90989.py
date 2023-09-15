box0 = []
box1 = ['book', 'desert', 'key', 'grinder', 'storm']
box2 = ['mixer', 'bell', 'brush', 'comb', 'violin']
box3 = ['microscope']

# Move microscope from Box 3 to Box 2
box2.append(box3.pop(0))

# Replace bell and violin with starfish and drum in Box 2
box2.remove('bell')
box2.remove('violin')
box2.append('starfish')
box2.append('drum')

# Replace desert and grinder with razor and mountain in Box 1
box1.remove('desert')
box1.remove('grinder')
box1.append('razor')
box1.append('mountain')

# Remove storm from Box 1
box1.remove('storm')

# Remove mountain and key from Box 1
box1.remove('mountain')
box1.remove('key')

# Replace razor with ship in Box 1
box1.remove('razor')
box1.append('ship')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)