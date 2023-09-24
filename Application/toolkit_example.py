from datetime import datetime
from tkinter import *
import json
from tkinter import ttk
import tkinter.messagebox
 
# create main form
mainForm = Tk()

# create json readable object
filename = 'ast.json'
f = open(filename)
data = json.load(f)

# root window title and dimension
mainForm.title("Service Toolkits")
# Set root window properties
mainForm.geometry('800x600')
mainForm.resizable(False,False)

# variable for log file
logfile = 'logfile.log'

########## functions ##########

# writeGenericData function writes X number of generic entries with a 
# sequential ID following the last index of the JSON collection
# and also displays messageboxes based on the actions taken
# the generic entries can be modified later
# it appends to the end of the JSON file
# and logs how many records were written
def writeGenericData():
    txt = txtProductCnt.get()
    acceptables=['1','2','3','4','5','6','7','8','9','10']
    count = int(txt)
    if txt not in acceptables:
        tkinter.messagebox.showinfo("Notification", "Please enter number of records to add (Maximum value 10) (Numeric values only)")
        logger("WARNING,WRITE", "No new records added as count is: " + txt)
    else:
        for i in range(count):
            jsonObjectCount = len(data)
            jsonObjectCount = jsonObjectCount + 1
            jsonCount = jsonObjectCount
            data.append({
                "ID": str(jsonCount),
                "summary": "[AST] - Provide summary - " + "KB" + str(jsonCount),
                "product": "Please provide product",
                "status": "U",
                "issueType": "AST",
                "astLastUpdated": "",
                "file": "Please enter filename"
                })
            logger("SUCCESS,WRITE", "Data added for new ID: " + str(jsonCount))
        print(data)
        with open (filename, 'w') as json_file:
            json.dump(data, json_file, indent=4, separators=(',',': '))
    txtProductCnt.delete(0, END)
    txtProductCnt.insert(0, '0')
    clearControls()

# loadData function loads JSON data into the tkinter treeview control
# data is sorted sequentially ascending based on the JOSN order and the ID value
# it will only display values that have not had their status marked as D (Disabled)
# the listview control only displays the ID and summary values from JSON
# and logs how many records were listed
def loadData():
    treeReleased.delete(*treeReleased.get_children())
    count = 0
    for x in data:
        if x['status'] != 'D':
            treeReleased.insert('', 'end', text="", values=(x['ID'], x['summary'], x['product'], x['status'], x['issueType'], x['astLastUpdated'], x['file']))
            count = count + 1
    logger("SUCCESS,LOAD", str(count) + " Records displayed in listview")

# selectItem function is called when the tkinter listview control has an item selected and populates
# label fields on the form with all the data associated with an ID
# and logs that data was displayed for the selected ID
def selectItem(a):
    item = treeReleased.focus()
    temp = treeReleased.item(item, 'values')
    lblID.config(text= 'ID: ' + temp[0])
    lblSummary.config(text = 'Summary: ' + temp[1])
    lblProduct.config(text = 'Product: ' + temp[2])
    lblStatus.config(text = 'Status: ' + temp[3])
    lblIssueType.config(text = 'Issue Type: ' + temp[4])
    lblUpdated.config(text = 'Last Updated: ' + temp[5])
    lblFile.config(text = 'File: ' + temp[6])
    txtSummary.delete(0, END)
    txtSummary.insert(0, temp[1])
    txtProduct.delete(0, END)
    txtProduct.insert(0, temp[2])
    txtStatus.delete(0, END)
    txtStatus.insert(0, temp[3])
    txtIssueType.delete(0, END)
    txtIssueType.insert(0, temp[4])
    txtUpdated.delete(0, END)
    txtUpdated.insert(0, temp[5])
    txtFile.delete(0, END)
    txtFile.insert(0, temp[6])
    logger("SUCCESS,SELECT", "Data displayed for ID: " + temp[0])

# deleteJSON will mark any selected record from the listview control as D (Disbaled)
# and also displays a message that the ID was disabled
# and logs the selected ID as disabled
def deleteJSON():
    item = treeReleased.focus()
    temp = treeReleased.item(item, 'values')
    idval = ""
    msg_box = tkinter.messagebox.askquestion("Notification", "Are you sure you want to mark the selected record as deleted?", icon='warning')
    if msg_box == 'yes':
        if treeReleased.focus():
            for x in data:
                if x['ID'] == temp[0]:
                    x['status'] = 'D'
                    idval = x['ID']
                    logger("DELETE,INFO", "Status marked as deleted for ID: " + temp[0])
    with open (filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',',': '))
    tkinter.messagebox.showinfo("Notification", idval + " marked as deleted")
    clearControls()

# updateJSON function will update the selected ID fom the listbox with the values from the input controls
# that can be entered by the user
# Updates will only occur on a yes answer to the messagebox prompt
# and log will be written to display the current/old values (label controls populated by selectItem function)
# and the new updated values
def updateJSON():
    item = treeReleased.focus()
    temp = treeReleased.item(item, 'values')
    msg_box = tkinter.messagebox.askquestion("Notification", "Are you sure you want to update the selected record?", icon='warning')
    if msg_box == 'yes':
        if treeReleased.focus():
            for x in data:
                if x['ID'] == temp[0]:
                    x['summary'] = txtSummary.get()
                    x['product'] = txtProduct.get()
                    x['status'] = txtStatus.get()
                    x['issueType'] = txtIssueType.get()
                    x['astLastUpdated'] = txtUpdated.get()
                    x['file'] = txtFile.get()
            logger("UPDATE,INFO", "Original values for: " + temp[0] + ' - ' + x['summary'] + ' - ' + x['product'] + ' - ' + x['status'] + ' - ' + x['issueType'] + ' - ' + x['astLastUpdated'] + ' - ' + x['file'])
            logger("UPDATE,INFO", "New updated values for: " + temp[0] + ' - ' + txtSummary.get() + ' - ' + txtProduct.get() + ' - ' + txtStatus.get() + ' - ' + txtIssueType.get() + ' - ' + txtUpdated.get() + ' - ' + txtFile.get())
    else:
        logger("UPDATE,WARNING", "No updated values for: " + temp[0])
    with open (filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',',': '))
    clearControls()

