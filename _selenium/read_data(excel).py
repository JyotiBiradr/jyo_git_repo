from xlrd import open_workbook
def read_data(sheet_name,test_case_name):
    wb=open_workbook("./data_files/testdata.xls")
    ws=wb.sheet_by_name(sheet_name)
    used_rows=ws.nrows
    for i in range(0,used_rows):
        row=ws.row_values(i)
        if row[0]==test_case_name:
            headers = ws.row_values(i - 1)
            headers=[header for header in headers if header]
            print(",".join(headers[2:]))
            break
            #headers=ws.row_values(i-1)
            #print(headers)
            #break

read_data('smoke','test_registration')



