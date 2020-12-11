from openpyxl import Workbook, load_workbook


def excel_write_test(calories_add):
    book = load_workbook("sample.xlsx")
    sheet = book["Sheet"]

    # sheet['A1'].value = 1
    if sheet['A2'].value is None:
        sheet['A2'].value = 0

    sheet['A2'].value = sheet['A2'].value + calories_add

    book.save("sample.xlsx")


def read_cell(cell):
    book = load_workbook("sample.xlsx")
    sheet = book["Sheet"]
    return sheet[cell].value


def delete_cell(cell):
    book = load_workbook("sample.xlsx")
    sheet = book["Sheet"]
    sheet[cell].value = None
    book.save("sample.xlsx")

# excel_write_test()
#reset()

