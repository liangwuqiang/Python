import xlrd

"""2、打开Excel文件读取数据"""
data = xlrd.open_workbook('excelFile.xls')

"""获取一个工作表"""
table = data.sheets()[0]
# table = data.sheet_by_index(0)
# table = data.sheet_by_name(u'Sheet1')

"""获取整行和整列的值（数组）"""
row = table.row_values(0)
col = table.col_values(0)

"""获取行数和列数"""
nrows = table.nrows
ncols = table.ncols

"""循环行列表数据"""
for i in range(nrows):
    print(table.row_values(i))

"""单元格"""
cell_A1 = table.cell(0, 0).value
cell_A2 = table.cell(1, 0).value
# print(cell_A1, cell_C4)

"""使用行列索引"""
_cell_A1 = table.row(0)[0].value
_cell_A2 = table.col(1)[0].value
print(_cell_A1, _cell_A2)

"""简单的写入"""
_row = 2
_col = 2
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1
value = '单元格的值'

xf = 0  # 扩展的格式化
table.put_cell(_row, _col, ctype, value, xf)

cell1 = table.cell(2, 2)  # 单元格的值'
cell2 = table.cell(2, 2).value  # 单元格的值'

print(cell1, cell2)


"""打印输出"""
text = nrows
print(type(text))
print(text)



