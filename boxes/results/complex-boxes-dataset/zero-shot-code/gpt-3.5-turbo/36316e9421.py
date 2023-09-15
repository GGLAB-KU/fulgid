box0 = ['toothbrush']
box1 = ['toy', 'ocean']
box2 = ['elephant', 'gloves', 'horse', 'tiger', 'needle']
box3 = ['desert']

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)

# Move the desert from Box 3 to Box 0
box0.extend(box3)
box3.clear()

# Remove the toothbrush from Box 0
box0.remove('toothbrush')

# Remove the ocean and the toy from Box 1
box1.remove('ocean')
box1.remove('toy')

# Move the desert from Box 0 to Box 3
box3.extend(box0)
box0.clear()

# Move the desert from Box 3 to Box 0
box0.extend(box3)
box3.clear()

# Replace the elephant with the fish in Box 2
box2.remove('elephant')
box2.append('fish')

print("\nAfter modifications:")
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)