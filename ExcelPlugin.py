from openpyxl import Workbook

class Excel:

    def __init__(self):
        self.workbook = Workbook()
        self.workspace = self.workbook.active

    def set_file(self):
        print("Esta wea ya se cargo")