box_0 = ['necklace', 'truck', 'thread', 'car']
box_1 = ['mirror', 'pan', 'doll', 'toaster']
box_2 = ['tape', 'candle', 'gloves', 'mask']
box_3 = ['island', 'sock', 'speaker', 'flower', 'boot']
box_4 = []

box_0 = []
box_2[box_2.index('tape')] = box_1[box_1.index('doll')]
box_1.remove('pan')
box_3 = []
box_2.remove('candle')
box_2.remove('doll')
box_2.remove('gloves')
box_1.remove('toaster')
box_1.remove('mirror')
box_1.remove('tape')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)