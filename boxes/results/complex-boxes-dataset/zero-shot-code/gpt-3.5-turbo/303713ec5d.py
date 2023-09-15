box_0 = ['lightning', 'crown', 'tape', 'shorts', 'horse']
box_1 = ['shoes', 'whistle', 'scarf', 'basket', 'shirt']
box_2 = []
box_3 = ['dolphin', 'moon', 'bowl', 'perfume']
box_4 = ['leaf']
box_5 = ['wire', 'jungle', 'cow', 'magnet', 'toy']
box_6 = ['brush', 'coat', 'forest', 'paint', 'vase']
box_7 = ['microscope', 'guitar', 'branch', 'necklace', 'motorcycle']
box_8 = ['puzzle']
box_9 = ['usb', 'dog', 'lamp', 'dice']
box_10 = ['keyboard']
box_11 = []
box_12 = ['coin', 'lion']
box_13 = []
box_14 = ['scissors', 'makeup']

box_12 = ['frame', 'soap']
box_1.append('needle')
box_7.remove('necklace')
box_3.remove('bowl')
box_11.extend(['frame', 'soap'])
box_11.remove('frame')
box_11.remove('necklace')
box_5[2] = 'mixer'
box_0[0], box_7[2] = box_7[2], box_0[0]
box_3.remove('leaf')
box_10.extend(['leaf', 'perfume', 'dolphin'])
box_0.append('blanket')
box_7[0], box_7[4], box_7[2] = box_5[2], box_1[0], box_0[1]
box_3[1], box_6[3] = box_6[3], box_3[1]
box_9.extend(['note', 'clock', 'horse'])
box_9.extend(['bear', 'branch', 'thread'])
box_1[0], box_0[2] = box_0[2], box_1[0]
box_5.extend(['lion', 'train', 'island'])
box_3.append('scissors')
box_8.extend(['magnet', 'jungle', 'toy'])
box_7.extend(['mirror', 'lamp', 'table'])
box_11.extend(['car', 'branch', 'island'])
box_0[1], box_7[2], box_0[3] = box_7[2], box_6[4], box_0[3]

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")