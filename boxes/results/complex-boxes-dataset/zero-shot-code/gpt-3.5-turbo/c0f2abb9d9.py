box = {
    0: ['pan'],
    1: ['umbrella', 'flute', 'watch'],
    2: ['bowl', 'paint'],
    3: ['speaker'],
    4: ['microscope', 'headphone', 'seaweed', 'coin'],
    5: ['fish', 'blanket', 'motorcycle', 'helmet', 'horn'],
    6: [],
    7: ['snow', 'fridge', 'battery', 'keyboard'],
    8: [],
    9: [],
    10: ['guitar', 'leaf', 'branch', 'polish', 'desert'],
    11: ['perfume', 'coat', 'cat'],
    12: ['ship', 'sock', 'belt', 'mixer', 'ocean']
}

box[11].append('crown')
box[0].remove('pan')
box[0].append('boot')
box[2].remove('paint')
box[9].append('sock')
box[4] = ['moon', 'freezer', 'truck']
box[4].remove('microscope')
box[12].remove('mixer')
box[11].append('thunder')
box[0].remove('sock')
box[0] = ['moon', 'ship', 'tape']
box[10].remove('branch')
box[6] = ['leaf', 'guitar', 'polish']
box[4].remove('freezer')
box[7].append('ocean')
box[1], box[12] = box[12], box[1]
box[12].append('desert')
box[12].extend(['crown', 'coat', 'perfume'])
box[4].remove('truck')
box[4].remove('moon')

for i in range(13):
    print(f"Box {i}: {box[i]}")