import requests

headers = {
    "X-API-KEY": "c612c439d54a20c20ef53aecde0967c7",
    "cfclearance": "true",
    "Accept": "application/json"
}
id = 12734

students_information = requests.get(f"https://intranet.hbtn.io/api/v1/students/{id}",headers=headers).json()
events_information = requests.get('https://intranet.hbtn.io/api/v1/events', headers=headers).json()

name_surname = f"---------------------------------\n{students_information['first_name']} {students_information['last_name']} - {students_information['id']}"
scores = f"""\nProgram - {students_information['product']['title']}
---------------------------------
Average Score - {students_information['product']['average']}
Optional Average - {students_information['product']['optional_average']}
Professional Average - {students_information['product']['professional_average']}
---------------------------------
"""


def print_events():
    print('Information About the Events: ')
    passage = ""
    for e in events_information["items"]:
        passage += (f"""
Title: {e['title']}
Start: {e['start_at']}
End:   {e['end_at']}
Location: {e['location']}
---------------------------------
        """)
    print(passage)

print(name_surname, scores)
print_events()