box0 = ['polish', 'shirt']
box1 = ['tree', 'pen', 'apple', 'bell']
box2 = ['seaweed', 'wire']
box3 = ['gloves', 'mask']
box4 = ['button', 'planet', 'dice', 'lock', 'necklace']
box5 = ['sandals', 'chair', 'wallet']

box4.remove('necklace')
box4.remove('button')
box4.remove('dice')

box0.append('bell')
box0.append('tree')
box1.remove('bell')
box1.remove('tree')

box4.remove('lock')
box4.remove('planet')

box2.append('beach')
box2.append('bicycle')

box0.remove('polish')
box4.append('polish')

box1.remove('apple')

box5.remove('sandals')
box5 = []

box1.remove('seaweed')
box1.remove('beach')
box1.remove('wire')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)