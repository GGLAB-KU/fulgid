box_0 = ['shelf']
box_1 = ['speaker', 'belt', 'book']
box_2 = ['horn', 'lion', 'earring']
box_3 = ['bus', 'mixer', 'polish', 'glove']
box_4 = []
box_5 = ['paint', 'seaweed', 'charger', 'puzzle', 'fork']
box_6 = []
box_7 = ['vase', 'camera', 'lipstick']
box_8 = ['usb', 'harmonica', 'lock']
box_9 = ['shark']
box_10 = []
box_11 = ['lamp', 'console', 'sandals']
box_12 = ['battery']
box_13 = ['fridge', 'needle']
box_14 = ['submarine', 'scarf', 'tree', 'thunder']

box_11 = ['elephant', 'island', 'jacket']
box_14 = ['mirror', 'dolphin', 'mask']
box_3.append('ring')
box_3.extend(box_13)
box_7.extend(box_14)
box_8.extend(['cloud', 'towel', 'dog'])
box_2 = ['helmet', 'mask']
box_0, box_7 = box_7, box_0
box_9 = ['mixer']
box_1 = []
box_0, box_14 = box_14, box_0
box_8 = []
box_2 = ['fridge', 'bell', 'grinder']
box_3 = []
box_0 = ['towel']
box_11 = []
box_10 = ['forest', 'umbrella']
box_2.append('sandals')
box_7.remove('tree')
box_7.remove('dolphin')
box_7.remove('lipstick')
box_1.extend(['vase', 'mask'])
box_0.remove('towel')
box_0.append('lipstick')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")