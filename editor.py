import tkinter as tk
from tkinter import ttk
import os
from tkinter import font,messagebox,colorchooser,filedialog
from PIL import Image, ImageTk
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
root = tk.Tk()
root.geometry('1200x800')
root.wm_iconbitmap('icon.ico')
root.title("Word Editor")
main_menu = tk.Menu(root)
# ICons 
new_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/new.png")
open_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/open.png")
Save_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/save.png")
Saveas_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2\save_as.png")
exit_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/exit.png")
cut_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/cut.png")
copy_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/copy.png")
paste_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/paste.png")
find_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/find.png")
clear_all_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/clear_all.png")
toolbar_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/tool_bar.png")
statusbar_icon = tk.PhotoImage(file="D:/Coding/Word_Editor/icons2/status_bar.png")
light_theme_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\light_default.png")
Blue_theme_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\ight_blue.png")
red_theme_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\ed.png")
movokia_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\monokai.png")
dark_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\dark.png")
light_plus_icon = tk.PhotoImage(file="D:\Coding\Word_Editor\icons2\light_plus.png")
# Main menu 
file_menu = tk.Menu(main_menu,tearoff=False)
# ######################################NEW FUNCTIONSLITY#############################
url = ''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
    root.title("Untitled document")
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select a File to Open",filetypes=(('Text File','*.txt'),('PDF','*.pdf'),('All files','*.*')))
    try:
        with open(url,'r') as f:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,f.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))
def save_file(event=None):
    global url 
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('PDF','*.pdf'),('All files','*.*')))
            content1=text_editor.get(1.0,tk.END)
            url.write(content1)
            url.close()
    except:
        return 
def printing(event=None):
    printer=QPrinter(QPrinter.HighResolution)
    dialog=QPrintDialog(printer,root)
    if dialog.exec_()==QPrintDialog.Accepted:
        text_editor.print_(printer)
def save_as(event=None):
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('PDF','*.pdf'),('All files','*.*')))
        content2=text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()
    except:
        return

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed==False:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save this file ?')
            # root.protocol('WM_DELETE_WINDOW',exit_func)
            if mbox is True:
                if url:
                    content4=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as ft:
                        ft.write(content4)
                        root.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    content3=str(text_editor.get(1.0,tk.END))
                    url.write(content3)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return
            
def findfunc(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match',"1.0",tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                endpos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match',start_pos,endpos)
                matches+=1
                start_pos = endpos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content = text_editor.get(1.0,tk.END)
        newcontent=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,newcontent)
    find_dialog= tk.Toplevel()
    find_dialog.geometry("500x250+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0,0)
    # Frame
    find_frame=ttk.LabelFrame(find_dialog,text="Find/Replace")
    find_frame.pack(pady=20)
    # LAbels
    find_label=ttk.Label(find_frame,text="Find : ")
    replace_label=ttk.Label(find_frame,text="Replace : ")
    # buttons
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    # Entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    # Grid
    find_label.grid(row=0,column=0,padx=4,pady=5)
    replace_label.grid(row=1,column=0,padx=4,pady=5)
    find_input.grid(row=0,column=1,padx=4,pady=5)
    replace_input.grid(row=1,column=1,padx=4,pady=5)
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    find_dialog.mainloop()




file_menu.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
file_menu.add_separator()
file_menu.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save',image=Save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file_menu.add_command(label='Save As',image=Saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Print',compound=tk.LEFT,accelerator='Ctrl+P',command=printing)
file_menu.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)
edit_menu = tk.Menu(main_menu,tearoff=False)
edit_menu.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit_menu.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit_menu.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=findfunc)
edit_menu.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+c',command=lambda:text_editor.delete(1.0,tk.END))
view_menu = tk.Menu(main_menu,tearoff=False)
showtool=tk.BooleanVar()
showtool.set(True)

showstatus=tk.BooleanVar()
showstatus.set(True)
def hide_toolbar():
    global showtool
    if showtool:
        tool_bar.pack_forget()
        showtool = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        showtool = True
def hide_statusbar():
    global showstatus
    if showstatus:
        status_bar.pack_forget()
        showstatus=False
    else:
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        showstatus=True

