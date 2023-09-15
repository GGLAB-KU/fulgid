box0 = ['plate']
box1 = ['bus', 'game', 'charger', 'submarine', 'hat']
box2 = ['river', 'horn', 'pillow']
box3 = ['mixer']
box4 = ['boat']

box4.remove('boat')
box1.extend(['lightning', 'controller'])
box3.extend(['fish', 'thunder'])
box1.extend(box2)
box2.clear()
box1.extend(['chair', 'starfish', 'fork'])
box3[0] = 'doll'
box3[1] = 'glasses'
box3.append('keyboard')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)