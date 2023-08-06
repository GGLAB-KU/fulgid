def what_did_the_boys_enjoy():
    activities = {
        'cornhole': 'game',
        'dinner': 'meal'
    }

    for activity, type in activities.items():
        if type == 'game':
            return activity

print(what_did_the_boys_enjoy())  # This should print 'cornhole'