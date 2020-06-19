from datetime import datetime

def call_time(record):
    """ 
    Function to calculate the time of the call using the timestamps of the records file.

    Parameters

    record : dict
        Dictionary with the origin and timestamps of the beginning and end of calls.

    Return

    total_minutes : int
        Total call duration in minutes. 

    """
    start = datetime.fromtimestamp(record["start"])
    end = datetime.fromtimestamp(record["end"])
    if int(start.hour) >= 22 and int(start.minute) >= 00:
        start = start.replace(hour=22, minute=00, second=00)
    elif int(start.hour) <= 6:
        start = start.replace(hour=6, minute=00, second=00)
    if int(end.hour) >= 22 and int(end.minute) >= 0:
        end = end.replace(hour=22, minute=00, second=00)
    elif int(end.hour) <= 6:
        end = end.replace(hour=6, minute=00, second=00)
    duration = end - start
    total_minutes = (int(duration.seconds) // 60)
    return total_minutes

def classify_by_phone_number(records):
    """
    Function that creates the phone list and total value with the help of other functions.

    Parameters

    records: list

        List containing dictionaries with call informations.

    Return
    
    bill : list

        List with total values by source number.
    """
    bill = []
    for i in records:
        x = {}
        duration = call_time(i)
        cost = round((duration * 0.09) + 0.36, 2)
        x["source"] = i["source"]
        x["total"] = cost
        check(x, cost, bill)
        bill = sorted(bill, key = lambda i: i['total'], reverse=True)
    return bill

def check(source, cost, bill):
    """ 
    Function to add values to source numbers in the bill list.

    Parameters

    source : str
        Call source number.

    cost : int
        Call value to be added. 

    bill : list
        List where the origin and cost of the call will be added.

    Return

    bill : list
        List containin call sources and costs.    

    """
    for dic in bill:
        if source['source'] in dic.values():
            dic["total"] = round(dic["total"] + cost, 2)
            return bill
    bill.append(source)
    return bill
records = [

    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},

    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},

    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},

    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},

    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},

    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},

    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},

    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}

]

print(classify_by_phone_number(records))