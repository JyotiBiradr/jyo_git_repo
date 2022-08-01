#read locators from excel
from xlrd import open_workbook
def read_locator(page_name):
    wb=open_workbook(r".\data_files\objects.xls")
    #wb=open_workbook(r"C:\Users\SANKETH\Desktop\python practice\selenium1\objects.xls")
    ws=wb.sheet_by_name(page_name)
    used_rows=ws.nrows
    locators={}
    for i in range(1,used_rows):
        data=ws.row_values(i)
        locators[data[0]]=(data[1],data[2])
    return locators

print(read_locator("loginpage"))