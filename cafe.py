import csv


class Cafe:
    def __init__(self, name="", location="", open_time="", close_time="", coffee_rate="", wifi_rate="", power_rate=""):
        self.name = name
        self.location = location
        self.open_time = open_time
        self.close_time = close_time
        self.coffee_rate = coffee_rate
        self.wifi_rate = wifi_rate
        self.power_rate = power_rate
        
    def get_all_cafes(self):
        with open('cafe-data.csv', 'r', encoding='utf8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
            list_of_rows.pop(0)
        return list_of_rows

    def get_all_cafes_headers(self):
        with open('cafe-data.csv', 'r', encoding='utf8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
            return list_of_rows[0]
