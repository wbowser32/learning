import PySimpleGUI as sg
import csv
import pandas as pd
import openpyxl

sg.theme("DarkTeal2")
layout = [[sg.T("")],
          [sg.Text("Choose a file: "), sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN-")],
          [sg.Button('Submit'), sg.Cancel()]]
layout2 = [[sg.T("")],
          [sg.Text("Choose a folder: "), sg.Input(key="-IN3-", change_submits=True), sg.FolderBrowse(key="-IN4-")],
          [sg.Button('Submit'), sg.Cancel()]]
layout3 = [[sg.T("")],
          [sg.Text("Enter a Name"), sg.Input(key="-IN5-", change_submits=True)],
          [sg.Button('Submit'), sg.Cancel()]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600, 150))
window2 = sg.Window('Where to Save This File', layout2, size=(600, 150))
window3 = sg.Window('What to name this folder', layout3, size=(600, 150))

while True:
    event, values = window.read()
    #print(values["-IN2-"])
    if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
        break
    elif event == "Submit":
        window.close()
        wb = openpyxl.Workbook()
        ws = wb.active
        path = values["-IN-"]
        with open(path) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                ws.append(row)
            while True:
                event2, values2 = window2.read()
                    # print(values["-IN2-"])
                if event2 == sg.WIN_CLOSED or event2 == "Exit" or event2 == "Cancel":
                    break
                elif event2 == "Submit":
                    window2.close()
                    path2 = values2["-IN4-"]
                    while True:
                        event3, values3 = window3.read()
                        # print(values["-IN2-"])
                        if event3 == sg.WIN_CLOSED or event3 == "Exit" or event3 == "Cancel":
                            break
                        elif event3 == "Submit":
                            path3 = values3["-IN5-"]
                            wb.save(path2 + "/" + path3 + ".xlsx")
                            break

        #print(values["-IN-"])
        #data = pd.read_excel(path)
        #for label, row in data.iterrows():
            #A = row["InternalNo"]
            #B = row["%W2dEnabled%"]
            #filename = "C:\\Users\\BowDa001\\Desktop\\Hourly Walmart Task\\NEW FILE NEW FORMAT\HiTouchW2DEligible20201201T181724Z.csv"
            #file = openpyxl.load_workbook(filename)
                #sheet = wb[]