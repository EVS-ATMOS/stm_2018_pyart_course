reflectivity = [radar.fields['velocity']['data'][x].mean() for x in radar.iter_slice()]
print(reflectivity)