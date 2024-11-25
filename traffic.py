def traffic_light(action):
    switcher={
        'red':'stop',
        'yellow':'slow down',
        'green':'go'
    }
    return switcher.get(action,"Invalid action")
print(traffic_light('red'))
print(traffic_light('blue'))