box_0 = []
box_1 = ['fridge', 'submarine']
box_2 = []
box_3 = ['charger', 'jungle']
box_4 = ['fish', 'boot', 'bear', 'car']
box_5 = ['telescope', 'branch', 'seaweed', 'bowl', 'bird']

box_5.remove('seaweed')
box_5.remove('bowl')

box_3.remove('jungle')
box_3.remove('charger')

box_4.remove('car')
box_5.remove('branch')
box_4.append('branch')

box_4.extend(['flute', 'mixer'])
box_4.remove('boot')
box_4.remove('branch')
box_4.remove('mixer')

box_1.remove('submarine')
box_5.remove('telescope')
box_1.append('telescope')

box_1.remove('fridge')
box_2.append('fridge')

box_2.remove('fridge')
box_4.append('fridge')

box_1.append('planet')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)