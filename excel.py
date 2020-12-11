from openpyxl import Workbook, load_workbook
import datetime


def excel_exist():
    from os import path
    if not path.exists("diet_diary.xlsx"):
        book = Workbook()
        sheet = book.active
        sheet['A1'] = "Date"
        sheet['B1'] = "Total Calories consumed"
        sheet['C1'] = "Net+-"
        sheet['D1'] = "Weight"
        sheet['E1'] = "Daily Calories: 1600"
        book.save("diet_diary.xlsx")
        print("diet_diary.xlsx doesnt exit. It has been created")
    else:
        print("Excel File exists.")


def excel_write_test(calories_add):
    book = load_workbook("diet_diary.xlsx")
    sheet = book.active

    if sheet['B2'].value is None:
        sheet['B2'].value = 0

    sheet['B2'].value = sheet['B2'].value + calories_add
    book.save("diet_diary.xlsx")


def read_cell(cell):
    book = load_workbook("diet_diary.xlsx")
    sheet = book.active
    return sheet[cell].value


def delete_cell(cell):
    book = load_workbook("diet_diary.xlsx")
    sheet = book.active
    sheet[cell].value = None
    book.save("diet_diary.xlsx")


def write_today_date_to_excel():
    book = load_workbook("diet_diary.xlsx")
    sheet = book.active
    a = 2
    dateset = True
    while dateset is True:
        if sheet['A' + str(a)].value is None:
            sheet['A' + str(a)] = datetime.date.today()
            dateset = False
        else:
            a += 1
    book.save("diet_diary.xlsx")


#excel_write_test(1)
#reset()
#excel_create()
#write_today_date_to_excel()
