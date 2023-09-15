box_0 = ['bicycle']
box_1 = []
box_2 = ['toothpaste', 'pan', 'flower', 'fork']
box_3 = ['shorts', 'meteor', 'microscope', 'telescope', 'rocket']
box_4 = ['skirt']
box_5 = ['clock', 'pot']
box_6 = ['piano']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)

box_6.extend(['flute', 'pen'])
box_5[0] = 'desert'
box_5.remove('pot')
box_5.remove('desert')
box_6[0] = 'pot'
box_6[1] = 'laptop'
box_2.remove('pan')
box_2.remove('flower')
box_5.extend(['pan', 'flower'])
box_4.remove('skirt')
box_6.append('skirt')
box_6.remove('pot')
box_6.append('toothpaste')
box_1.extend(['toothpaste', 'piano'])
box_3[2] = 'thread'
box_3[4] = 'comet'
box_6.clear()
box_2.extend(['shorts', 'comet', 'meteor'])

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)