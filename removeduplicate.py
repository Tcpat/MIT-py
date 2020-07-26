def remove_duplicate_ids(obj):
    order_keys = []
    for i in obj:
        order_keys.append(int(i))
    for i in range(len(order_keys)):
        order_keys[i] = int(order_keys[i])
    keys_sorted = sorted(order_keys)
    values_ordered = []
    for i in keys_sorted:
        values_ordered.append(obj[str(i)])
    new_dict = {}
    all_values = []
    new_values = []
    for i in range(len(values_ordered)):
        new_values.append([])
    for i in range(-1, -len(values_ordered)-1, -1):
        for j in range(len(values_ordered[i])):
            if values_ordered[i][j] not in all_values:
                all_values.append(values_ordered[i][j])
                new_values[i].append(values_ordered[i][j])
    for i in range(len(keys_sorted)):
        new_dict[str(keys_sorted[i])] = new_values[i]
    return new_dict
