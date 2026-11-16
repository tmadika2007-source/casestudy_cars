first_line = list()

data = {}

with open("cars.csv") as CSV_file:
    i = 0
    for row in CSV_file:
        formatted_row = row.strip('"').split('","')
        formatted_row[-1] = formatted_row[-1].rstrip('"\r\n')
        if i == 0:
            first_line = formatted_row
        else:
            data[i - 1] = {
                first_line[j]: formatted_row[j]
                for j in range(len(first_line))
            }

        i += 1

#Basic Get Car data by CAR_ID. CAR_ID ranges from 0-len(data)
def get_car(car_id):
    if car_id in data:
        return data[car_id]
    else:
        return None

print(get_car(4))



def get_brands():
    car_brands = []
    for brand in data:
        if data[brand]["Identification.Make"] not in car_brands:
            car_brands.append(data[brand]["Identification.Make"])
    return car_brands

print(get_brands())
