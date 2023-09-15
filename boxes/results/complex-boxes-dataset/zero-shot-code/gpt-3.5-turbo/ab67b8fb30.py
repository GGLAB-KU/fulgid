box_0 = ['skirt', 'fork', 'island']
box_1 = ['sun', 'basket', 'tree', 'bowl', 'apple']
box_2 = ['soap', 'meteor', 'pen', 'controller', 'desert']
box_3 = ['planet']
box_4 = ['mixer', 'river', 'pants', 'mask']
box_5 = ['bicycle', 'toy']
box_6 = ['cow']
box_7 = ['telescope', 'watch']
box_8 = ['shirt', 'forest', 'lipstick']
box_9 = ['bag']
box_10 = ['book', 'branch', 'train', 'bell']
box_11 = ['bus', 'rocket']

# Swap toy in Box 5 with controller in Box 2
box_5.remove('toy')
box_2.remove('controller')
box_5.append('controller')
box_2.append('toy')

# Put shark, plane, and pants into Box 9
box_9.extend(['shark', 'plane', 'pants'])

# Move fork, skirt, and island from Box 0 to Box 5
box_0.remove('fork')
box_0.remove('skirt')
box_0.remove('island')
box_5.extend(['fork', 'skirt', 'island'])

# Replace fork, island, and bicycle with pan, boat, and laptop in Box 5
box_5.remove('fork')
box_5.remove('island')
box_5.remove('bicycle')
box_5.extend(['pan', 'boat', 'laptop'])

# Put comb into Box 3
box_3.append('comb')

# Remove forest, shirt, and lipstick from Box 8
box_8.remove('forest')
box_8.remove('shirt')
box_8.remove('lipstick')

# Empty Box 11
box_11.clear()

# Put star and bus into Box 2
box_2.extend(['star', 'bus'])

# Replace controller, pan, and boat with tie, earring, and mixer in Box 5
box_5.remove('controller')
box_5.remove('pan')
box_5.remove('boat')
box_5.extend(['tie', 'earring', 'mixer'])

# Empty Box 5
box_5.clear()

# Put branch into Box 0
box_0.append('branch')

# Remove pants and shark from Box 9
box_9.remove('pants')
box_9.remove('shark')

# Replace branch with shoes in Box 10
box_10.remove('branch')
box_10.append('shoes')

# Put wallet, lipstick, and vase into Box 2
box_2.extend(['wallet', 'lipstick', 'vase'])

# Empty Box 1
box_1.clear()

# Remove train and shoes from Box 10
box_10.remove('train')
box_10.remove('shoes')

# Put freezer into Box 3
box_3.append('freezer')

# Replace comb, freezer, and planet with key, pan, and bus in Box 3
box_3.remove('comb')
box_3.remove('freezer')
box_3.remove('planet')
box_3.extend(['key', 'pan', 'bus'])

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
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)