box_0 = ['star', 'toothbrush', 'razor']
box_1 = []
box_2 = ['makeup', 'glove']
box_3 = ['magnet', 'car', 'mirror', 'pen', 'cow']
box_4 = ['shark', 'zipper', 'mask', 'chair']
box_5 = ['laptop', 'shoe', 'starfish']
box_6 = ['wire']
box_7 = []
box_8 = ['leaf', 'piano']
box_9 = ['seaweed']

box_0.remove('pot')
box_0.append('frame')

box_5.remove('oven')
box_9.remove('seaweed')
box_9.append('oven')

box_8.remove('piano')
box_3.append('piano')

box_9.remove('oven')
box_9.append('toaster')

box_2.append('tree')
box_2.append('pan')

box_6.remove('wire')
box_6.append('game')

box_2.remove('sun')
box_2.remove('horn')
box_2.remove('pan')

box_6.remove('game')
box_6.append('swimsuit')

box_3.remove('cow')
box_3.remove('mirror')
box_3.remove('pen')
box_4.append('cow')
box_4.append('mirror')
box_4.append('pen')

box_8 = []

box_2.append('oven')
box_2.append('meteor')

box_3.remove('car')
box_3.append('fork')

box_3.remove('piano')
box_3.remove('magnet')
box_7.append('piano')
box_7.append('magnet')

box_1.append('doll')
box_1.append('tiger')
box_1.append('planet')

box_3.remove('fork')
box_6.remove('swimsuit')
box_3.append('swimsuit')

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