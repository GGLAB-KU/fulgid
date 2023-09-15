box_0 = ['freezer']
box_1 = ['butterfly', 'coin', 'mask', 'lion']
box_2 = []
box_3 = ['lightning']
box_4 = ['bracelet', 'scarf', 'dice', 'toaster']
box_5 = ['cup']
box_6 = ['bicycle', 'lamp', 'harmonica']
box_7 = ['sculpture', 'boat', 'submarine', 'scissors']
box_8 = ['storm']
box_9 = ['violin']
box_10 = ['belt', 'rain', 'branch', 'helmet', 'note']

box_9.append('magnet')
box_6.remove('harmonica')
box_6.append('swimsuit')
box_0, box_10 = box_10, box_0
box_1.append('storm')
box_7.append('guitar')
box_4.extend(['lamp', 'bicycle', 'swimsuit'])
box_1.remove('coin')
box_1.remove('storm')
box_1.extend(['forest', 'flower'])
box_9.append('lightning')
box_7, box_4 = box_4, box_7
box_5 = ['paint']
box_8.extend(['perfume', 'butterfly', 'tape'])
box_10, box_0 = box_0, box_10
box_10.remove('note')
box_8.remove('butterfly')
box_8.extend(['cow', 'leaf', 'cup'])
box_5, box_2 = box_2, box_5
box_9, box_4 = box_4, box_9

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