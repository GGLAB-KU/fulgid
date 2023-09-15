box_0 = ['telescope', 'car']
box_1 = ['polish', 'octopus', 'flute', 'book', 'river']
box_2 = ['drum', 'gloves', 'shorts', 'grass', 'battery', 'brush']
box_3 = ['car', 'starfish', 'coin', 'basket']
box_4 = []

box_4.append('towel')
box_2.extend(['shorts', 'grass', 'battery'])
box_1.extend(['book', 'river'])
box_0[0] = 'car'
box_2.extend(['book', 'flute'])
box_0.append('blender')
box_1.clear()
box_2[2] = 'brush'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)