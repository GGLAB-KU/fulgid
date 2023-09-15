box_0 = ['key']
box_1 = ['fish', 'sculpture', 'microscope']
box_2 = ['storm', 'car', 'coat', 'cat', 'hat']
box_3 = ['shoes', 'button', 'submarine', 'pen']
box_4 = ['toaster', 'glasses']
box_5 = ['comb', 'bicycle', 'bowl', 'table']
box_6 = ['drum']
box_7 = ['leaf', 'comet']
box_8 = ['lamp', 'zipper', 'bus', 'dolphin']

box_7.remove('comet')
box_7.append('keyboard')

box_1 = []

box_5.remove('bicycle')
box_5.remove('table')

box_8.remove('lamp')
box_5.append('lamp')

box_4.remove('glasses')
box_4.remove('toaster')
box_4.append('rock')
box_4.append('mixer')

box_7.remove('leaf')

box_2.remove('coat')
box_2.remove('cat')
box_2.remove('hat')
box_2.append('mountain')
box_2.append('shorts')
box_2.append('book')

box_6.remove('drum')
box_4.append('drum')

box_2.append('scissors')
box_2.append('shoes')
box_2.append('comb')

box_0.remove('key')

box_4.remove('mixer')
box_3.append('mixer')

box_3.remove('rock')
box_3.append('puzzle')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)