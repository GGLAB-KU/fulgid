box_0 = ['dolphin', 'ring', 'fridge']
box_1 = ['lightning', 'magnet', 'earring', 'beach', 'island']
box_2 = ['jungle', 'shelf']
box_3 = ['swimsuit', 'doll', 'blanket']

box_3.extend(['lipstick', 'train'])
box_2[0] = 'bell'
box_1.extend(['microscope', 'usb'])
box_3.remove('lipstick')
box_3.remove('swimsuit')
box_2[0] = 'horn'
box_1[3] = 'dress'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)