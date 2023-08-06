def what_resonates_with_decorations():
    furniture = {
        'table': 'not as much',
        'couch': 'more'
    }

    for item, preference in furniture.items():
        if preference == 'more':
            return item

print(what_resonates_with_decorations())  # This should print 'couch'