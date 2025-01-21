from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from queue_functions import HospitalQueue

colors = {
    'navy': '#1B2838',
    'light_blue': '#3498db',
    'white': '#FFFFFF',
    'grey': '#95a5a6',
    'dark_grey': '#2C3E50',
    'black': '#000000'
}

win = Tk()
queue = HospitalQueue()
win.title("Grey Sloan Memorial Hospital")
win.geometry("1200x860+320+80")
win.maxsize(1200, 860)
win.configure(bg=colors['navy'])

def content_frames():
    global login_frame, menu_div, logo_label, add_patient_frame, view_queue_frame
    global admit_patient_frame, search_patient_frame, update_patient_frame, delete_patient_frame

    login_frame = Frame(main_div, bg=colors['navy'], padx=40, pady=20)
    setup_login_frame()
    
    menu_div = Frame(main_div, bg=colors['dark_grey'], padx=20, pady=20)
    logo_label = Label(menu_div, text="GREY SLOAN\nMEMORIAL", font=('Helvetica', 16, 'bold'), bg=colors['dark_grey'], fg=colors['white'], pady=20)
    
    add_patient_frame = Frame(main_div, bg="#2E2E2E")
    setup_add_patient_frame()

    view_queue_frame = Frame(main_div, bg="#2E2E2E")
    setup_view_queue_frame()

    admit_patient_frame = Frame(main_div, bg="#2E2E2E")
    setup_admit_patient_frame()

    search_patient_frame = Frame(main_div, bg="#2E2E2E")
    setup_search_patient_frame()

    update_patient_frame = Frame(main_div, bg="#2E2E2E")
    setup_update_patient_frame()

    delete_patient_frame = Frame(main_div, bg="#2E2E2E")
    setup_delete_patient_frame()

