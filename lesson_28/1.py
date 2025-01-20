users = [
    {
        "first_name": "Angeline",
        "last_name":"Timothy",
        "email":"atimothy0@geocities.com",
        "gender":"Female",
        "ip_address":"48.93.26.14",
        "age": 12
    },
    {
        "first_name":"Shandy",
        "last_name":"Kierans",
        "email":"skierans1@surveymonkey.com",
        "gender":"Female",
        "ip_address":"164.225.85.37",
        "age": 15
    },
    {
        "first_name":"Scott",
        "last_name":"Ketton",
        "email":"sketton2@sogou.com",
        "gender":"Male",
        "ip_address":"71.70.178.85",
        "age": 10
    },
]

male_count = 0
female_count = 0

for user in users:
    if user['gender'] == 'Male':
        male_count += 1
    elif user["gender"] == 'Female':
        female_count += 1

total_count = len(users)

if total_count > 0:
    male_per = (male_count / total_count) * 100
    female_per = (female_count / total_count) * 100
else:
    male_per = 0
    female_per = 0

print(f"Erkaklar: {male_count}ta,  {male_per:.2f}%")
print(f"Ayollar: {female_count}ta, {female_per:.2f}%")

