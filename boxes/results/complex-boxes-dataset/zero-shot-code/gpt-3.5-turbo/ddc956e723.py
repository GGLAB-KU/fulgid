box_0 = ['necklace']
box_1 = []
box_2 = ['tie', 'cat', 'magnet']
box_3 = ['guitar', 'tree', 'belt', 'razor', 'coat']
box_4 = ['sculpture']
box_5 = ['pen', 'flute', 'controller', 'game', 'glove']
box_6 = ['fish', 'jacket', 'toy']
box_7 = ['toothbrush', 'tiger', 'octopus', 'elephant']
box_8 = ['scarf', 'toaster', 'desert', 'shirt']
box_9 = ['pillow', 'bear', 'rocket', 'earring']
box_10 = ['wig', 'shoe']
box_11 = ['polish', 'needle', 'shampoo', 'whistle', 'pants']

box_6 = []
box_4.append(box_8.pop(box_8.index('sculpture')))
box_7.remove('octopus')
box_5.extend(['basket', 'book', 'truck'])
box_4.extend([box_2.pop(box_2.index('cat')), box_2.pop(box_2.index('tie')), box_2.pop(box_2.index('magnet'))])
box_7.remove('toothbrush')
box_7.remove('elephant')
box_3.remove('guitar')
box_3.remove('tree')
box_5.remove('glove')
box_7.append('boat')
box_0, box_4 = box_4, box_0
box_6.extend([box_9.pop(box_9.index('earring')), box_9.pop(box_9.index('pillow'))])
box_0.extend([box_6.pop(box_6.index('earring')), box_6.pop(box_6.index('pillow'))])
box_0, box_4 = box_4, box_0
box_4, box_0 = box_0, box_4
box_10 = []
box_7.extend([box_8.pop(box_8.index('scarf')), box_8.pop(box_8.index('toaster'))])
box_9.remove('bear')
box_9.remove('rocket')
box_3, box_7 = box_7, box_3
box_4, box_8 = box_8, box_4

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