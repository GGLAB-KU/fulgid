box_0 = ['sculpture', 'doll']
box_1 = ['charger', 'toaster', 'wig', 'shirt', 'elephant']
box_2 = ['frame', 'sock', 'octopus', 'clock', 'fork']
box_3 = ['microwave', 'seaweed', 'puzzle', 'storm', 'apple']
box_4 = ['umbrella', 'rain', 'gloves', 'game']
box_5 = []
box_6 = ['beach', 'crown', 'dog', 'leaf', 'wallet']
box_7 = ['usb', 'dice', 'ocean', 'chair', 'razor']
box_8 = ['dolphin', 'soap', 'perfume', 'bear', 'starfish']
box_9 = ['coral', 'harmonica', 'mask', 'pillow', 'whistle']
box_10 = ['microscope', 'note', 'towel']

box_2.append('tree')
box_3.remove('puzzle')
box_3.remove('apple')
box_3.append('car')
box_3.append('doll')
box_1.remove('toaster')
box_1.remove('wig')
box_6.append('toaster')
box_6.remove('crown')
box_6.remove('toaster')
box_3.remove('microwave')
box_10.remove('note')
box_3.append('note')
box_7.extend(['flute', 'glasses'])
box_0.remove('doll')
box_0.append('ship')
box_3.remove('seaweed')
box_3.append('bear')
box_3.append('pot')
box_9.remove('whistle')
box_9.remove('mask')
box_1.append('whistle')
box_1.append('mask')
box_8.remove('starfish')
box_8.remove('perfume')
box_8.remove('dolphin')
box_8.append('usb')
box_2.remove('car')
box_4.remove('game')
box_4.remove('rain')
box_4.remove('umbrella')
box_4.append('phone')
box_4.append('tree')
box_9.remove('coral')
box_9.remove('pillow')
box_9.remove('harmonica')
box_9.append('clock')
box_9.append('battery')
box_9.append('branch')

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