from PySimpleGUI import *
import PySimpleGUI as sg
 
sg.theme('SandyBeach') 

#BAGIAN SHOW TABLE CREDIT
headings = ['GRADE', 'GP', 'Percentage']
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
input_rows = [[sg.Text('           A+', size=(15,1), pad=(0,0)),sg.Text('       4.3', size=(15,1), pad=(0,0)),sg.Text('          100-90', size=(15,1), pad=(0,0))],
              [sg.Text('           A', size=(15,1), pad=(0,0)),sg.Text('       4.0', size=(15,1), pad=(0,0)),sg.Text('          89-85', size=(15,1), pad=(0,0))],
              [sg.Text('           A-', size=(15,1), pad=(0,0)),sg.Text('       3.7', size=(15,1), pad=(0,0)),sg.Text('          84-80', size=(15,1), pad=(0,0))],
              [sg.Text('           B+', size=(15,1), pad=(0,0)),sg.Text('       3.3', size=(15,1), pad=(0,0)),sg.Text('          79-77', size=(15,1), pad=(0,0))],
              [sg.Text('           B', size=(15,1), pad=(0,0)),sg.Text('       3.0', size=(15,1), pad=(0,0)),sg.Text('          76-73', size=(15,1), pad=(0,0))],
              [sg.Text('           B-', size=(15,1), pad=(0,0)),sg.Text('       2.7', size=(15,1), pad=(0,0)),sg.Text('          72-70', size=(15,1), pad=(0,0))],
              [sg.Text('           C+', size=(15,1), pad=(0,0)),sg.Text('       2.3', size=(15,1), pad=(0,0)),sg.Text('          69-67', size=(15,1), pad=(0,0))],
              [sg.Text('           C', size=(15,1), pad=(0,0)),sg.Text('       2.0', size=(15,1), pad=(0,0)),sg.Text('          66-63', size=(15,1), pad=(0,0))],
              [sg.Text('           C-', size=(15,1), pad=(0,0)),sg.Text('       1.7', size=(15,1), pad=(0,0)),sg.Text('          62-60', size=(15,1), pad=(0,0))],
              [sg.Text('           D', size=(15,1), pad=(0,0)),sg.Text('       1.0', size=(15,1), pad=(0,0)),sg.Text('          59-50', size=(15,1), pad=(0,0))],
              [sg.Text('           E', size=(15,1), pad=(0,0)),sg.Text('       0.0', size=(15,1), pad=(0,0)),sg.Text('          49-1', size=(15,1), pad=(0,0))],
              [sg.Text('           X', size=(15,1), pad=(0,0)),sg.Text('       0.0', size=(15,1), pad=(0,0)),sg.Text('            0', size=(15,1), pad=(0,0))]]
layout4 = header+input_rows
#BAGIAN SHOW TABLE CREDIT
#BAGIAN DISPLAY FINAL GRADE
layout2 = [[sg.Text('Grade(0-100)              ', font=('Arial',24)),sg.Text('Weight (%)', font=('Arial',24))],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.Button('Calculate Grade')]]
#BAGIAN DISPLAY FINAL GRADE

#BAGIAN DISPLAY GPA
layout3 = [[sg.Text('GP(0-4.3)                   ', font=('Arial',24)),sg.Text('Credit Hours', font=('Arial',24))],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.InputText(0),sg.InputText(0)],
           [sg.Button('Calculate GPA')]]
#BAGIAN DISPLAY GPA
#BAGIAN DISPLAY AWAL
layout1 = [[sg.Text('Made By :', font=('Arial',24))],
           [sg.Text('Hanwell         109006237', font=('Arial',24))],
           [sg.Text('Jansen R G   109006240', font=('Arial',24))],
           [sg.Text('Kenneth         109006106', font=('Arial',24))],
           [sg.Text('DATA USED BASED ON NTHU GPA TABLE CREDIT',text_color='red' , font=('Arial',24))],
           [sg.Text('https://registra.site.nthu.edu.tw/var/file/211/1211/img/75/GPAConversionChart.pdf', font=('Arial',13))]]
#BAGIAN DISPLAY AWAL
#DISPLAY TOMBOL BAWAH
layout  = [[sg.Column(layout1, key='-TEAM-'),sg.Column(layout2, key='-GRADE-', visible=False), sg.Column(layout3, visible=False, key='-GPA-'), sg.Column(layout4, visible=False, key='-TABLE-')],
           [sg.Text('MENU :', size = (16,1), font = ('Arial', 16)),Text('', size = (15, 1), font = ('Helvetica', 18),text_color = 'black', key = 'input')],
          [sg.Button('GRADE', font=('Arial',14)),sg.Button('GPA', font=('Arial',14)),sg.Button('TABLE', font=('Arial',14)),sg.Button('Quit', font=('Arial',14))
          ]]
#DISPLAY TOMBOL BAWAH

window = sg.Window('NTHU GRADE TOOL', layout)
while True:
    event, value = window.Read()
#Transisi
    if event == 'GRADE':
        window[f'-GRADE-'].update(visible=True)
        window[f'-GPA-'].update(visible=False)
        window[f'-TABLE-'].update(visible=False)
        window[f'-TEAM-'].update(visible=False)
    elif event=='GPA':
        window[f'-GRADE-'].update(visible=False)
        window[f'-GPA-'].update(visible=True)
        window[f'-TABLE-'].update(visible=False)
        window[f'-TEAM-'].update(visible=False)
    elif event=='TABLE':
        window[f'-GRADE-'].update(visible=False)
        window[f'-GPA-'].update(visible=False)
        window[f'-TABLE-'].update(visible=True)
        window[f'-TEAM-'].update(visible=False)
        window.FindElement('input').Update(visible=False)
    elif event=='TEAM':
        window[f'-GRADE-'].update(visible=False)
        window[f'-GPA-'].update(visible=False)
        window[f'-TABLE-'].update(visible=False)
        window[f'-TEAM-'].update(visible=True)
#Transisi

#Perhitungan
    elif event=='Calculate Grade':
        finalgrade=0
        for i in range (0,20,2):
            finalgrade = finalgrade + (float(value[i])*float(value[i+1])/100)
        finalgrade = round(finalgrade,2)
        print(finalgrade)
        window.FindElement('input').Update(finalgrade, visible=True)
    elif event=='Calculate GPA':
        totalcredit = 0
        for i in range (20,39,2):
            totalcredit = totalcredit + (float(value[i+1]))
        finalgpa = 0
        for i in range (20,39,2):
            finalgpa= finalgpa + (float(value[i])*float(value[i+1])/totalcredit)
        finalgpa= round(finalgpa,2)
        print(finalgpa)
        window.FindElement('input').Update(finalgpa, visible=True)
#Perhitungan

#Keluar
    elif event == 'Quit'  or event == None:
        break
#Keluar
