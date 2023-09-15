box0 = ['mountain', 'blanket', 'razor']
box1 = []
box2 = ['pan', 'pants', 'forest', 'vase', 'butterfly']
box3 = ['controller', 'umbrella', 'bicycle']
box4 = ['ring']

# Move the blanket, mountain, and razor from Box 0 to Box 4
box4.extend(box0)
box0.clear()

# Move the forest, pants, and butterfly from Box 2 to Box 0
box0.extend(box2[2:5])
box2 = box2[:2] + box2[5:]

# Swap the bicycle in Box 3 with the ring in Box 4
box3[2], box4[0] = box4[0], box3[2]

# Remove the mountain and the razor from Box 4
box4.remove('mountain')
box4.remove('razor')

# Remove the forest and the butterfly from Box 0
box0.remove('forest')
box0.remove('butterfly')

# Put the polish into Box 3
box3.append('polish')

# Remove the blanket from Box 4
box4.remove('blanket')

# Swap the ring in Box 3 with the pants in Box 0
box3[2], box0[1] = box0[1], box3[2]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)