box_0 = ['keyboard', 'car']
box_1 = []
box_2 = ['thunder']
box_3 = []
box_4 = ['grinder', 'chair', 'island', 'leaf', 'blanket']

box_4.remove('grinder')
box_4.remove('island')
box_4.append('towel')
box_2, box_4 = box_4, box_2
box_0.remove('keyboard')
box_2.append('chair')
box_4.remove('thunder')
box_4.extend(['freezer', 'microwave', 'elephant', 'shelf'])
box_4.remove('microwave')
box_4.remove('freezer')
box_4.remove('elephant')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)