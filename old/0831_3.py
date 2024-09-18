import openpyxl

wb = openpyxl.load_workbook(r"C:\Users\turnt\OneDrive\デスクトップ\Python\2023_July\a.xlsx")
sheet = wb["sample"]
sheet["A1"].value = 666
wb.save(r"C:\Users\turnt\OneDrive\デスクトップ\Python\2023_July\a.xlsx")
wb.close()