import re

def validate_car_number(car_id):
    pattern = r'^[А-ЯA-Z]{1}\d{3}[А-ЯA-Z]{2}(\d{2,3})$'
    match = re.match(pattern, car_id)

    if match:
        number_part = car_id[:-2]  # Все, кроме последних двух символов
        region_part = car_id[-2:]  # Последние два символа (может быть три)
        return f"Номер {number_part} валиден. Регион: {region_part}."
    else:
        return "Номер не валиден."

while True:
    car_id = input("Введите транспортный номер или 'exit' для выхода: ")
    if car_id.lower() == 'exit':
        print("Выход из программы.")
        break

    result = validate_car_number(car_id)
    print(result)



