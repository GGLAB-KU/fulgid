box_0 = ['planet', 'guitar', 'tie']
box_1 = ['harmonica', 'charger', 'whistle']
box_2 = ['shampoo']
box_3 = ['toaster', 'wig']
box_4 = ['polish']

box_4 = []

box_2.remove('shampoo')
box_2.append('boot')

box_0.extend(['dolphin', 'usb'])
box_1.append('whistle')

box_1.append(box_2.pop())

box_0[0], box_1[0] = box_1[0], box_0[0]

box_0[0] = 'spoon'

box_4.extend([box_0.pop(1), box_0.pop(1)])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)