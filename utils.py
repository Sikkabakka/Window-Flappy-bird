from screeninfo import get_monitors


def getMonitorDimensions():
    monitor = {
        "height": 0,
        "width": 0
    }
    for m in get_monitors():
        if (m.is_primary):
            monitor["height"], monitor["width"] = m.height, m.width
    return monitor      
    
