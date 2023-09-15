box_0 = ['button', 'gloves']
box_1 = ['needle', 'headphone', 'tiger', 'submarine']
box_2 = ['wallet']
box_3 = ['sandals']
box_4 = ['comet', 'bracelet', 'dress', 'grass', 'microscope']
box_5 = ['branch']
box_6 = ['car', 'rock', 'usb']
box_7 = ['glove', 'cup', 'fridge']
box_8 = ['shoes', 'pan', 'skirt']

box_7.remove('glove')
box_7.remove('cup')
box_7.remove('fridge')

box_5.remove('branch')

box_0.clear()

box_4.remove('tiger')
box_4.append('shampoo')

box_6.remove('usb')
box_6.extend(['dress', 'fork'])

box_2, box_6 = box_6, box_2

box_6.remove('rock')

box_1.remove('needle')
box_5.append('needle')

box_8, box_2 = box_2, box_8

box_4.remove('shampoo')
box_4.remove('microscope')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)