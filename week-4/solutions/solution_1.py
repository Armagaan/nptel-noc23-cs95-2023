def rain_average(data_):
    '''Compute the average rainfall of cities. Sort the output alphabetically based on the city's name.'''
    # city: [values, count]
    averages = {}
    for item in data_:
        city = item[0]
        rain = item[1]
        # If we have seen this city before, update the values.
        if city in averages.keys():
            averages[city][0] += rain
            averages[city][1] += 1
        else:
            averages[city] = [rain, 1]
    
    output = [(key, val[0] / val[1]) for key, val in averages.items()]
    
    output.sort(key=lambda x: x[0])
    # This is same as:
    # def func(item):
    #     return item[0]
    # output.sort(key=func)

    return output

if __name__ == "__main__":
    data = [('Bombay', 848),('Madras', 103),('Bombay', 923),('Bangalore', 201),('Madras', 128)]
    print(rain_average(data))

    data = [('Bombay', 1848), ('Bombay', 923), ('Bombay', 201), ('Bombay', 128), ('Bombay', 103), ('Bombay', 948), ('Bangalore', 323)]
    print(rain_average(data))
