box_0 = []
box_1 = ['dog']
box_2 = ['thunder', 'shelf', 'horn', 'starfish']
box_3 = ['bird', 'charger', 'pants', 'camera', 'chair']
box_4 = ['telescope']
box_5 = ['grinder', 'mask', 'toothpaste', 'lion', 'bowl']

box_0.append('zipper')
box_5.remove('bowl')
box_1.append('bowl')
box_0.remove('zipper')
box_1.extend(['dog', 'lion', 'grinder'])
box_2.remove('shelf')
box_4.append('shelf')
box_4.remove('telescope')
box_3.append('drum')
box_3.remove('bird')
box_3.remove('drum')
box_3.extend(['blender', 'cow'])
box_5.remove('mask')
box_5.remove('toothpaste')
box_5.extend(['zipper', 'paint'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)