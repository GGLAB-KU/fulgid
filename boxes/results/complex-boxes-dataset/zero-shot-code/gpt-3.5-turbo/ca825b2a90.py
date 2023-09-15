box_0 = ['doll', 'swimsuit', 'shoes', 'lion', 'tie']
box_1 = ['microwave', 'pillow']
box_2 = ['mountain', 'card', 'lamp']
box_3 = ['bracelet', 'puzzle']
box_4 = ['dress']
box_5 = ['phone']
box_6 = ['river', 'whistle', 'drum', 'seaweed', 'apple']
box_7 = ['polish', 'pan']

# Swap phone in Box 5 with lion in Box 0
box_0.remove('lion')
box_5.remove('phone')
box_0.append('phone')
box_5.append('lion')

# Move phone, doll, and shoes from Box 0 to Box 5
box_0.remove('phone')
box_0.remove('doll')
box_0.remove('shoes')
box_5.append('phone')
box_5.append('doll')
box_5.append('shoes')

# Remove shoes, lion, and phone from Box 5
box_5.remove('shoes')
box_5.remove('lion')
box_5.remove('phone')

# Put car, shoe, and forest into Box 7
box_7.append('car')
box_7.append('shoe')
box_7.append('forest')

# Replace microwave and pillow with ship and mixer in Box 1
box_1.remove('microwave')
box_1.remove('pillow')
box_1.append('ship')
box_1.append('mixer')

# Move mountain, lamp, and card from Box 2 to Box 0
box_2.remove('mountain')
box_2.remove('lamp')
box_2.remove('card')
box_0.append('mountain')
box_0.append('lamp')
box_0.append('card')

# Swap mountain in Box 0 with mixer in Box 1
box_0.remove('mountain')
box_1.remove('mixer')
box_0.append('mixer')
box_1.append('mountain')

# Swap pan in Box 7 with drum in Box 6
box_7.remove('pan')
box_6.remove('drum')
box_7.append('drum')
box_6.append('pan')

# Put skirt and harmonica into Box 4
box_4.append('skirt')
box_4.append('harmonica')

# Put sun into Box 4
box_4.append('sun')

# Swap dress in Box 4 with doll in Box 5
box_4.remove('dress')
box_5.remove('doll')
box_4.append('doll')
box_5.append('dress')

# Remove ship and mountain from Box 1
box_1.remove('ship')
box_1.remove('mountain')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)