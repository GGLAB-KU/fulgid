box_0 = []
box_1 = ['bracelet', 'lion']
box_2 = []
box_3 = ['needle', 'frame']
box_4 = ['mixer', 'perfume', 'makeup', 'boat']
box_5 = []
box_6 = ['thread']
box_7 = ['microscope', 'jacket', 'bird']
box_8 = ['spoon', 'clock', 'shark', 'scissors', 'umbrella']
box_9 = ['lamp', 'sculpture', 'wallet', 'flute']
box_10 = ['wire', 'toothpaste', 'wig', 'elephant']
box_11 = ['coat', 'comet', 'shirt']
box_12 = ['rock', 'forest', 'phone', 'soap', 'watch']

box_12.remove('rock')
box_12.remove('forest')
box_12.remove('phone')
box_12.append('rock')
box_12.append('forest')
box_12.append('watch')

box_10.remove('wire')
box_10.remove('toothpaste')
box_10.remove('wig')
box_10.append('elephant')
box_10.append('wig')
box_10.append('toothpaste')

box_7.remove('microscope')
box_7.remove('jacket')
box_7.remove('bird')
box_7.append('bird')
box_7.append('microscope')

box_3.remove('needle')
box_3.remove('frame')
box_3.append('zipper')
box_3.append('piano')

box_5.remove('zipper')
box_5.remove('piano')
box_5.append('train')

box_1.remove('bracelet')
box_1.remove('lion')

box_12.remove('lion')
box_12.remove('bracelet')
box_12.append('lion')
box_12.append('bracelet')

box_10.remove('elephant')
box_10.remove('wig')
box_10.remove('toothpaste')
box_10.append('elephant')
box_10.append('wig')
box_10.append('toothpaste')

box_7.remove('bird')
box_7.remove('microscope')
box_7.remove('jacket')
box_7.append('piano')
box_7.append('bird')

box_1.remove('lion')
box_1.remove('bracelet')

box_12.remove('rock')
box_12.remove('forest')
box_12.remove('watch')
box_12.append('rock')
box_12.append('forest')
box_12.append('watch')

box_1 = []
box_4 = ['mixer', 'perfume', 'makeup', 'boat', 'butterfly', 'tie']

box_12.remove('rock')
box_12.remove('forest')
box_12.remove('watch')
box_12.append('rock')
box_12.append('forest')
box_12.append('watch')

box_7.remove('rock')
box_7.remove('sculpture')
box_7.remove('phone')
box_7.append('rock')
box_7.append('sculpture')
box_7.append('phone')

box_3.remove('zipper')
box_3.remove('leaf')

box_10.remove('rocket')
box_10.remove('watch')
box_10.append('rocket')
box_10.append('watch')

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