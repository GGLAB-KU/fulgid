def who_gets_easier_cases():
    surgeons = {
        'Sarah': 'better',
        'Maria': 'not as good'
    }

    for surgeon, skill in surgeons.items():
        if skill == 'not as good':
            return surgeon

print(who_gets_easier_cases())  # This should print 'Maria'
