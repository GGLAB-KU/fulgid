box_0 = ['tape', 'mixer', 'paint']
box_1 = ['lightning', 'apple', 'rain']
box_2 = []
box_3 = ['dress', 'pan']
box_4 = ['cow', 'umbrella', 'lock', 'phone']
box_5 = ['butterfly', 'watch']
box_6 = []
box_7 = ['game', 'table', 'freezer']
box_8 = []
box_9 = ['perfume', 'charger']
box_10 = ['vase', 'shorts', 'polish', 'forest']
box_11 = ['toaster', 'controller', 'doll', 'tree', 'lamp']
box_12 = []
box_13 = ['violin', 'chair', 'belt', 'coral', 'dolphin']
box_14 = ['toothbrush', 'needle', 'coin']

box_14.remove('toothbrush')
box_14.remove('coin')
box_14.append('puzzle')
box_14.append('microscope')
box_14.append('controller')

box_11.remove('toaster')
box_11.remove('tree')
box_11.remove('lamp')

box_1.remove('apple')
box_3.remove('dress')
box_1.append('dress')
box_3.append('apple')

box_3.remove('apple')

box_3.remove('pan')
box_10.remove('shorts')
box_3.append('shorts')
box_5.append('shorts')

box_8.append('vase')

box_6.append('polish')
box_6.append('dolphin')

box_4.remove('phone')
box_4.remove('umbrella')
box_4.remove('lock')
box_10.append('phone')
box_10.append('umbrella')
box_10.append('lock')

box_10.remove('forest')
box_8.remove('vase')
box_10.append('vase')
box_8.append('forest')

box_5.remove('butterfly')
box_5.append('elephant')

box_1.remove('rain')
box_0.remove('tape')
box_0.remove('mixer')
box_0.remove('paint')
box_1.append('paint')
box_0.append('rain')

box_9.remove('perfume')
box_9.remove('charger')
box_1.append('perfume')
box_1.append('charger')

box_3.append('bell')
box_3.append('snow')

box_11.remove('doll')
box_4.append('doll')

box_13.remove('violin')
box_10.remove('pan')
box_13.append('pan')
box_10.append('violin')

box_7.remove('table')
box_5.remove('shorts')
box_7.append('shorts')

box_0.remove('paint')
box_0.remove('tape')
box_0.append('pants')
box_0.append('sock')

box_6.remove('dolphin')

box_12.append('keyboard')
box_12.append('dolphin')
box_12.append('river')

box_10.remove('phone')
box_12.append('phone')

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
print("Box 13:", box_13)
print("Box 14:", box_14)