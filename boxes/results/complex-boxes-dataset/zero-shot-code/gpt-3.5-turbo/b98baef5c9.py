box_0 = ['telescope', 'drum']
box_1 = ['sock', 'shorts', 'mixer', 'note']
box_2 = ['camera', 'gloves', 'moon']
box_3 = ['plate']
box_4 = ['candle']

# Move gloves from Box 2 to Box 0
box_0.append(box_2.pop(box_2.index('gloves')))

# Swap drum in Box 0 with sock in Box 1
box_0.append(box_1.pop(box_1.index('sock')))
box_1.append(box_0.pop(box_0.index('drum')))

# Put belt and drum into Box 1
box_1.extend(['belt', 'drum'])

# Move gloves, sock, and telescope from Box 0 to Box 4
box_4.extend([box_0.pop(box_0.index('gloves')), box_0.pop(box_0.index('sock')), box_0.pop(box_0.index('telescope'))])

# Remove camera and moon from Box 2
box_2.remove('camera')
box_2.remove('moon')

# Move sock and telescope from Box 4 to Box 2
box_2.extend([box_4.pop(box_4.index('sock')), box_4.pop(box_4.index('telescope'))])

# Move candle and gloves from Box 4 to Box 2
box_2.extend([box_4.pop(box_4.index('candle')), box_4.pop(box_4.index('gloves'))])

# Move plate from Box 3 to Box 2
box_2.append(box_3.pop())

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)