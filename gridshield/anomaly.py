import statistics

history=[]

def detect_anomaly(value):

    history.append(value)

    if len(history) < 3:
        return False

    avg = statistics.mean(history)

    if abs(value-avg) > 200:
        return True

    return False