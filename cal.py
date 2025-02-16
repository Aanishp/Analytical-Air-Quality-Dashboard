def get_data(data, key):
    lst = []
    for d in data[key]:
            lst.append(d['value'])

    return lst