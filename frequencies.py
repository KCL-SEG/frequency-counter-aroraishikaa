def frequencies(items):
    frequencies = {}
    for item in items:
        # Convert item to string
        item_str = str(item)
        # Count the occurrences
        if item_str in frequencies:
            frequencies[item_str] += 1
        else:
            frequencies[item_str] = 1
    return frequencies
