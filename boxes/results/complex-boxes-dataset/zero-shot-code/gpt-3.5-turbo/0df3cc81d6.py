box_0 = ['card', 'horse', 'brush', 'leaf', 'seaweed']
box_1 = ['comb', 'train', 'perfume', 'mountain', 'apple']
box_2 = ['toaster', 'gloves', 'shoe', 'pants', 'controller']
box_3 = ['cat', 'branch', 'boot']
box_4 = ['lamp', 'plane']
box_5 = ['watch', 'bag', 'hat', 'dice', 'speaker']
box_6 = ['frame', 'dog', 'grinder', 'tie', 'doll']
box_7 = []
box_8 = ['book', 'oven']

box_6.append('motorcycle')
box_8[box_8.index('book')] = 'lamp'
box_2.extend([box_4.pop(box_4.index('plane')), box_8.pop(box_8.index('lamp'))])
box_3.remove('boot')
box_3.remove('branch')
box_3.remove('cat')
box_1[box_1.index('apple')] = 'blanket'
box_1[box_1.index('perfume')] = 'zipper'
box_8.clear()
box_2[box_2.index('gloves')] = 'dice'
box_2[box_2.index('shoe')] = 'sun'
box_6[box_6.index('tie')] = 'sun'
box_6.remove('frame')
box_2.extend(['mountain', 'coral', 'thunder'])
box_5.remove('speaker')
box_5.remove('hat')
box_0[box_0.index('card')] = 'soap'
box_0[box_0.index('seaweed')] = 'rain'
box_1.extend(['lion', 'towel'])
box_1[box_1.index('train')] = 'leaf'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)