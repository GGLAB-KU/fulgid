box_0 = ['boat', 'doll', 'crown', 'zipper']
box_1 = ['lion', 'toothbrush', 'train']
box_2 = ['truck', 'seaweed', 'phone', 'motorcycle', 'magnet']
box_3 = ['whistle', 'brush', 'frame', 'makeup', 'paint']
box_4 = ['perfume', 'flower']
box_5 = ['blender']
box_6 = ['button']
box_7 = ['fish', 'bell', 'rain', 'car']
box_8 = ['battery', 'tie', 'branch', 'bicycle']
box_9 = ['rocket', 'speaker']
box_10 = ['ship', 'lightning', 'piano', 'cat', 'bus']
box_11 = ['tiger']
box_12 = ['keyboard', 'shampoo']

box_7.remove('bell')
box_7.remove('rain')
box_8.append('bell')
box_8.append('rain')

box_2.append('coat')
box_2.append('bear')

box_7.remove('fish')
box_6.append('fish')

box_9.remove('rocket')
box_9.remove('speaker')
box_9.append('scarf')
box_9.append('elephant')

box_9.remove('elephant')
box_9.remove('scarf')
box_11.append('elephant')
box_11.append('scarf')

box_2.remove('coat')
box_2.remove('magnet')
box_2.remove('phone')
box_6.append('magnet')
box_6.append('phone')
box_6.append('coat')

box_0.remove('doll')
box_0.remove('boat')
box_0.remove('zipper')
box_11.append('doll')
box_11.append('boat')
box_11.append('zipper')

box_2.clear()

box_7.append('glove')
box_7.append('ring')
box_7.append('pants')

box_8.remove('bell')

box_1.remove('lion')
box_7.remove('pants')
box_1.append('pants')
box_7.append('lion')

box_7.remove('lion')
box_8.remove('rain')
box_7.append('rain')
box_8.append('lion')

box_4.remove('flower')
box_4.remove('perfume')
box_8.append('flower')
box_8.append('perfume')

box_6.clear()

box_12.append('shoes')
box_12.append('cloud')
box_12.append('bag')

box_11.remove('doll')
box_11.remove('tiger')
box_11.remove('zipper')

box_1.remove('toothbrush')
box_1.remove('pants')
box_1.remove('train')
box_10.append('toothbrush')
box_10.append('pants')
box_10.append('train')

box_5.clear()

box_12.clear()

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