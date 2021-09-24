import tkinter
from tkinter.constants import GROOVE
import PyPDF2
import os
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilenames

program_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(program_path)
writer = PyPDF2.PdfFileWriter()

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
merged_file_name = '0.All_merged.pdf'

def merge_files():
    merged_file_name = textBox.get()
    if not (merged_file_name.endswith('.pdf')):
        merged_file_name+='.pdf'
    mergedFile = open(desktop+merged_file_name, 'wb')
    writer.write(mergedFile)
    mergedFile.close()
    merge_btn.config(state=tkinter.DISABLED)
    textBox.config(state=tkinter.DISABLED)  

def open_files():
    merge_btn['state'] == tkinter.NORMAL
    browse_text.set('Select pdf\'s..')
    file_names = askopenfilenames(parent=root, filetypes=[('Pdf file', '*.pdf')])  # returns full path of files
    for file in file_names:
        #print(file)
        if(file.endswith('.pdf')):
            pdfFile = open(file, 'rb')
            reader = PyPDF2.PdfFileReader(pdfFile)
            for pageNum in range(reader.numPages):
                page = reader.getPage(pageNum)
                writer.addPage(page)
    browse_text.set('Choose files')
    merge_btn.config(state=tkinter.NORMAL)
    textBox.config(state=tkinter.NORMAL)
    

root = tkinter.Tk()
root.geometry("450x300")
root.iconbitmap("images\PDF_merge_logo.ico")
root.resizable(height=False)

# logo
logo = Image.open('images\PDF_merge_logo2.png').resize((140,140))
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(image=logo)
logo_label.image = logo
logo_label.grid(row = 0, column = 1,pady=16)

# browse button
browse_text = tkinter.StringVar()
browse_btn = tkinter.Button(root, text="Choose files", bg='#db4b38', height=1,width=20,font='Helvetica 15 bold', command=lambda:open_files(), fg='white',relief=GROOVE)
browse_text.set('Choose files')
browse_btn.grid(row = 1, column=1,sticky=(tkinter.N,tkinter.S))

# text box for merged file name
textBox = tkinter.Entry(root, width=40)
textBox.insert(0,merged_file_name)
textBox.grid(row = 2, column=1)
textBox.config(state='disabled')

# merge button
merge_text = tkinter.StringVar()
merge_btn = tkinter.Button(root, textvariable = merge_text, bg='#db4b38', height=1,width=20, font='Helvetica 15 bold', command=lambda:merge_files() ,
                            fg='white', state=tkinter.DISABLED,relief=GROOVE)
merge_text.set('Merge')
merge_btn.grid(row = 3,column=1,sticky=(tkinter.N,tkinter.S))

root.columnconfigure(1,weight=1)


root .mainloop()
