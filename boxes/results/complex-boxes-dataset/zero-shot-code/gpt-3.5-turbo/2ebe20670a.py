box_0 = ['bracelet', 'dog', 'telescope', 'shampoo']
box_1 = ['blender', 'necklace']
box_2 = ['lipstick', 'polish', 'thread', 'swimsuit']
box_3 = ['fish']
box_4 = ['snow', 'bicycle']
box_5 = ['bell', 'elephant']

box_0 = []
box_1.remove('necklace')
box_2.extend(['necklace', 'blender'])
box_4.remove('snow')
box_4.append('tree')
box_0.extend(['phone', 'mask'])
box_3.remove('fish')
box_5.remove('elephant')
box_3.append('elephant')
box_2.extend(['bell', 'fish'])
box_4.append('rock')
box_2.remove('blender')
box_2.remove('bell')
box_2.remove('lipstick')
box_2.extend(['sculpture', 'glove', 'mirror'])
box_0.remove('mask')
box_5.append('mask')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)