box_0 = ['tree', 'vase', 'puzzle', 'rocket', 'starfish']
box_1 = ['toothpaste', 'lock', 'ship', 'toaster', 'cloud']
box_2 = ['shirt', 'bracelet', 'sculpture', 'camera']
box_3 = ['bicycle', 'motorcycle', 'clock', 'wire', 'key']
box_4 = ['doll', 'dolphin', 'button', 'spoon']
box_5 = ['sock', 'game', 'candle', 'tape']
box_6 = ['storm', 'needle', 'plane']
box_7 = ['headphone', 'blanket', 'perfume', 'thread', 'horse']
box_8 = ['shoes', 'violin', 'freezer', 'hat', 'submarine']
box_9 = ['branch', 'rock', 'star', 'boot']

box_9.remove('rock')
box_9.remove('star')
box_9.append('watch')
box_9.append('fridge')

box_8.remove('shoes')

box_0.remove('puzzle')
box_0.remove('rocket')
box_0.append('magnet')
box_0.append('cow')

box_2.remove('camera')

box_1.remove('ship')
box_1.remove('toothpaste')
box_1.remove('toaster')
box_7.extend(['ship', 'toothpaste', 'toaster'])

box_5.remove('tape')
box_5.remove('candle')
box_5.remove('sock')
box_8.extend(['tape', 'candle', 'sock'])

box_4.remove('button')

box_6.remove('needle')
box_4.remove('dolphin')
box_6.append('dolphin')
box_4.append('needle')

box_8.remove('sock')

box_8.remove('hat')
box_8.remove('violin')
box_8.remove('candle')
box_8.append('comet')
box_8.append('bear')
box_8.append('towel')

box_5.remove('game')

box_8.remove('comet')
box_8.remove('bear')
box_8.remove('freezer')
box_7.extend(['comet', 'bear', 'freezer'])

box_2.remove('bracelet')
box_2.append('wire')

box_8.extend(['pillow', 'wig', 'usb'])

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