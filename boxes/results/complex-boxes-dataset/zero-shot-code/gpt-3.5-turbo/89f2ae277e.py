box_0 = ['mirror', 'rock', 'microscope']
box_1 = ['note', 'comet', 'thread', 'truck', 'coin']
box_2 = []
box_3 = ['skirt', 'ring', 'vase', 'pen']
box_4 = ['forest', 'game', 'lion', 'table']
box_5 = ['towel', 'rain', 'flower', 'snow']
box_6 = ['coat', 'bell', 'island', 'mixer']
box_7 = ['makeup', 'phone', 'harmonica', 'motorcycle', 'tiger']

box_3.remove('vase')
box_3.extend(['butterfly', 'plane', 'speaker'])
box_5[1:4] = ['controller', 'ship', 'scarf']
box_1[0:2] = ['wire', 'river']
box_4[3] = 'freezer'
box_1.remove('thread')
box_3.append('thread')
box_4, box_7 = box_7, box_4
box_1[2] = 'island'
box_6[2] = 'wire'
box_3.remove('butterfly')
box_3.remove('thread')
box_3.remove('speaker')
box_6.extend(['swimsuit', 'mountain', 'island'])
box_0.append('truck')
box_6.remove('swimsuit')
box_6.remove('mountain')
box_6.remove('wire')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")