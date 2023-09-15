box = {
    0: ['earring', 'puzzle', 'bowl'],
    1: ['charger', 'card', 'towel', 'blender'],
    2: ['wallet', 'elephant', 'comet'],
    3: ['violin'],
    4: ['rocket', 'note', 'toothbrush'],
    5: ['cloud'],
    6: [],
    7: [],
    8: ['shirt', 'cat', 'cow'],
    9: ['sandals'],
    10: ['island', 'branch', 'flute', 'piano'],
    11: [],
    12: ['dog']
}

def print_box_contents():
    for i in range(13):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

def move_items():
    box[0].extend(['lamp', 'spoon'])
    box[5] = []
    box[1] = ['train', 'drum']
    box[9] = ['microwave', 'bicycle']
    box[3].extend(box[2])
    box[2] = []
    box[0].extend(['brush', 'cat'])
    box[6] = []
    box[6].append(box[1].pop(1))
    box[8][0], box[2][0] = box[2][0], box[8][0]
    box[3] = ['motorcycle', 'controller']
    box[8] = ['wig', 'lipstick', 'jungle']
    box[4].append('grinder')
    box[2][0], box[12][0] = box[12][0], box[2][0]
    box[10].remove('branch')
    box[7].extend([box[4].pop(1), box[4].pop(1), box[4].pop(0)])
    box[5].append('scissors')
    box[4][0] = 'tie'
    box[2] = []
    box[3], box[5] = box[5], box[3]
    box[10] = []

print_box_contents()
move_items()
print_box_contents()