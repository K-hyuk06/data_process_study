import random
import datetime
import csv


def make_attendance(prob):
    return random.random() < prob


def generate_late_time(date:datetime.date,distance):
    time_limit=datetime.datetime(year=date.year,month=date.month,day=date.day,hour=10,minute=0)
    late_time= random.randint(0,distance)
    
    return time_limit+datetime.timedelta(minutes=late_time)

def generate_daily_report(date: datetime.date):
    file_name = "employee.csv"
    report = []
    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader, None)

        for row in reader:
            first_name, last_name, prob, distance = row
            late_for_work = make_attendance(float(prob))
            attendance_time = generate_late_time(date=date, distance=int(distance))

            if late_for_work:
                report.append(
                    [
                        f"{first_name} {last_name}",
                        date,
                        attendance_time.strftime("%H:%M:%S"),
                    ]
                )
            else:
                report.append([f"{first_name} {last_name}", date, "10:00:00"])

    return report

if __name__=="__main__":
    test_date=datetime.date(2022,1,1)
    generate_daily_report(test_date)
    #예시 출력: 이름, 일자, 출근 시간
    # [['지영 김', datetime.date(2022, 1, 1), '10:00:00'], ['예원 박', datetime.date(2022, 1, 1), '10:00:00'], ['지우 신', datetime.date(2022, 1, 1), '10:00:00'], ['진우 문', datetime.date(2022, 1, 1), '10:12:00'], ['혜진 양', datetime.date(2022, 1, 1), '10:13:00']]

