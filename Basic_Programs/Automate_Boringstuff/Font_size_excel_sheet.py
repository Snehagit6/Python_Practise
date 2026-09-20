from openpyxl import Workbook,cell
from openpyxl.styles import Color
from openpyxl.styles.colors import BLUE

wb = Workbook()
sheet = wb.active
cell_color = Color(BLUE)
c = sheet['A1']
c.cell_color
wb.save("G://Cell_color.xlsx")




