box = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: []
}

box[0] = ['note']
box[1] = ['wig', 'planet', 'helmet']
box[2] = ['crown', 'brush', 'forest', 'needle']
box[3] = ['button', 'train', 'tape', 'basket']
box[4] = ['coin', 'lipstick', 'wire', 'bus', 'razor']
box[5] = ['toothbrush', 'plane']
box[6] = ['card', 'belt']
box[7] = ['motorcycle']
box[8] = ['drum']
box[9] = ['shoe', 'makeup', 'jungle']
box[10] = ['comet', 'camera', 'fish', 'star', 'harmonica']
box[11] = ['frame', 'table', 'perfume']
box[12] = ['skirt', 'doll', 'speaker', 'sculpture', 'dog']
box[13] = ['horse', 'microwave', 'comb']
box[14] = ['mirror', 'car', 'river']

box[13].extend(['brush', 'lock'])
box[7].extend(['pants', 'watch', 'pot'])
box[1].remove('wire')
box[1].remove('coin')
box[3].append('coin')
box[3].append('wire')
box[13].remove('comb')
box[3].append('comb')
box[6].remove('card')
box[6].remove('belt')
box[6].extend(['forest', 'magnet'])
box[4].extend(['wallet', 'razor', 'pan'])
box[4].remove('pan')
box[5].remove('plane')
box[4].append('plane')
box[14].remove('car')
box[6].remove('magnet')
box[6].remove('forest')
box[6].extend(['razor', 'usb'])
box[7].extend(['watch', 'pants'])
box[2].remove('brush')
box[10].remove('camera')
box[10].remove('star')
box[10].remove('harmonica')
box[6].extend(['table', 'frame', 'perfume'])
box[0].extend(['shoes'])
box[5].remove('toothbrush')
box[5].remove('pan')
box[6].remove('perfume')
box[6].append('crown')
box[14].remove('river')
box[7].extend(['river', 'mirror'])
box[13].remove('horse')
box[8].append('horse')
box[5].extend(['shoes', 'toy'])
box[2].remove('needle')
box[0].append('needle')
box[9].remove('jungle')
box[7].append('jungle')
box[1].remove('helmet')
box[1].remove('planet')
box[1].remove('wire')
box[2].extend(['helmet', 'planet', 'wire'])

for i in range(15):
    print(f"Box {i}: {box[i]}")