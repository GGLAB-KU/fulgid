box0 = ['swimsuit', 'shoes', 'scarf', 'ring']
box1 = ['earring']
box2 = ['fork', 'grinder', 'note', 'speaker']
box3 = ['meteor', 'umbrella']
box4 = ['sun', 'pen', 'ocean', 'bell']
box5 = ['harmonica']

box5 = []

box4.remove('ocean')
box3.append('ocean')
box3.remove('meteor')
box4.append('meteor')

box5.extend(['chair', 'car'])
box5.remove('chair')
box1.append('chair')

box2.remove('fork')
box2.append('magnet')

box4.remove('meteor')
box4.remove('bell')
box4.remove('sun')
box3.extend(['meteor', 'bell', 'sun'])

box0.remove('shoes')
box0.remove('swimsuit')
box0.remove('scarf')
box0.extend(['game', 'spoon', 'shampoo'])

box2.remove('speaker')
box2.remove('magnet')
box2.remove('note')
box1.extend(['speaker', 'magnet', 'note'])

box4.remove('pen')
box4.append('truck')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)