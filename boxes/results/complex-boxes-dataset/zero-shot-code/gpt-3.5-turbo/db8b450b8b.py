box_0 = []
box_1 = ['telescope', 'glasses', 'wallet', 'bicycle']
box_2 = ['mask', 'planet', 'forest', 'shoe', 'phone']
box_3 = ['pillow', 'river', 'soap', 'sun']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)

# Put the soap into Box 3
box_3.append('soap')

# Move the pillow and the soap from Box 3 to Box 1
box_1.extend(['pillow', 'soap'])
box_3.remove('pillow')
box_3.remove('soap')

# Swap the forest in Box 2 with the dress in Box 3
box_2[2], box_3[1] = box_3[1], box_2[2]

# Put the oven into Box 2
box_2.append('oven')

# Put the scarf and the needle into Box 3
box_3.extend(['scarf', 'needle'])

# Move the soap from Box 1 to Box 3
box_3.append(box_1.pop(box_1.index('soap')))

print("\nAfter modifications:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)