def what_was_stuffy_and_old_fashioned():
    clothing = {
        'shirt': 'old_fashioned',
        't-shirt': 'not_old_fashioned'
    }

    for item, fashion in clothing.items():
        if fashion == 'old_fashioned':
            return item

print(what_was_stuffy_and_old_fashioned())  # This should print 'shirt'