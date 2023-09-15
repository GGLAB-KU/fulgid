box_0 = ['table', 'helmet']
box_1 = ['bag', 'belt', 'shirt', 'flute', 'needle']
box_2 = ['desert', 'lion']
box_3 = ['cat', 'key', 'controller', 'horn', 'toothpaste']
box_4 = ['bell', 'keyboard', 'bird', 'horse']
box_5 = []
box_6 = ['chair', 'leaf', 'perfume']

box_6.remove('perfume')
box_6.remove('leaf')
box_6.remove('chair')

box_1.append(box_4.pop(box_4.index('bird')))

box_5.extend([box_3.pop(box_3.index('controller')), box_3.pop(box_3.index('cat')), box_3.pop(box_3.index('toothpaste'))])

box_0[box_0.index('helmet')] = 'fish'

box_2.clear()

box_6.extend(['glove', 'submarine'])

box_0.append('card')

box_3.remove('horn')

box_1.remove('belt')
box_1.remove('flute')

box_6.append('storm')

box_0.remove('table')
box_0.remove('card')
box_0.remove('fish')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)