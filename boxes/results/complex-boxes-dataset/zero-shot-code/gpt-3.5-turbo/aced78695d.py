box_0 = ['card']
box_1 = ['note', 'chair', 'sock']
box_2 = ['truck', 'ring', 'dog', 'thread', 'horse']
box_3 = ['starfish', 'polish']
box_4 = ['perfume', 'keyboard', 'shampoo']

box_3.remove('polish')
box_3.append('bowl')
box_3.append('blender')
box_3.extend(['brush', 'dolphin', 'bell'])
box_4.remove('shampoo')
box_4.remove('keyboard')
box_4.remove('perfume')
box_4.extend(['dog', 'truck'])
box_1.remove('sock')
box_1.remove('chair')
box_1.remove('note')
box_1.extend(['rock', 'branch', 'dice'])
box_2.remove('thread')
box_2.remove('horse')
box_2.remove('ring')
box_2.extend(['oven', 'card'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)