import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from data_processor import PersonDataProcessor

processor = PersonDataProcessor()


def open_file():
    file_path = filedialog.askopenfilename(title='Ava fail', filetypes=(('JSON files', '*.json'),), initialdir=".")
    if file_path:
        processor.read_file_contents(file_path)
        if len(processor.content) > 0:
            lbl_file.config(text=os.path.basename(file_path))
            show_info()
        else:
            messagebox.showwarning(title='Hoiatus', message='See pole õige andmete fail')


def show_info():
    txt_result.delete('1.0', END)
    if len(processor.content) > 0:
        result_text = (
            f'1. Isikute arv kokku: {processor.get_total_persons()}\n'
            f'2. Kõige pikem nimi: {processor.get_longest_name()["name"]}, Tähemärkide arv: {processor.get_longest_name()["length"]}\n'
            f'3. Kõige vanem elav inimene: {processor.get_oldest_living_person()["name"]}, Vanus: {processor.get_oldest_living_person()["age"]}, {processor.get_oldest_living_person()["dateofbirth"]}-today\n'
            f'4. Kõige vanem surnud inimene: {processor.get_oldest_deceased_person()["name"]}, Vanus: {processor.get_oldest_deceased_person()["age"]}, {processor.get_oldest_deceased_person()["dateofbirth"]}-{processor.get_oldest_deceased_person()["dateofdeath"]}\n'
            f'5. Näitlejate koguarv: {processor.get_actor_count()}\n'
            f'6. Sündinud 1997 aastal: {processor.get_births_in_1997()}\n'
            f'7. Kui palju on erinevaid elukutseid: {processor.get_unique_professions()}\n'
            f'8. Nimi sisaldab rohkem kui kaks nime: {processor.get_names_with_more_than_two_parts()}\n'
            f'9. Sünniaeg ja surmaaeg on sama v.a. aasta: {processor.get_same_birth_death_month_day()}\n'
            f'10. Elavaid isikud: {processor.get_living_and_deceased_counts()["living"]}, Surnud isikud: {processor.get_living_and_deceased_counts()["deceased"]}\n'
        )
        txt_result.insert(END, result_text)

    else:
        txt_result.insert(END, 'Õiget faili pole valitud\n')


win = Tk()
win.geometry('700x400')
win.title('Eesti Kuulsused Statistika')
win.resizable(False, False)

# Frame, kuhu peale tulevad kõik vidinad (Widgets)
frame = Frame(win)
frame.pack(side=TOP, anchor=NW, padx=5, pady=5)

# Nupp (Button) faili avamiseks (rida 1)
btn_open = Button(frame, text='Ava fail', command=open_file)
btn_open.grid(row=0, column=0, sticky=EW, padx=2, pady=2)

# Silt (Label) avatud faili nime näitamiseks (rida 2)
lbl_file = Label(frame, text='Siia tuleb failinimi')
lbl_file.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Mitmerealine tekstikast (Text) tulemuste näitamiseks (rida 3)
txt_result = Text(frame, wrap=NONE, height=20, width=120)  # Adjust height and width as needed
txt_result.grid(row=2, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Lisame kerimisribad
scroll_y = Scrollbar(frame, orient="vertical", command=txt_result.yview)
scroll_y.grid(row=2, column=2, sticky='ns')
txt_result.config(yscrollcommand=scroll_y.set)

scroll_x = Scrollbar(frame, orient="horizontal", command=txt_result.xview)
scroll_x.grid(row=3, column=0, columnspan=3, sticky='ew')  # Adjusted columnspan to 3
txt_result.config(xscrollcommand=scroll_x.set)




win.mainloop()