view_menu.add_checkbutton(label='Tool Bar',image=toolbar_icon,compound=tk.LEFT,onvalue=True,offvalue=0,variable=showtool,activeforeground='blue',activebackground="yellow",command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar',image=statusbar_icon,compound=tk.LEFT,onvalue=True,offvalue=0,variable=showstatus,activeforeground='blue',activebackground="yellow",command=hide_statusbar)
colortheme_menu = tk.Menu(main_menu,tearoff=False)
theme_choice = tk.StringVar()
# main menu cascade with file,view,edit,theme menu-------------
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Theme',menu=colortheme_menu)
color_icons=(light_theme_icon,light_plus_icon,dark_icon,red_theme_icon,movokia_icon,Blue_theme_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

count=0
def color_changer():
    color_theme=theme_choice.get()
    color_tuple=color_dict.get(color_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(foreground=fg_color,background=bg_color)
for i in color_dict:
    colortheme_menu.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=color_changer)
    count+=1
# toolbar
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)
# Fontbox
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
# sizebox
size=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size,state='readonly')
font_size['values']=tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=1)
# bold
bold_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=1)
italic_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=1,pady=1)
underline_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/1.png")
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=1)
# font color button
font_color_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=1)
# align left
align_left_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=1)
align_center_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=1)
align_right_icon=tk.PhotoImage(file="D:/Coding/Word_editor/icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=1)
# Text editor
text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()
scroll_bar=tk.Scrollbar(root)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.pack(fill=tk.BOTH,expand=True)
text_editor.configure(font="Arial 16")
# font size and font family functionality
current_font_size =16
current_font_family = "Arial"
def change_font(root):
    global current_font_family
    global current_font_size
    current_font_family = font_family.get()
    current_font_size = size.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font)
# #### Bold button functionality or button functionality
def changebold(root):
    textproperty  = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()["weight"]== "normal":
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if textproperty.actual()["weight"]== "bold":
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
def changeitalic(root):
    textproperty  = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()["slant"]== "italic":
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
    if textproperty.actual()["slant"]== "roman":
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
def changeunderline(root):
    textproperty  = tk.font.Font(font=text_editor['font'])
    if textproperty.actual()["underline"]== 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if textproperty.actual()['underline']== 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.bind("<Button-1>",changebold)
italic_btn.bind("<Button-1>",changeitalic)
underline_btn.bind("<Button-1>",changeunderline)
# bold_btn.configure(command=changebold)
# italic_btn.configure(command=changeitalic)
# underline_btn.configure(command=changeunderline)
# ###################################################FONT COLOR FUNCTIONALITY########################################################
def font_color_changer(root):
    colorvar=tk.colorchooser.askcolor()
    text_editor.configure(fg=colorvar[1])
font_color_btn.bind("<Button-1>",font_color_changer)
# ################################################ALIGNMENT FUNCTIONALITY###################################################################
def alignleft(root):
    text_content = text_editor.get(1.0,tk.END)
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
def alignright(root):
    text_content = text_editor.get(1.0,tk.END)
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
def aligncenter(root):
    text_content = text_editor.get(1.0,tk.END)
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.bind('<Button-1>',aligncenter)
align_right_btn.bind("<Button-1>",alignright)
align_left_btn.bind("<Button-1>",alignleft)





    
    



# statusbar
status_bar = tk.Label(root,text='Status Bar',anchor='w',font='lucida 10')
status_bar.pack(side=tk.BOTTOM,fill=tk.X)
text_changed = False
def countwordchar(event=None):
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",countwordchar)
# if text_editor.edit_modified():
#     text_changed = True
# print(text_changed)
# print(text_editor.edit_modified())
# INSEERT meNU
def imagefunc(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select a Image to Open",filetypes=(('JPEG','*.jpeg'),('Image File','*.png'),('JPG','*.jpg'),('All files','*.*')))
    try:
        image1=Image.open(url)
        photo=ImageTk.PhotoImage(image1)
        image_label=tk.Frame(text_editor,image=photo)
        # image_label=tk.Label(text_editor,image=photo)
        text_editor.config(image=photo)

        # text_editor.image_create('insert',image=)
    except FileNotFoundError:
        return
    except:
        return
    

insert_menu=tk.Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Insert",menu=insert_menu)
insert_menu.add_command(label="Table",compound=tk.LEFT)
insert_menu.add_command(label="Images",compound=tk.LEFT,command=imagefunc)
root.config(menu=main_menu)
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Alt-s>",save_as)
root.bind("<Control-q>",exit_func)
root.bind("<Control-f>",findfunc)
root.protocol('WM_DELETE_WINDOW',exit_func)
root.mainloop()