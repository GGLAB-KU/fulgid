box0 = ['comet']
box1 = ['glasses']
box2 = ['shoes', 'phone']
box3 = ['wallet']
box4 = ['glove', 'motorcycle', 'shorts', 'bell', 'frame']

# Swap wallet in box3 with glasses in box1
box3, box1 = box1, box3

# Move glasses from box3 to box1
box1.extend(box3)
box3 = []

# Put dog, button, and battery into box4
box4.extend(['dog', 'button', 'battery'])

# Put rocket into box4
box4.append('rocket')

# Remove button from box4
box4.remove('button')

# Put paint and pot into box4
box4.extend(['paint', 'pot'])

# Put thunder into box4
box4.append('thunder')

# Move comet from box0 to box4
box4.append(box0.pop())

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)