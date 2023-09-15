box_0 = ['coral', 'console', 'headphone']
box_1 = ['cloud', 'submarine', 'rocket', 'lamp']
box_2 = []
box_3 = ['razor', 'motorcycle']
box_4 = ['plate', 'makeup', 'apple']
box_5 = ['shelf', 'vase', 'toothbrush', 'blanket', 'toy']
box_6 = []
box_7 = ['scissors', 'table']
box_8 = ['sock', 'whistle']
box_9 = ['frame', 'lipstick', 'violin', 'island', 'storm']
box_10 = ['wire', 'mask', 'umbrella', 'dress', 'shirt']

box_10.remove('shirt')
box_10.remove('wire')
box_10.extend(['crown', 'horn'])
box_0.remove('coral')
box_10.extend(['lamp', 'note', 'tape'])
box_7.remove('scissors')
box_7.append('lamp')
box_0.remove('headphone')
box_5.extend(['paint', 'grinder', 'battery'])
box_8.remove('whistle')
box_7.remove('table')
box_7.append('tiger')
box_7.append('microwave')
box_2.append('tiger')
box_0.extend(['coral', 'phone', 'earring'])
box_3.extend(['laptop', 'thread'])
box_1.remove('scissors')
box_1.remove('submarine')
box_4.remove('apple')
box_7.remove('microwave')
box_7.append('storm')
box_2.extend(['lightning', 'paint', 'cup'])
box_5.clear()
box_7.remove('storm')
box_3.append('motorcycle')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")