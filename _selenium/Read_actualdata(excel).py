from xlrd import open_workbook
def Read_actual_data(sheet_name,test_case_name):
    actual_data=[]
    wb=open_workbook("./data_files/testdata.xls")
    ws=wb.sheet_by_name(sheet_name)
    used_rows=ws.nrows
    for i in range(0,used_rows):
        row=ws.row_values(i) #row consist of list
        if row[0]==test_case_name:
            data=[item for item in row if item]  #removing empty values
            actual_data.append(data[2:])
    return actual_data

print(Read_actual_data("smoke","test_registration"))

