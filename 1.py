from datetime import datetime
from typing import Dict, Union

student_details: Dict[int, Dict[str, Union[str, datetime]]] = {

    1: {
        'name': 'John Doe',
        'address': '123 Elm Street, Springfield',
        'email': 'john.doe@example.com',
        'phone': '+1234567890',
        'enrollment_date': datetime(2022, 1, 15)
    },
    2: {
        'name': 'Maaya Patel',
        'address': '456 Oak Avenue, Metropolis',
        'email': 'maaya.patel@example.com',
        'phone': '+0987654321',
        'enrollment_date': datetime(2023, 2, 20)
    },
    3: {
        'name': 'Aditya Singh',
        'address': '789 Maple Lane, Gotham',
        'email': 'aditya.singh@example.com',
        'phone': '+1122334455',
        'enrollment_date': datetime(2021, 3, 25)
    },
    4: {
        'name': 'Rocky Balboa',
        'address': '101 Pine Road, Star City',
        'email': 'rocky.balboa@example.com',
        'phone': '+5566778899',
        'enrollment_date': datetime(2020, 4, 30)
    },
    5: {
        'name': 'Sachin Tendulkar',
        'address': '202 Birch Drive, Sunnydale',
        'email': 'sachin.tendulkar@example.com',
        'phone': '+6677889900',
        'enrollment_date': datetime(2024, 5, 10)
    }
}



print(student_details[1]['name'])   