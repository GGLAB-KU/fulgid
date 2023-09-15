box_0 = ['star', 'mirror', 'bell', 'branch', 'microwave']
box_1 = ['wire', 'comb', 'train']
box_2 = ['bracelet', 'oven', 'beach', 'forest', 'motorcycle']
box_3 = []
box_4 = ['game', 'elephant', 'battery', 'dress']
box_5 = []
box_6 = ['rock', 'key', 'starfish', 'cow', 'pen']
box_7 = ['river', 'guitar', 'mask', 'coin']
box_8 = ['glasses', 'phone']
box_9 = ['sandals', 'card', 'keyboard', 'truck']
box_10 = ['headphone', 'brush', 'console']

box_2 = []
box_7.remove('mask')
box_7.remove('coin')
box_8.append('grinder')
box_7, box_6 = box_6, box_7
box_9.append('boot')
box_7 = []
box_3.extend([box_9.pop(box_9.index('card')), box_9.pop(box_9.index('truck')), box_9.pop(box_9.index('sandals'))])
box_8.remove('glasses')
box_9.remove('keyboard')
box_6, box_0 = box_0, box_6
box_9.append('coin')
box_10 = ['usb', 'pan', 'dolphin']
box_1.extend(['blender', 'speaker', 'horse'])
box_9 = ['star', 'game']
box_2.extend([box_4.pop(box_4.index('game')), box_4.pop(box_4.index('elephant')), box_4.pop(box_4.index('battery'))])
box_4, box_3 = box_3, box_4

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")