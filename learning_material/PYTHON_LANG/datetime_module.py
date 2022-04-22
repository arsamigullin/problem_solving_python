from datetime import datetime
def getcurrenttime():
    dt = datetime.utcnow() # 2022-03-13 17:52:31.850754
    print(dt.minute)
    print(dt.hour)
    print(dt.year)
    print(dt.month)
    print(dt.second)
    print(dt.microsecond) # 850754
    print(dt.day)
    print(dt.max)
    print(dt.min)
    print(dt.time()) # 17:52:31.850754

def create_date():
    pivot = datetime(1970,1,1,0)
    dt = datetime.fromisoformat('2022-03-13 17:52:31.850754')
    res = dt - pivot
    mins = int(res.total_seconds()//60)
    print(mins)
    print(isinstance(mins, int))

if __name__ == '__main__':
    create_date()