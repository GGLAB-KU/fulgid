box_0 = []
box_1 = ['swimsuit']
box_2 = []
box_3 = []
box_4 = ['motorcycle', 'river', 'grinder']
box_5 = ['car', 'tape', 'rocket', 'violin', 'book']
box_6 = ['sock', 'shelf', 'tiger', 'grass', 'cow']

box_4.append('flute')
box_4.append('crown')

box_1.remove('swimsuit')

box_4.extend(box_5.pop(box_5.index('book')))
box_4.extend(box_5.pop(box_5.index('tape')))

box_5[box_5.index('violin')], box_6[box_6.index('shelf')] = box_6[box_6.index('shelf')], box_5[box_5.index('violin')]

box_6[box_6.index('tiger')] = 'pot'

box_4.append('coral')

box_5.extend(box_6.pop(box_6.index('cow')))
box_5.extend(box_6.pop(box_6.index('pot')))
box_5.extend(box_6.pop(box_6.index('sock')))

box_4[box_4.index('motorcycle')], box_5[box_5.index('shelf')] = box_5[box_5.index('shelf')], box_4[box_4.index('motorcycle')]

box_4.remove('book')
box_4.remove('grinder')
box_4.remove('crown')

box_0.append('bracelet')

box_5.remove('pot')
box_5.remove('motorcycle')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)