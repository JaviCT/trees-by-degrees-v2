import json

with open('data/London.geojson', 'r+') as f:
    data = json.load(f)
    for data_point in data['features']:
        coords = data_point['geometry']['coordinates'][0][0]
        for point in coords:
            point[0]/=100000
            point[1]/=100000
            print(point)
    with open('out.json', 'w') as outfile:
        json.dump(data, outfile)
