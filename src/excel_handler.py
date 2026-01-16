import win32com.client as win32
import pyautogui
import time

class ExcelRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        try:
            self.excel = win32.gencache.EnsureDispatch('Excel.Application')
        except:
            self.excel = win32.Dispatch('Excel.Application')
        
        self.excel.Visible = True
        self.wb = self.excel.Workbooks.Add()
        self.ws = self.wb.ActiveSheet
        self.pixel_range = self.ws.Range(self.ws.Cells(1, 1), self.ws.Cells(height, width))
        self._prepare_sheet()
        self.focus_excel()

    def _prepare_sheet(self):
        self.pixel_range.ColumnWidth = 1 
        self.pixel_range.RowHeight = 10
        self.pixel_range.FormatConditions.Delete()
        
        c1 = self.pixel_range.FormatConditions.Add(1, 3, "1")
        c1.Interior.Color = 0x000000
        c1.Font.Color = 0x000000 
        
        c0 = self.pixel_range.FormatConditions.Add(1, 3, "0")
        c0.Interior.Color = 0xFFFFFF
        c0.Font.Color = 0xFFFFFF 

    def is_alive(self):
        try:
            return self.excel.Visible
        except:
            return False

    def focus_excel(self):
        try:
            time.sleep(0.5)
            win = pyautogui.getWindowsWithTitle(self.wb.Name)
            if win: win[0].activate()
        except:
            pass

    def update_frame(self, data):
        try:
            self.excel.ScreenUpdating = False
            self.pixel_range.Value2 = data 
            self.excel.ScreenUpdating = True
        except:
            pass

    def stop(self):
        try:
            if self.excel:
                self.excel.ScreenUpdating = True
        except:
            pass