# restoreJSON function will set any ID's at status D (Disbaled) to U (Unreleased) 
# so they can be visible in the listview control
def restoreJSON():
    for x in data:
        if x['status'] == 'D':
            x['status'] = 'U'
            logger("RESTORE,INFO", "Status marked as unreleased for ID: " + x['ID'])
    with open (filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',',': '))
    clearControls()

# logger will accept messages from the functions to write to the log file
def logger(level, message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file_object = open('logfile.log', 'a')
    file_object.write(level + ',' + dt_string + ',' + message + '\n')
    file_object.close()

# clearControls function to be called in other functions to clear out all cached data in UI.
def clearControls():
    treeReleased.delete(*treeReleased.get_children())
    lblID.config(text= 'ID: ')
    lblSummary.config(text = 'Summary: ')
    lblProduct.config(text = 'Product: ')
    lblStatus.config(text = 'Status: ')
    lblIssueType.config(text = 'Issue Type: ')
    lblUpdated.config(text = 'Last Updated: ')
    lblFile.config(text = 'File: ')
    txtSummary.delete(0, END)
    txtSummary.insert(0, '')
    txtProduct.delete(0, END)
    txtProduct.insert(0, '')
    txtStatus.delete(0, END)
    txtStatus.insert(0, '')
    txtIssueType.delete(0, END)
    txtIssueType.insert(0, '')
    txtUpdated.delete(0, END)
    txtUpdated.insert(0, '')
    txtFile.delete(0, END)
    txtFile.insert(0, '')
    loadData()

######## endfunctions #########

########## Controls ##########

# All controls in this section that make up the UI
s = ttk.Style()
s.theme_use('clam')
treeReleased = ttk.Treeview(mainForm, selectmode="browse", column=("c1", "c2"), show='headings', height=8)
treeReleased.column("# 1", anchor=CENTER, minwidth=0, width=100, stretch=NO)
treeReleased.heading("# 1", text="ID")
treeReleased.column("# 2", anchor=CENTER, minwidth=0, width=650, stretch=NO)
treeReleased.heading("# 2", text="Released Toolkits")
treeReleased.place(relx=0.03, rely=0.07)
treeReleased.bind('<ButtonRelease-1>', selectItem)
  
btnLoadData = Button(mainForm, bd=3, width=40, height=1, text="Load Toolkit Data", command = loadData)
btnLoadData.place(relx=0.03, rely=0.01)

btnWrite = Button(mainForm, bd=3, width=40, height=1, text="Write New Toolkit/s", command = writeGenericData)
btnWrite.place(relx=0.03, rely=0.4)

btnDelete = Button(mainForm, bd=3, width=40, height=1, text="Delete Toolkit/s", command = deleteJSON)
btnDelete.place(relx=0.03, rely=0.87)

btnUpdate = Button(mainForm, bd=3, width=40, height=1, text="Update Toolkit/s", command = updateJSON)
btnUpdate.place(relx=0.03, rely=0.81)

btnRestore = Button(mainForm, bd=3, width=40, height=1, text="Restore Deleted Toolkit/s", command = restoreJSON)
btnRestore.place(relx=0.03, rely=0.93)

v = StringVar(mainForm, value='0')
txtProductCnt = Entry(mainForm, width=25, text=v)
txtProductCnt.place(relx=0.03, rely=0.46)

lblID = Label(mainForm, width=15, text="ID:", anchor="w")
lblID.place(relx=0.03, rely=0.51)

lblNewVal = Label(mainForm, width=15, text="New Values:", anchor="w")
lblNewVal.place(relx=0.44, rely=0.51)

lblSummary = Label(mainForm, width=50, text="Summary:", anchor="w")
lblSummary.place(relx=0.03, rely=0.55)

txtSummary = Entry(mainForm, width=70)
txtSummary.place(relx=0.44, rely=0.55)

lblProduct = Label(mainForm, width=50, text="Product:", anchor="w")
lblProduct.place(relx=0.03, rely=0.59)

txtProduct = Entry(mainForm, width=70)
txtProduct.place(relx=0.44, rely=0.59)

lblStatus = Label(mainForm, width=50, text="Status:", anchor="w")
lblStatus.place(relx=0.03, rely=0.63)

txtStatus = Entry(mainForm, width=70)
txtStatus.place(relx=0.44, rely=0.63)

lblIssueType = Label(mainForm, width=50, text="Type:", anchor="w")
lblIssueType.place(relx=0.03, rely=0.67)

txtIssueType = Entry(mainForm, width=70)
txtIssueType.place(relx=0.44, rely=0.67)

lblUpdated = Label(mainForm, width=50, text="Last Updated:", anchor="w")
lblUpdated.place(relx=0.03, rely=0.71)

txtUpdated = Entry(mainForm, width=70)
txtUpdated.place(relx=0.44, rely=0.71)

lblFile = Label(mainForm, width=50, text="File:", anchor="w")
lblFile.place(relx=0.03, rely=0.75)

txtFile = Entry(mainForm, width=70)
txtFile.place(relx=0.44, rely=0.75)

######## endControls #########

mainForm.mainloop()