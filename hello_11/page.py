results = [x for x in range(1050)]

def page(data, size=100):
    '''分页'''

    length = len(data)
    pages = length//size

    rec = []
    i = 0
    while i < pages:
        start = i * size
        end = (i+1) * size
        rec.append(data[start:end])
        i = i + 1

    if length/size > pages:
        rec.append(data[end:])

    return rec

x = page(results)
print(x)

x = page(results, size=1000)
print(x)