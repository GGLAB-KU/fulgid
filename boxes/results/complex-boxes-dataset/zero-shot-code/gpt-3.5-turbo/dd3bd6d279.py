box0 = ['grass', 'leaf', 'makeup', 'razor', 'comet']
box1 = []
box2 = ['storm', 'console', 'butterfly', 'table', 'perfume']
box3 = ['rain']
box4 = []

# Swap the rain in Box 3 with the makeup in Box 0
box3[0], box0[2] = box0[2], box3[0]

# Swap the perfume in Box 2 with the makeup in Box 3
box2[4], box3[0] = box3[0], box2[4]

# Move the console and the makeup and the storm from Box 2 to Box 1
box1.extend([box2[1], box2[2], box2[0]])
box2.remove(box2[0])
box2.remove(box2[0])
box2.remove(box2[0])

# Move the rain and the grass from Box 0 to Box 2
box2.extend([box0[0], box0[3]])
box0.remove(box0[0])
box0.remove(box0[2])

# Remove the razor from Box 0
box0.remove(box0[1])

# Swap the perfume in Box 3 with the leaf in Box 0
box3[0], box0[1] = box0[1], box3[0]

# Move the leaf from Box 3 to Box 1
box1.append(box3[0])
box3.remove(box3[0])

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)