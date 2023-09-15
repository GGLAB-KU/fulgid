box = {
    0: ['cat', 'button', 'key'],
    1: [],
    2: ['shorts', 'rain', 'blanket'],
    3: ['coral', 'pot', 'note', 'plane'],
    4: ['sandals'],
    5: ['mirror', 'oven'],
    6: ['wallet', 'cow', 'fork', 'desert', 'glasses'],
    7: ['comb', 'usb', 'vase', 'watch', 'mountain'],
    8: ['jungle', 'island', 'charger', 'zipper', 'tie'],
    9: ['glove', 'octopus', 'wire'],
    10: ['freezer', 'swimsuit', 'fish'],
    11: ['jacket', 'storm', 'sculpture'],
    12: ['doll']
}

def print_box_contents():
    for i in range(13):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

print_box_contents()

box[5].append('flower')
box[5].append('polish')

box[0].remove('blanket')
box[0].remove('shorts')
box[0].remove('rain')

box[8].append('blanket')
box[8].append('shorts')
box[8].append('rain')

box[0].remove('cat')
box[0].remove('rain')
box[0].remove('button')

box[8].append('cat')
box[8].append('rain')
box[8].append('button')

box[12], box[5] = box[5], box[12]

box[10].remove('fish')
box[10].append('microwave')

box[6], box[7] = box[7], box[6]

box[5].remove('mirror')
box[5].remove('oven')
box[5].remove('doll')

box[9].append('mirror')
box[9].append('oven')
box[9].append('doll')

box[6], box[10] = box[10], box[6]

box[8].append('basket')
box[8].append('seaweed')

box[7], box[6] = box[6], box[7]

box[6].remove('desert')
box[6].remove('swimsuit')

box[9].append('wallet')

box[7].append('fork')

box[0].remove('blanket')
box[0].remove('shorts')

box[2].append('blanket')
box[2].append('shorts')

box[0].remove('key')

box[8].append('cat')

box[6], box[9] = box[9], box[6]

box[2].remove('blanket')

box[10].append('blanket')

box[7].remove('usb')
box[7].remove('comb')

box[7].append('rocket')
box[7].append('shirt')

print_box_contents()