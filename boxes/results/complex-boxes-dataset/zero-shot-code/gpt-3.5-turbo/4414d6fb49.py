box_0 = ['razor', 'mixer', 'necklace']
box_1 = ['bus', 'fork', 'wallet']
box_2 = ['gloves', 'mask', 'wig', 'pen', 'swimsuit']
box_3 = ['grass', 'pants']
box_4 = ['storm', 'ship', 'truck', 'plane']
box_5 = []
box_6 = ['mirror', 'dress', 'thread', 'dolphin']
box_7 = ['speaker', 'pan', 'ocean', 'coral', 'guitar']
box_8 = ['leaf', 'lamp']
box_9 = ['violin', 'shelf', 'rain', 'thunder']
box_10 = ['book', 'makeup', 'earring', 'console']
box_11 = []
box_12 = ['hat', 'boat', 'motorcycle']
box_13 = ['rock', 'horse']

box_0.remove('mixer')
box_0.remove('necklace')
box_0.remove('razor')

box_12.remove('boat')
box_12.remove('hat')

box_0.extend(['shelf', 'necklace', 'coral'])

horse_index = box_13.index('horse')
motorcycle_index = box_12.index('motorcycle')
box_12[motorcycle_index], box_13[horse_index] = box_13[horse_index], box_12[motorcycle_index]

ship_index = box_4.index('ship')
box_4[ship_index] = 'toaster'

box_13.remove('rock')

box_13.extend(['shelf', 'rain'])

box_10.remove('book')

motorcycle_index = box_12.index('motorcycle')
box_12[motorcycle_index] = 'freezer'

box_2.remove('wig')
box_2.remove('mask')
box_2.remove('pen')

box_0.remove('coral')
box_0.remove('shelf')
box_0.extend(['horn', 'boat'])

box_0.remove('necklace')
box_0.remove('boat')
box_0.remove('horn')

pants_index = box_3.index('pants')
guitar_index = box_7.index('guitar')
box_3[pants_index], box_7[guitar_index] = box_7[guitar_index], box_3[pants_index]

violin_index = box_9.index('violin')
thunder_index = box_9.index('thunder')
box_9[violin_index], box_9[thunder_index] = 'blender', 'glasses'

dress_index = box_6.index('dress')
box_6[dress_index] = 'wire'

box_10.extend(['jungle', 'bear', 'river'])

storm_index = box_4.index('storm')
plane_index = box_4.index('plane')
box_3.extend([box_4[storm_index], box_4[plane_index]])
box_4.remove('storm')
box_4.remove('toaster')
box_4.remove('plane')

lamp_index = box_8.index('lamp')
truck_index = box_4.index('truck')
box_8[lamp_index], box_4[truck_index] = box_4[truck_index], box_8[lamp_index]

ocean_index = box_7.index('ocean')
speaker_index = box_7.index('speaker')
box_9.extend([box_7[ocean_index], box_7[speaker_index]])
box_7.remove('ocean')
box_7.remove('speaker')

lamp_index = box_8.index('lamp')
box_8[lamp_index] = 'speaker'

box_2.remove('swimsuit')
box_2.remove('gloves')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)
print("Box 13:", box_13)