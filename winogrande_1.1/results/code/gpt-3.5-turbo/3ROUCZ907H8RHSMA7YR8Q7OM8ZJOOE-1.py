def why_get_newspaper():
    reasons = {
        'newspaper': 'look_forward_to',
        'comics': 'only_reason'
    }

    for item, reason in reasons.items():
        if reason == 'only_reason':
            return item

print(why_get_newspaper())  # This should print 'comics'