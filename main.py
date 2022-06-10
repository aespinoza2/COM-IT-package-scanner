from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Designate Our .kv design file
# Builder.load_file('main.kv')

class AppLayout(Widget):
    pass

class PackageScanner(App):
    def build(self):
        return AppLayout()


if __name__ == '__main__':
    PackageScanner().run()

# from tkinter.filedialog import asksaveasfilename
# from graphics import *
#
#
# def main():
#     win, tracIn, ticIn, macIn = winCreate()
#     checkBoxes(win, tracIn, ticIn, macIn)
#     win.close()
#
# def winCreate():
#     # Window create
#     win = GraphWin("COM IT Package Scanner", 550, 400)
#     win.setBackground(color_rgb(255, 255, 255))
#     # Logo
#     label = Image(Point(win.getWidth()/2, 47), 'logo_edit.png')
#     label.draw(win)
#     # Heading
#     # head = Text(Point(win.getWidth()/2,45), "Scan the package barcodes.\nSelect the 'Check' button to format.\nCopy and paste the formatted IDs into Snipe-It.")
#     # head.setTextColor("grey")
#     # head.setSize(10)
#     # head.draw(win)
#     # Entry title
#     tracNum = Text(Point(100, 100), "Tracking")
#     ordNum = Text(Point(100, 150), "Order")
#     ticNum = Text(Point(100, 200), "Ticket")
#     serialNum = Text(Point(100, 250), "Serial")
#     macNum = Text(Point(100,300), "MAC")
#     comNum = Text(Point(90, 350), "Asset Tag")
#     # Entry title color
#     tracNum.setTextColor('black')
#     ordNum.setTextColor('black')
#     ticNum.setTextColor('black')
#     serialNum.setTextColor('black')
#     macNum.setTextColor('black')
#     comNum.setTextColor('black')
#     # Entry title style (bold)
#     tracNum.setStyle('bold')
#     ordNum.setStyle('bold')
#     ticNum.setStyle('bold')
#     serialNum.setStyle('bold')
#     macNum.setStyle('bold')
#     comNum.setStyle('bold')
#     # Entry title size
#     tracNum.setSize(9)
#     ordNum.setSize(9)
#     ticNum.setSize(9)
#     serialNum.setSize(9)
#     macNum.setSize(9)
#     comNum.setSize(9)
#     # Entry title create
#     tracNum.draw(win)
#     ordNum.draw(win)
#     ticNum.draw(win)
#     serialNum.draw(win)
#     macNum.draw(win)
#     comNum.draw(win)
#     # Entry field
#     tracIn = Entry(Point(275, 100), 30)
#     ordIn = Entry(Point(275, 150), 30)
#     ticIn = Entry(Point(275, 200), 30)
#     serialIn = Entry(Point(275, 250), 30)
#     macIn = Entry(Point(275, 300), 30)
#     comIn = Entry(Point(275, 350), 30)
#     # Entry fill color
#     tracIn.setFill('#ffffff')
#     ordIn.setFill('#ffffff')
#     ticIn.setFill('#ffffff')
#     serialIn.setFill('#ffffff')
#     macIn.setFill('#ffffff')
#     comIn.setFill('#ffffff')
#     # Entry text color
#     tracIn.setTextColor('black')
#     ordIn.setTextColor('black')
#     ticIn.setTextColor('black')
#     serialIn.setTextColor('black')
#     macIn.setTextColor('black')
#     comIn.setTextColor('black')
#     # Entry COM -
#     comIn.setText('COM-')
#     # Entry create
#     tracIn.draw(win)
#     ordIn.draw(win)
#     ticIn.draw(win)
#     serialIn.draw(win)
#     macIn.draw(win)
#     comIn.draw(win)
#
#     return win, tracIn, ticIn, macIn
#
# def inside(clickPoint, okBox):
#     # Is point inside rectangle?
#     ll = okBox.getP1()  # assume p1 is ll (lower left)
#     ur = okBox.getP2()  # assume p2 is ur (upper right)
#
#     return ll.getX() < clickPoint.getX() < ur.getX() and ll.getY() < clickPoint.getY() < ur.getY()
#
# def checkBoxes(win, tracIn, ticIn, macIn):
#     # Tracking button
#     tracCheck = Rectangle(Point(450, 87), Point(490, 107))
#     tracCheck.setFill('#296d98')
#     tracText = Text(Point(470, 97), "Check")
#     tracText.setSize(8)
#     tracText.setFill('white')
#     tracCheck.draw(win)
#     tracText.draw(win)
#
#     # Ticket button
#     ticCheck = Rectangle(Point(450, 190), Point(490, 210))
#     ticCheck.setFill('#296d98')
#     ticText = Text(Point(470, 200), "Check")
#     ticText.setSize(8)
#     ticText.setFill('white')
#     ticCheck.draw(win)
#     ticText.draw(win)
#
#     # MAC button
#     macCheck = Rectangle(Point(450, 290), Point(490, 310))
#     macCheck.setFill('#296d98')
#     macText = Text(Point(470, 300), "Check")
#     macText.setSize(8)
#     macText.setFill('white')
#     macCheck.draw(win)
#     macText.draw(win)
#
#     # Exit button
#     xButton = Circle(Point(530, 375), 7)
#     xButton.setFill('red')
#     xButton.draw(win)
#
#
#     while True:
#         clickPoint = win.getMouse()
#         if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
#             tracText.setText("")
#         elif inside(clickPoint, tracCheck):
#             tracList = []
#             tracVal = tracIn.getText()
#             for i in range(len(tracVal)):
#                 tracList.append(tracVal[i])
#             if len(tracList) > 18:
#                 tracList = tracList[-18:]
#                 tracVal = "0"
#                 for i in range(len(tracList)):
#                     tracVal = tracVal + tracList[i]
#                 tracIn.setText(tracVal[1:])
#             # break
#
#         elif inside(clickPoint, ticCheck):
#             ticList = []
#             ticVal = ticIn.getText()
#             for i in range(len(ticVal)):
#                 ticList.append(ticVal[i])
#             if len(ticList) > 10:
#                 ticList = ticList[-10:]
#                 ticVal = "0"
#                 for i in range(len(ticList)):
#                     ticVal = ticVal + ticList[i]
#                 ticIn.setText(ticVal[1:])
#             # break
#         elif inside(clickPoint, macCheck):
#             macList = []
#             macFmtList = []
#             macVal = macIn.getText()
#             for i in range(len(macVal)):
#                 macList.append(macVal[i])
#             macVal = "0"
#             # print(macList)
#             for i in range(len(macList)):
#                 if i in (1,3,5,7,9):
#                     macFmtList.append(macList[i])
#                     macFmtList.append("-")
#                 elif i == len(macList):
#                     macFmtList.append(macList[i])
#                     macFmtList.append(macList[i+1])
#                 else:
#                     macFmtList.append(macList[i])
#                 macVal = macVal + macFmtList[i]
#             macVal = macVal + macFmtList[12] + macFmtList[13] + macFmtList[14] + macFmtList[15]+ macFmtList[16]
#             # print(macFmtList)
#             # print(macVal)
#             macIn.setText(macVal[1:])
#             # break
#         elif inside(clickPoint, xButton):
#             break
#
#     return
#
#
# main()