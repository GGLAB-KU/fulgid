box_0 = ['telescope']
box_1 = ['comb', 'starfish']
box_2 = ['earring', 'bear', 'shoes']
box_3 = ['pen']
box_4 = ['shirt', 'candle', 'glasses', 'brush']
box_5 = ['submarine', 'clock', 'drum']
box_6 = ['cat', 'bus', 'mixer', 'shoes', 'comet']
box_7 = ['spoon']
box_8 = ['table']
box_9 = ['game', 'boot', 'lipstick']
box_10 = ['scissors', 'jacket', 'blender', 'card', 'harmonica']
box_11 = []
box_12 = ['grinder', 'lion', 'flute', 'seaweed', 'soap']

box_8 = ['keyboard']
box_4 = ['grass']
box_5.append('crown')
box_7.append('cat')
box_8.extend(['cloud', 'chair'])
box_4.extend(['glasses', 'brush'])
box_2.extend(['pen', 'dice', 'starfish'])
box_5.remove('crown')
box_11.append('earring')
box_5[box_5.index('clock')] = 'seaweed'
box_1.extend(['shorts', 'basket'])
box_3 = ['seaweed']
box_5 = ['violin', 'button']
box_4.append('seaweed')
box_5.remove('violin')
box_5.remove('drum')
box_5.remove('submarine')
box_4[box_4.index('candle')] = 'lipstick'
box_9[box_9.index('lipstick')] = 'candle'
box_0[box_0.index('telescope')] = 'candle'
box_6.append('seaweed')
box_11 = []
box_6.extend(['mixer', 'shoes', 'comet'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")