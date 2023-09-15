box_0 = ['necklace', 'magnet', 'cat']
box_1 = ['lamp']
box_2 = ['shark', 'ocean']
box_3 = ['piano', 'submarine']
box_4 = ['pen', 'pot']
box_5 = ['telescope', 'bear', 'scarf', 'comb', 'planet']
box_6 = ['speaker', 'razor', 'toaster', 'hat']

box_4 = []

box_4.append(box_6.pop(box_6.index('hat')))
box_4.append(box_6.pop(box_6.index('speaker')))

box_6.extend(['octopus', 'dog', 'horse'])

box_6[box_6.index('razor')], box_0[box_0.index('magnet')] = box_0[box_0.index('magnet')], box_6[box_6.index('razor')]

box_6.append('shoes')

box_6[box_6.index('octopus')] = 'coat'
box_6[box_6.index('dog')] = 'boot'

box_4.remove('hat')
box_4.remove('speaker')

box_2.extend([box_5.pop(box_5.index('scarf')), box_5.pop(box_5.index('planet'))])

box_5[box_5.index('comb')] = 'dress'
box_5[box_5.index('telescope')] = 'coral'
box_5[box_5.index('bear')] = 'bicycle'

box_1.remove('lamp')

box_5[box_5.index('dress')], box_2[box_2.index('planet')] = box_2[box_2.index('planet')], box_5[box_5.index('dress')]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)