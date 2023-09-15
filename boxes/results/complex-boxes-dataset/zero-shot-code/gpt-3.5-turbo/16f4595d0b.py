box_0 = ['ring', 'phone', 'violin', 'wig']
box_1 = []
box_2 = ['shoes', 'tree', 'razor', 'tie']
box_3 = ['wallet', 'headphone']
box_4 = ['blender']
box_5 = ['shark', 'planet']
box_6 = ['beach', 'river', 'meteor', 'train']
box_7 = []
box_8 = ['hat', 'octopus']
box_9 = ['rain']
box_10 = ['lamp', 'shoe']
box_11 = ['coin', 'crown', 'bear', 'shampoo', 'shorts']
box_12 = ['star']

box_0.remove('glasses')
box_0.append('laptop')
box_0.remove('plate')
box_0.append('mountain')
box_0.append('guitar')
box_0.remove('bicycle')

box_10.remove('lamp')
box_10.append('guitar')

box_12.remove('star')
box_0.append('plate')

box_0.remove('plate')
box_12.append('plate')

box_9.remove('rain')
box_11.remove('crown')
box_9.append('crown')

box_0.remove('ring')
box_0.remove('laptop')
box_0.remove('mountain')
box_0.append('guitar')
box_0.append('bicycle')

box_8.extend(box_6)
box_6.clear()

box_3.remove('wallet')
box_5.remove('planet')
box_9.append('blender')

box_2.remove('shoes')
box_3.remove('headphone')
box_3.append('helmet')

box_11.remove('guitar')
box_11.append('guitar')

box_6.remove('river')
box_3.append('river')

box_11.remove('bear')

box_11.remove('shorts')
box_11.remove('coin')
box_11.remove('shampoo')
box_2.append('shorts')
box_2.append('coin')
box_2.append('shampoo')

box_11.remove('guitar')
box_11.remove('rain')
box_11.append('comb')
box_11.append('needle')

box_5, box_8 = box_8, box_5

box_6.extend(['toaster', 'tape'])

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
print("Box 12:", box_12)