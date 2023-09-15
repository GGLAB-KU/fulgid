box_0 = ['flower', 'bell', 'coin', 'violin']
box_1 = ['usb', 'microscope', 'coat']
box_2 = ['thunder', 'tape']
box_3 = ['toothbrush', 'battery', 'speaker']
box_4 = ['snow', 'needle']
box_5 = []
box_6 = ['whistle', 'shorts', 'plane', 'plate']
box_7 = ['car']
box_8 = ['cow', 'watch', 'microwave', 'frame', 'lion']
box_9 = ['chair', 'crown', 'octopus', 'rocket']
box_10 = ['pants', 'doll', 'tree', 'shoes', 'puzzle']
box_11 = ['boot']
box_12 = ['lock', 'starfish', 'phone', 'cat']
box_13 = ['horn', 'clock', 'flute', 'freezer', 'bird']

box_11.remove('boot')
box_11.append('drum')

box_1.remove('microscope')
box_1.append('thunder')

box_12.remove('starfish')
box_3.remove('battery')
box_12.append('battery')
box_3.append('starfish')

box_13.append('octopus')
box_13.append('blanket')

box_6.remove('plane')
box_6.remove('whistle')
box_4.append('plane')
box_4.append('whistle')

box_8.remove('watch')
box_9.append('watch')

box_13.remove('octopus')
box_7.append('octopus')

box_11.remove('drum')
box_1.append('drum')

box_2.remove('thunder')
box_1.append('thunder')

box_1.remove('thunder')
box_1.remove('drum')
box_1.append('mixer')
box_1.append('rock')

box_1.remove('rock')
box_9.remove('watch')
box_1.append('watch')
box_9.append('rock')

box_13.remove('bird')

box_6.remove('shorts')
box_6.remove('plate')
box_5.append('shorts')
box_5.append('plate')

box_13.remove('horn')
box_10.append('horn')

box_2.remove('tape')
box_2.append('toaster')

box_9.remove('crown')
box_7.remove('car')
box_9.append('car')
box_7.append('crown')

box_13.remove('freezer')
box_4.remove('plane')
box_13.append('plane')
box_4.append('freezer')

box_7.remove('octopus')
box_13.append('octopus')

box_4.append('octopus')

box_6.append('earring')
box_6.append('necklace')
box_6.append('speaker')

box_2.remove('toaster')

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