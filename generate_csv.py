# generate_csv.py
import csv, random
from datetime import datetime, timedelta

first = ["Aisha","Bilal","Chen","Diego","Elena","Fatima","Gopal","Hiro","Ibrahim","Jamal","Khadija","Liam","Maya","Nadia","Omar","Priya","Qasim","Rana","Sofia","Tariq"]
last = ["Khan","Ahmed","Li","Lopez","Garcia","Ali","Patel","Yamada","Hussain","Singh","Malik","Cruz","Nguyen","Hassan","Zhang","Sharma","Iqbal","Raza","Saeed","Kaur"]
departments = ["Engineering","Sales","Marketing","Product","HR","Customer Success","Finance","Data","Design"]
locations = ["Lahore,PK","Karachi,PK","Islamabad,PK","Hyderabad,PK","Peshawar,PK","Remote,PK","Dhaka,BD","Istanbul,TR","London,UK","San Francisco,US"]
def random_date(start_year=2015, end_year=2024):
    start = datetime(start_year,1,1)
    end = datetime(end_year,12,31)
    return (start + (end-start)*random.random()).date().isoformat()

with open("employees_large.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["emp_id","name","email","department","salary","hire_date","location","remote","performance_score","projects_completed"])
    for i in range(1, 501):
        fn = random.choice(first)
        ln = random.choice(last)
        name = f"{fn} {ln}"
        email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
        dept = random.choice(departments)
        # salary ranges vary by dept
        base = {"Engineering":70000,"Data":68000,"Product":75000,"Design":60000,"Sales":45000,"Marketing":50000,"HR":40000,"Finance":65000,"Customer Success":42000}
        salary = base.get(dept,50000) + random.randint(-10000,30000)
        hire = random_date()
        loc = random.choice(locations)
        remote = random.choice(["yes","no","sometimes"])
        perf = round(max(1.0, min(5.0, random.gauss(3.4, 0.8))),1)  # score 1.0-5.0
        proj = random.randint(0, 25)
        writer.writerow([i, name, email, dept, salary, hire, loc, remote, perf, proj])
print("employees_large.csv generated (500 rows)")
