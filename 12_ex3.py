import csv


class SalesForText:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_data_length(self):
        count = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                count += 1
            return count

    def get_total(self):
        total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                total += int(row)
            return total

    def get_surplus(self):
        surplus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                if int(row) >= 0:
                    surplus += int(row)
            return surplus

    def get_deficit(self):
        deficit = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                if int(row) < 0:
                    deficit += int(row)
            return deficit


class SalesForCSV(SalesForText):

    def get_total(self):
        total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                total += int(row[2])
            return total

    def get_surplus(self):
        surplus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if int(row[2]) >= 0:
                    surplus += int(row[2])
            return surplus

    def get_deficit(self):
        deficit = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if int(row[2]) < 0:
                    deficit += int(row[2])
            return deficit


csv_sales = SalesForCSV('sales.csv')
total_sales = csv_sales.get_total()
total_surplus = csv_sales.get_surplus()
total_deficit = csv_sales.get_deficit()
count = csv_sales.get_data_length()

print(total_sales, total_surplus, total_deficit)
print(f'件数 : {count} ')
