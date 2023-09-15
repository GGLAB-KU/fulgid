box_0 = ['pot', 'moon', 'train', 'grinder', 'paint']
box_1 = ['boat', 'soap', 'river', 'lightning']
box_2 = ['microscope', 'flute', 'rocket']
box_3 = ['card']
box_4 = ['glove']
box_5 = ['bicycle', 'submarine']
box_6 = ['jungle', 'helmet', 'basket', 'harmonica', 'storm']
box_7 = ['bus', 'watch', 'island']
box_8 = ['speaker', 'gloves', 'brush', 'mirror', 'ocean']

# Replace speaker, gloves, and mirror with toothpaste, spoon, and thunder in Box 8
box_8.remove('speaker')
box_8.remove('gloves')
box_8.remove('mirror')
box_8.append('toothpaste')
box_8.append('spoon')
box_8.append('thunder')

# Move rocket, flute, and microscope from Box 2 to Box 6
box_6.extend(box_2)
box_2.clear()

# Put skirt and battery into Box 3
box_3.append('skirt')
box_3.append('battery')

# Remove submarine and bicycle from Box 5
box_5.remove('submarine')
box_5.remove('bicycle')

# Remove boat and river from Box 1
box_1.remove('boat')
box_1.remove('river')

# Remove glove from Box 4 and put frame into Box 4
box_4.remove('glove')
box_4.append('frame')

# Put button into Box 2
box_2.append('button')

# Replace frame with dress in Box 4
box_4.remove('frame')
box_4.append('dress')

# Put shorts and drum into Box 3
box_3.append('shorts')
box_3.append('drum')

# Remove dress from Box 2
box_2.remove('dress')

# Move brush and spoon from Box 8 to Box 0
box_0.append('brush')
box_0.append('spoon')
box_8.remove('brush')
box_8.remove('spoon')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)