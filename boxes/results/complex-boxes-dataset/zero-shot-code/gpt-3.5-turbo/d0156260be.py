box_0 = ['doll', 'shark', 'wig', 'whistle', 'drum']
box_1 = ['cat', 'plate', 'wire', 'controller', 'shampoo']
box_2 = ['clock', 'cow', 'thunder', 'laptop', 'guitar']
box_3 = []
box_4 = ['vase', 'earring', 'apple', 'shorts', 'swimsuit']
box_5 = []
box_6 = ['piano', 'pants', 'planet']
box_7 = ['polish', 'pillow']
box_8 = []
box_9 = []
box_10 = ['lightning', 'helmet', 'grass', 'bicycle', 'pan']
box_11 = ['bracelet', 'truck', 'towel', 'magnet', 'mask']

box_11.append('seaweed')
box_7.remove('pillow')
box_7.remove('polish')
box_2.append('pillow')
box_2.append('polish')
box_6.remove('piano')
box_6.append('star')
box_8.extend(['needle', 'blanket', 'shelf'])
box_8.remove('blanket')
box_8.remove('needle')
box_8.remove('shelf')
box_8.extend(['apple', 'leaf', 'bicycle'])
box_2.remove('laptop')
box_2.remove('polish')
box_6.remove('star')
box_6.append('bicycle')
box_6.remove('bicycle')
box_10.extend(['seaweed', 'harmonica'])
box_2.remove('thunder')
box_2.remove('pillow')
box_2.extend(['apple', 'violin'])
box_9.extend(['octopus', 'rocket', 'doll'])
box_9.remove('octopus')
box_9.remove('doll')
box_3.extend(['octopus', 'doll'])
box_8.remove('apple')
box_8.remove('star')
box_8.remove('leaf')
box_4.remove('apple')
box_4.remove('swimsuit')
box_4.remove('shorts')
box_4.extend(['charger', 'note'])
box_10.remove('pan')
box_0.append('pan')
box_0.remove('pan')
box_0.append('leaf')
box_4.remove('note')
box_4.append('scarf')

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