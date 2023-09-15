box_0 = ['plane']
box_1 = ['dress']
box_2 = ['razor', 'oven', 'tiger', 'glasses']
box_3 = ['bracelet']
box_4 = []
box_5 = ['horse', 'necklace', 'ship']

box_3.remove('bracelet')
box_3.append('sun')

box_3.remove('sun')
box_4.append('sun')

box_2.remove('razor')
box_2.remove('oven')
box_2.remove('tiger')
box_2.remove('glasses')
box_2.append('umbrella')
box_2.append('ocean')
box_2.append('shoes')

box_4.remove('sun')
box_4.append('clock')

box_1.remove('dress')
box_1.append('umbrella')

box_5.append('rocket')
box_5.append('tape')

box_0.remove('plane')
box_1.append('plane')

box_2.remove('umbrella')
box_2.remove('ocean')
box_2.remove('shoes')
box_2.append('lock')
box_2.append('blanket')
box_2.append('bag')

box_3.append('guitar')
box_3.append('swimsuit')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)