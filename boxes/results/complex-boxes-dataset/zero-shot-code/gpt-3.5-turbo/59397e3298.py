box = {
    0: [],
    1: ['lion'],
    2: [],
    3: ['pen', 'keyboard', 'coat'],
    4: [],
    5: ['watch', 'battery', 'spoon'],
    6: ['sock', 'coin', 'grass', 'table'],
    7: ['console', 'laptop', 'thread'],
    8: [],
    9: ['tie'],
    10: [],
    11: [],
    12: ['lock', 'ship', 'candle']
}

print("Initial State:")
for i in range(13):
    print(f"Box {i}: {box[i]}")

box[2].append(box[9].pop(0))
box[11].extend(['candle', 'jungle'])
box[6] = ['doll', 'ring']
box[12] = []
box[12].extend(['mask', 'candle'])
box[5].remove('spoon')
box[5].remove('battery')
box[5].remove('watch')
box[12].remove('candle')
box[6] = ['perfume', 'jungle']
box[1].remove('lion')
box[3].append(box[12].pop(0))
box[3] = []
box[11] = ['train']
box[1].extend(['table', 'perfume', 'ring'])
box[9].append('dice')
box[11], box[7] = box[7], box[11]
box[4].extend(['key', 'helmet', 'candle'])
box[2].append(box[4].pop(0))
box[8].append(box[4].pop(0))
box[10].extend(['table', 'ring', 'perfume'])
box[7].append(box[11].pop(0))

print("\nFinal State:")
for i in range(13):
    print(f"Box {i}: {box[i]}")