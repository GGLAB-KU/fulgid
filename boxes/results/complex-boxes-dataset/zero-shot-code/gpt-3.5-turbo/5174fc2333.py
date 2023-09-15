box0 = []
box1 = []
box2 = ['camera', 'butterfly', 'helmet', 'bag']
box3 = []
box4 = ['sandals', 'seaweed']

print("Initial state:")
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)

box1.append('mountain')
box4.extend(['bag', 'laptop'])
box2.remove('camera')
box2.remove('helmet')
box2.remove('bag')
box4.remove('bag')
box4.remove('laptop')
box1.append('scissors')
box2.remove('mountain')
box4.remove('butterfly')
box4.remove('mountain')

print("\nFinal state:")
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)