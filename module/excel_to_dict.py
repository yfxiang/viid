import xlrd


class ExcelToDict(object):
    
    def __init__(self, excel_path, sheet_name):
        """
        初始化excel数据，获取指定页的列标题、总行数和总列数
        """
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行数据、列标题
        self.row = self.table.row_values(0)
        # 获取表格的总行数
        self.rowNum = self.table.nrows
        # 获取表格的总列数
        self.colNum = self.table.ncols
        # 设置默认从第二行开始
        self.curRowNo = 1
        
    def next(self):
        r = []
        while self.has_next():
            """
            循环获取excel数据，每次读取一行，
            每一行的数据作为一个字典，字典的键是每一列的标题。
            """
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r
    
    def has_next(self):
        """
        判断execl的数据是否已经读取完
        """
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True


if __name__ == '__main__':
    ExcelToDict("../data/test.xlsx", "Sheet1").next()
