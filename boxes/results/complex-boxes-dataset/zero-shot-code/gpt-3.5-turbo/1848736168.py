box = {
    0: ['dice', 'shorts', 'car'],
    1: ['card', 'towel'],
    2: ['lightning'],
    3: ['umbrella', 'headphone'],
    4: ['telescope', 'soap', 'sandals', 'wallet'],
    5: [],
    6: [],
    7: ['river', 'doll', 'lion', 'razor', 'tie'],
    8: ['mask'],
    9: ['shelf', 'flower', 'controller', 'train', 'motorcycle'],
    10: ['thread'],
    11: ['lipstick', 'cow', 'fridge', 'puzzle', 'book'],
    12: ['truck', 'clock']
}

def move_items():
    box[2].extend([box[11].pop(box[11].index('cow')), box[11].pop(box[11].index('book'))])
    box[10].remove('thread')
    box[1][box[1].index('card')], box[12][box[12].index('truck')] = box[12][box[12].index('truck')], box[1][box[1].index('card')]
    box[8].append('bell')
    box[1].append('pan')
    box[1].append(box[11].pop(box[11].index('lipstick')))
    box[11] = []
    box[2].extend([box[9].pop(box[9].index('controller')), box[9].pop(box[9].index('train')), box[9].pop(box[9].index('shelf'))])
    box[9].extend([box[0].pop(box[0].index('shorts')), box[0].pop(box[0].index('car'))])
    box[8][box[8].index('mask')], box[9][box[9].index('motorcycle')] = box[9][box[9].index('motorcycle')], box[8][box[8].index('mask')]
    box[7].append(box[9].pop(box[9].index('flower')))
    box[10].append('thread')
    box[7].remove('tie')
    box[9].remove('shorts')
    box[9].remove('car')
    box[9].extend([box[8].pop(box[8].index('bell')), box[9].pop(box[9].index('motorcycle'))])
    box[1].remove('lipstick')
    box[1][box[1].index('towel')], box[12][box[12].index('clock')] = box[12][box[12].index('clock')], box[1][box[1].index('towel')]
    box[3] = ['shelf', 'tree']
    box[6].extend([box[2].pop(box[2].index('book')), box[2].pop(box[2].index('train')), box[2].pop(box[2].index('controller'))])
    box[10].append('dice')

def print_boxes():
    for i in range(13):
        print(f"Box {i}: {box[i]}")

move_items()
print_boxes()