# 1：
excelFile = "excel.xls"
workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet(u"top")
workbook.save(excelFile )

# 2:
excelFile = "excel.xlsx"
workbook = xlsxwriter.Workbook(topExcelFile)
sheet1 = workbook.add_worksheet("top")
workbook.close()
