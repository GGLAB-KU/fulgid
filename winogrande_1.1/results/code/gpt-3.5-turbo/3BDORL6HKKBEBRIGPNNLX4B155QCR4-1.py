def what_would_be_more_noticeable():
    items = {
        'dress': 'new_item',
        'hat': 'old_item'
    }

    for item, description in items.items():
        if description == 'new_item':
            return item

print(what_would_be_more_noticeable())  # This should print 'dress'