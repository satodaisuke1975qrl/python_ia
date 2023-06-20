class SalesForText:

    def __init__(self, file_name):
        self.file_name = file_name

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


sales = SalesForText('../sales.txt')
total_sales = sales.get_total()
total_surplus = sales.get_surplus()
total_deficit = sales.get_deficit()

print(total_sales, total_surplus, total_deficit)
