import openpyxl

book = openpyxl.load_workbook("/home/shanky/PycharmProjects/Python_Testing_Selenium/Selenium_Framework/PythonDemo.xlsx")
sheet = book.active
cell = sheet.cell(row=2 , column=2)
print(cell.value)