def setup_login_frame():
    global staff_id_var
    container = Frame(login_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    Label(container, text="🏥", font=('Helvetica', 64), bg=colors['navy'], fg=colors['light_blue']).pack(pady=(20,0))
    Label(container, text="GREY SLOAN\nMEMORIAL HOSPITAL", font=('Helvetica', 24, 'bold'), bg=colors['navy'], fg=colors['white']).pack(pady=(0,10))
    Label(container, text="Staff Login Portal", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack(pady=(0,40))
    
    form_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=30)
    form_frame.pack(fill="x")
    Label(form_frame,text="👤 Staff ID", font=('Helvetica', 12, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")
    
    staff_id_var = Entry(form_frame, font=('Helvetica', 12), bg=colors['navy'], fg=colors['white'], insertbackground=colors['white'], relief=FLAT, bd=10)
    staff_id_var.pack(fill="x", pady=(5,20))
    button_frame = Frame(form_frame, bg=colors['dark_grey'])
    button_frame.pack(fill="x", pady=(10,0))
    Button(button_frame,text="🚪 LOGIN", command=login, bg=colors['light_blue'], fg=colors['white'], font=('Helvetica', 12, 'bold'), pady=12, relief=FLAT, cursor="hand2").pack(fill="x", pady=(0,10))
    Button(button_frame, text="❌ EXIT", command=exit_application, bg='#e74c3c', fg=colors['white'], font=('Helvetica', 12, 'bold'), pady=12, relief=FLAT, cursor="hand2").pack(fill="x")

def login():
    staff_id = staff_id_var.get()
    
    if staff_id == "12345":
        login_frame.pack_forget()
        
        menu_div.pack(side="left", fill='y')
        logo_label.pack()
        create_menu_buttons()
        show_add_patient_page()
    else:
        messagebox.showerror("Login Failed", 
                           "Invalid Staff ID.\nPlease try again.")

def show_login_page():
    clear_frames()
    login_frame.pack(fill="both", expand=True)

def clear_frames():
    frames = [login_frame, add_patient_frame, view_queue_frame, admit_patient_frame, search_patient_frame, update_patient_frame, delete_patient_frame ]
    for frame in frames:
        frame.pack_forget()

def setup_add_patient_frame():
    global add_patient_vars
    container = Frame(add_patient_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    
    header_frame = Frame(container, bg=colors['navy'])
    header_frame.pack(fill="x", pady=(0,30))
    Label(header_frame, text="🚨 EMERGENCY ADMISSION", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg=colors['light_blue']).pack()
    Label(header_frame, text="Grey Sloan Memorial Hospital", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack()

    form_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=20)
    form_frame.pack(fill="x", padx=20)
    entries = [('👤 Patient Name:', 'name'), ('🆔 Chief Complaint:', 'symptoms'), ('⚡ Severity Level (1-10):', 'severity')]
    add_patient_vars = {}

    for label_text, var_name in entries:
        entry_container = Frame(form_frame, bg=colors['dark_grey'])
        entry_container.pack(pady=12, fill="x")
        Label(entry_container, text=label_text, font=('Helvetica', 12, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")
        entry = Entry(entry_container, font=('Helvetica', 12), bg=colors['navy'], fg=colors['white'], insertbackground=colors['white'], relief=FLAT, bd=10)
        entry.pack(fill="x", pady=(5,0))
        add_patient_vars[var_name] = entry

    button_frame = Frame(container, bg=colors['navy'], pady=20)
    button_frame.pack(fill="x")
    Button(button_frame, text="ADMIT PATIENT", command=add_patient, bg=colors['light_blue'], fg=colors['white'], font=('Helvetica', 13, 'bold'), pady=12, padx=30, relief=FLAT, cursor="hand2").pack(side=LEFT, padx=5)
    Button(button_frame, text="CLEAR FORM", command=lambda: [entry.delete(0, END) for entry in add_patient_vars.values()], bg=colors['dark_grey'], fg=colors['white'], font=('Helvetica', 13), pady=12, padx=30, relief=FLAT, cursor="hand2").pack(side=LEFT, padx=5)

def setup_view_queue_frame():
    global queue_tree, stats_labels
    container = Frame(view_queue_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    Label(container, text="🚑 EMERGENCY DEPARTMENT", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg=colors['light_blue']).pack()
    Label(container, text="Current Patient Queue", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack(pady=(0,20))

    stats_frame = Frame(container, bg=colors['dark_grey'])
    stats_frame.pack(fill="x", pady=20)
    stats_labels = {}
    for stat in ['Total Patients', 'Critical (7-10)', 'Moderate (4-6)', 'Minor (1-3)']:
        stat_container = Frame(stats_frame, bg=colors['dark_grey'], padx=20, pady=10)
        stat_container.pack(side=LEFT, expand=True)
        Label(stat_container, text=stat, font=('Helvetica', 10), bg=colors['dark_grey'], fg=colors['grey']).pack()
        stats_labels[stat] = Label(stat_container, text="0", font=('Helvetica', 20, 'bold'), bg=colors['dark_grey'], fg=colors['white'])
        stats_labels[stat].pack()

    style = ttk.Style()
    style.configure("Custom.Treeview", background=colors['light_blue'], foreground=colors['white'],fieldbackground=colors['light_blue'], rowheight=40)
    style.configure("Custom.Treeview.Heading", background=colors['light_blue'], foreground=colors['black'], relief="flat", padding=10)

    queue_tree = ttk.Treeview(container, style="Custom.Treeview", columns=('ID', 'Name', 'Symptoms', 'Severity', 'Wait Time'), show='headings', height=10)
    column_configs = [('ID', 100), ('Name', 200), ('Symptoms', 300), ('Severity', 100), ('Wait Time', 150)]

    for col, width in column_configs:
        queue_tree.heading(col, text=col)
        queue_tree.column(col, width=width, anchor='center')
    queue_tree.pack(pady=20, fill="both")

    button_frame = Frame(container, bg=colors['navy'], pady=20)
    button_frame.pack(fill="x", expand=True)
    buttons = [("🚨 ADMIT NEXT PATIENT", admit_patient, colors['light_blue']),("🔄 REFRESH QUEUE", refresh_queue, colors['dark_grey'])]

    for text, command, color in buttons:
        Button(button_frame, text=text, command=command, bg=color, fg=colors['white'], font=('Helvetica', 11, 'bold'), pady=12, padx=20, relief=FLAT, cursor="hand2").pack(side=LEFT, padx=5, expand=True)

def setup_admit_patient_frame():
    global admitted_tree, admitted_count
    container = Frame(admit_patient_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    
    header_frame = Frame(container, bg=colors['navy'])
    header_frame.pack(fill="x", pady=(0,30))
    Label(header_frame, text="🏥 ADMITTED PATIENTS", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg=colors['light_blue']).pack()
    
    admitted_count = Label(header_frame, text="Currently Admitted: 0", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey'])
    admitted_count.pack()
    admitted_tree = ttk.Treeview(container, style="Custom.Treeview", columns=('ID', 'Name', 'Symptoms', 'Severity', 'Admission Time'), show='headings', height=12)
    for col, width in [('ID', 100), ('Name', 200), ('Symptoms', 300), ('Severity', 100), ('Admission Time', 150)]:
        admitted_tree.heading(col, text=col)
        admitted_tree.column(col, width=width)
    admitted_tree.pack(pady=20, fill="both")

    button_frame = Frame(container, bg=colors['navy'], pady=20)
    button_frame.pack(fill="x", expand=True)
    buttons = [("🗑️ DISCHARGE PATIENT", delete_admitted_patient, colors['light_blue']), ("🔄 REFRESH LIST", refresh_admitted_patients, colors['dark_grey'])]
    for text, command, color in buttons:
        Button(button_frame, text=text, command=command, bg=color, fg=colors['white'], font=('Helvetica', 11, 'bold'), pady=12, padx=20, relief=FLAT, cursor="hand2").pack(side=LEFT, padx=5, expand=True)

def setup_search_patient_frame():
    global search_id_var, search_result_label
    container = Frame(search_patient_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    Label(container, text="🔍 PATIENT LOOKUP", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg=colors['light_blue']).pack()
    Label(container, text="Search Patient Records", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack(pady=(0,30))

    search_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=20)
    search_frame.pack(fill="x", padx=20)
    Label(search_frame, text="🆔 Patient ID:", font=('Helvetica', 12, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")
    search_id_var = Entry(search_frame, font=('Helvetica', 12), bg=colors['navy'], fg=colors['white'], insertbackground=colors['white'], relief=FLAT, bd=10)
    search_id_var.pack(fill="x", pady=(5,15))
    Button(search_frame, text="🔍 SEARCH RECORDS", command=search_patient, bg=colors['light_blue'], fg=colors['white'], font=('Helvetica', 12, 'bold'), pady=12, padx=30, relief=FLAT, cursor="hand2").pack()

    result_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=20)
    result_frame.pack(fill="x", padx=20, pady=20)
    Label(result_frame, text="Patient Information", font=('Helvetica', 14, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")

    search_result_label = Label(result_frame, text="No patient selected", font=('Helvetica', 12), bg=colors['dark_grey'], fg=colors['grey'], justify=LEFT, pady=15)
    search_result_label.pack(anchor="w")

def setup_update_patient_frame():
    global update_patient_vars
    container = Frame(update_patient_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    Label(container, text="✏️ UPDATE PATIENT", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg=colors['light_blue']).pack()
    Label(container, text="Modify Patient Information", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack(pady=(0,30))

    form_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=20)
    form_frame.pack(fill="x", padx=20)
    entries = [('🆔 Patient ID:', 'id'),('🏥 Updated Symptoms:', 'symptoms'),('⚡ New Severity Level (1-10):', 'severity')]
    update_patient_vars = {}

    for label_text, var_name in entries:
        entry_container = Frame(form_frame, bg=colors['dark_grey'])
        entry_container.pack(pady=12, fill="x")
        Label(entry_container, text=label_text, font=('Helvetica', 12, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")
        entry = Entry(entry_container, font=('Helvetica', 12), bg=colors['navy'], fg=colors['white'], insertbackground=colors['white'], relief=FLAT, bd=10)
        entry.pack(fill="x", pady=(5,0))
        update_patient_vars[var_name] = entry

    button_frame = Frame(container, bg=colors['navy'], pady=20)
    button_frame.pack(fill="x")
    buttons = [("💾 UPDATE RECORD", update_patient, colors['light_blue']), ("🔄 CLEAR FORM", lambda: [entry.delete(0, END) for entry in update_patient_vars.values()], colors['dark_grey'])]
    for text, command, color in buttons:
        Button(button_frame, text=text, command=command, bg=color, fg=colors['white'], font=('Helvetica', 11, 'bold'), pady=12, padx=20, relief=FLAT, cursor="hand2").pack(side=LEFT, padx=5)

def setup_delete_patient_frame():
    global delete_id_var, confirm_var
    container = Frame(delete_patient_frame, bg=colors['navy'], padx=40, pady=20)
    container.pack(fill="both", expand=True)
    Label(container, text="⚠️", font=('Helvetica', 48), bg=colors['navy'], fg='#e74c3c').pack()
    Label(container, text="DELETE PATIENT RECORD", font=('Helvetica', 28, 'bold'), bg=colors['navy'], fg='#e74c3c').pack()
    Label(container, text="This action cannot be undone", font=('Helvetica', 14), bg=colors['navy'], fg=colors['grey']).pack(pady=(0,30))

    form_frame = Frame(container, bg=colors['dark_grey'], padx=30, pady=20)
    form_frame.pack(fill="x", padx=20)
    Label(form_frame, text="🆔 Patient ID to Delete:", font=('Helvetica', 12, 'bold'), bg=colors['dark_grey'], fg=colors['white']).pack(anchor="w")

    delete_id_var = Entry(form_frame, font=('Helvetica', 12), bg=colors['navy'], fg=colors['white'], insertbackground=colors['white'], relief=FLAT, bd=10)
    delete_id_var.pack(fill="x", pady=(5,15))

    confirm_var = BooleanVar()
    Checkbutton(form_frame, text="I confirm that I want to delete this patient record", variable=confirm_var, font=('Helvetica', 11), bg=colors['dark_grey'], fg=colors['white'], selectcolor=colors['navy'], activebackground=colors['dark_grey'], activeforeground=colors['white']).pack(pady=10)
    Button(form_frame, text="🗑️ DELETE PATIENT RECORD", command=confirm_delete_patient, bg='#e74c3c', fg=colors['white'], font=('Helvetica', 12, 'bold'), pady=12, padx=30, relief=FLAT, cursor="hand2").pack(pady=10)

def add_patient():
    name = add_patient_vars['name'].get()
    symptoms = add_patient_vars['symptoms'].get()
    try:
        severity = int(add_patient_vars['severity'].get())
        if not 1 <= severity <= 10:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Severity must be a number between 1 and 10.")
        return

    if not name or not symptoms:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    result = queue.add_patient(name, symptoms, severity)
    messagebox.showinfo("Add Patient", result)

    for entry in add_patient_vars.values():
        entry.delete(0, END)

def admit_patient():
    result = queue.admit_patient()
    messagebox.showinfo("Admit Patient", result)
    refresh_queue()
    refresh_admitted_patients()

def delete_patient():
    id = delete_id_var.get()
    if not id:
        messagebox.showerror("Input Error", "Patient ID is required.")
        return
    result = queue.delete_patient(id)
    messagebox.showinfo("Delete Patient", result)
    refresh_queue()

def delete_admitted_patient():
    selected_item = admitted_tree.selection()
    if not selected_item:
        messagebox.showwarning("Delete Patient", "No patient selected.")
        return
    id = admitted_tree.item(selected_item, 'values')[0]
    result = queue.delete_admitted_patient(id)
    messagebox.showinfo("Delete Admitted Patient", result)
    refresh_admitted_patients()

def search_patient():
    id = search_id_var.get()
    if not id:
        messagebox.showerror("Input Error", "Patient ID is required.")
        return
    patient = queue.search_patient(id)
    if patient:
        search_result_label.config(
            text=f"Patient: {patient.name}\nSymptoms: {patient.symptoms}\nSeverity: {patient.severity}")
    else:
        search_result_label.config(text="Patient not found.")

def update_patient():
    id = update_patient_vars['id'].get()
    symptoms = update_patient_vars['symptoms'].get()
    try:
        severity = int(update_patient_vars['severity'].get())
        if severity < 1 or severity > 10:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Severity must be a number between 1 and 10.")
        return

    if not id or not symptoms:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    result = queue.update_patient(id, symptoms, severity)
    messagebox.showinfo("Update Patient", result)
    refresh_queue()

def refresh_queue():
    patients = queue.get_queue()
    stats = {'Total Patients': len(patients), 'Critical (7-10)': sum(1 for p in patients if p.severity >= 7), 'Moderate (4-6)': sum(1 for p in patients if 4 <= p.severity <= 6), 'Minor (1-3)': sum(1 for p in patients if p.severity <= 3)}
    
    for label, count in stats.items():
        stats_labels[label].config(text=str(count))
    queue_tree.delete(*queue_tree.get_children())
    
    for patient in patients:
        wait_time = datetime.now() - patient.timestamp
        wait_str = f"{wait_time.seconds // 3600}h {(wait_time.seconds % 3600) // 60}m"
        queue_tree.insert('', 'end', values=(
            patient.id, patient.name, patient.symptoms, 
            patient.severity, wait_str
        ))

def refresh_admitted_patients():
    admitted_tree.delete(*admitted_tree.get_children())
    
    for patient in queue.admitted_patients:
        admitted_tree.insert('', 'end', values=(
            patient.id, patient.name, patient.symptoms,
            patient.severity, patient.timestamp.strftime("%H:%M")
        ))
    
    admitted_count.config(
        text=f"Currently Admitted: {len(queue.admitted_patients)}"
    )

def confirm_delete_patient():
    if not confirm_var.get():
        messagebox.showwarning("Delete Patient", "Please confirm the deletion by checking the confirmation box.")
        return
    
    if not delete_id_var.get():
        messagebox.showerror("Delete Patient", "Patient ID is required.")
        return
    
    result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this patient record?\n\n" + "This action cannot be undone.")
    if result:
        delete_patient()
        delete_id_var.delete(0, END)
        confirm_var.set(False)

def show_add_patient_page():
    clear_frames()
    add_patient_frame.pack(fill="both", expand=True)

def show_view_queue_page():
    clear_frames()
    view_queue_frame.pack(fill="both", expand=True)
    refresh_queue()

def show_admit_patient_page():
    clear_frames()
    admit_patient_frame.pack(fill="both", expand=True)
    refresh_admitted_patients()

def show_search_patient_page():
    clear_frames()
    search_patient_frame.pack(fill="both", expand=True)

def show_update_patient_page():
    clear_frames()
    update_patient_frame.pack(fill="both", expand=True)

def show_delete_patient_page():
    clear_frames()
    delete_patient_frame.pack(fill="both", expand=True)

def create_menu_buttons():
    buttons = [
        ("🏥 New Patient", show_add_patient_page),
        ("👥 View Queue", show_view_queue_page),
        ("🚪 Admit Patient", show_admit_patient_page),
        ("🔍 Search Patient", show_search_patient_page),
        ("✏️ Update Patient", show_update_patient_page),
        ("❌ Delete Patient", show_delete_patient_page),
        ("🚪 Logout", logout)
    ]

    for text, command in buttons:
        button_frame = Frame(menu_div, bg=colors['dark_grey'])
        button_frame.pack(fill="x", pady=5, padx=5)
        Button(button_frame, text=text, command=command, width=20, font=("Helvetica", 11), pady=10, bg=colors['light_blue'], fg=colors['white'], activebackground=colors['grey'], activeforeground=colors['white'], relief=FLAT, cursor="hand2").pack(expand=True)

def logout():
    result = messagebox.askquestion("Logout", "Are you sure you want to logout?", icon='warning')
    if result == 'yes':
        staff_id_var.delete(0, END)
        clear_frames()
        menu_div.pack_forget()
        show_login_page()

def exit_application():
    result = messagebox.askquestion("Exit", "Are you sure you want to exit the application?", icon='warning')
    if result == 'yes':
        win.destroy()

main_div = Frame(win, bg=colors['navy'])
main_div.pack(side="left", fill="both", expand=True)

content_frames()
show_login_page()

win.mainloop()