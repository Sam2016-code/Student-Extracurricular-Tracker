import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# ============================================================
# STUDENT EXTRACURRICULAR ACTIVITY TRACKER
# Basic Python + Tkinter + JSON
# ============================================================

STUDENT_FILE = "students.json"
ACTIVITY_FILE = "activities.json"

students = []
activities = []

current_student = None


# ============================================================
# COLORS
# ============================================================

BG_COLOR = "#F4F7FB"
SIDEBAR_COLOR = "#1E293B"
PRIMARY_COLOR = "#2563EB"
PRIMARY_DARK = "#1D4ED8"
WHITE = "#FFFFFF"
TEXT_COLOR = "#1E293B"
GRAY = "#64748B"
LIGHT_BLUE = "#DBEAFE"
LIGHT_GREEN = "#DCFCE7"
GREEN = "#16A34A"
LIGHT_ORANGE = "#FFEDD5"
ORANGE = "#EA580C"
LIGHT_RED = "#FEE2E2"
RED = "#DC2626"
BORDER_COLOR = "#E2E8F0"


# ============================================================
# LOAD DATA
# ============================================================

def load_data():

    global students
    global activities

    try:
        with open(STUDENT_FILE, "r") as file:
            students = json.load(file)
    except:
        students = []

    try:
        with open(ACTIVITY_FILE, "r") as file:
            activities = json.load(file)
    except:
        activities = []


# ============================================================
# SAVE DATA
# ============================================================

def save_data():

    with open(STUDENT_FILE, "w") as file:
        json.dump(students, file, indent=4)

    with open(ACTIVITY_FILE, "w") as file:
        json.dump(activities, file, indent=4)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Student Extracurricular Activity Tracker")

root.geometry("1200x720")

root.minsize(1000, 650)

root.configure(bg=BG_COLOR)


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


def create_button(parent, text, command, width=20):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        font=("Segoe UI", 10, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE,
        activebackground=PRIMARY_DARK,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=10,
        pady=8
    )

    return button


def create_entry(parent, width=35):

    entry = tk.Entry(
        parent,
        width=width,
        font=("Segoe UI", 10),
        relief="solid",
        bd=1
    )

    return entry


def create_label(parent, text, size=10, bold=False):

    font_style = "bold" if bold else "normal"

    label = tk.Label(
        parent,
        text=text,
        font=("Segoe UI", size, font_style),
        bg=parent.cget("bg"),
        fg=TEXT_COLOR
    )

    return label


def create_card(parent, title, value, bg_color):

    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    card.pack_propagate(False)

    color_box = tk.Frame(
        card,
        bg=bg_color,
        width=8
    )

    color_box.pack(
        side="left",
        fill="y"
    )

    content = tk.Frame(
        card,
        bg=WHITE
    )

    content.pack(
        side="left",
        fill="both",
        expand=True,
        padx=15,
        pady=12
    )

    tk.Label(
        content,
        text=title,
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY
    ).pack(anchor="w")

    tk.Label(
        content,
        text=str(value),
        font=("Segoe UI", 22, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(anchor="w")

    return card


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    clear_window()

    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    # Top area

    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=180
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)


    tk.Label(
        header,
        text="STUDENT EXTRACURRICULAR",
        font=("Segoe UI", 27, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=(35, 0))


    tk.Label(
        header,
        text="ACTIVITY TRACKER",
        font=("Segoe UI", 27, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack()


    tk.Label(
        header,
        text="Track • Manage • Monitor Student Activities",
        font=("Segoe UI", 11),
        bg=PRIMARY_COLOR,
        fg="#DBEAFE"
    ).pack(pady=5)


    # Main cards

    cards_frame = tk.Frame(
        main,
        bg=BG_COLOR
    )

    cards_frame.pack(
        expand=True,
        pady=40
    )


    student_card = tk.Frame(
        cards_frame,
        bg=WHITE,
        width=280,
        height=250,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    student_card.grid(
        row=0,
        column=0,
        padx=20
    )

    student_card.pack_propagate(False)


    tk.Label(
        student_card,
        text="👨‍🎓",
        font=("Segoe UI Emoji", 38),
        bg=WHITE
    ).pack(pady=(25, 5))


    tk.Label(
        student_card,
        text="STUDENT",
        font=("Segoe UI", 18, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack()


    tk.Label(
        student_card,
        text="Register, login and manage\n"
             "your extracurricular activities.",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY,
        justify="center"
    ).pack(pady=10)


    create_button(
        student_card,
        "Student Login",
        student_login,
        20
    ).pack(pady=10)


    mentor_card = tk.Frame(
        cards_frame,
        bg=WHITE,
        width=280,
        height=250,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    mentor_card.grid(
        row=0,
        column=1,
        padx=20
    )

    mentor_card.pack_propagate(False)


    tk.Label(
        mentor_card,
        text="👨‍🏫",
        font=("Segoe UI Emoji", 38),
        bg=WHITE
    ).pack(pady=(25, 5))


    tk.Label(
        mentor_card,
        text="MENTOR",
        font=("Segoe UI", 18, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack()


    tk.Label(
        mentor_card,
        text="View students, activities\n"
             "and overall progress.",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY,
        justify="center"
    ).pack(pady=10)


    create_button(
        mentor_card,
        "Mentor Login",
        mentor_login,
        20
    ).pack(pady=10)


    bottom = tk.Frame(
        main,
        bg=BG_COLOR
    )

    bottom.pack(
        fill="x",
        pady=15
    )


    tk.Button(
        bottom,
        text="Exit Application",
        command=root.destroy,
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=RED,
        relief="flat",
        cursor="hand2"
    ).pack()


# ============================================================
# STUDENT REGISTRATION
# ============================================================

def student_registration():

    clear_window()

    container = tk.Frame(
        root,
        bg=BG_COLOR
    )

    container.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        container,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Create Student Account",
        font=("Segoe UI", 22, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=28)


    form = tk.Frame(
        container,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    form.pack(
        pady=35,
        padx=100
    )


    fields = [
        ("Student ID", False),
        ("Full Name", False),
        ("Department", False),
        ("Year", False),
        ("Email", False),
        ("Phone", False),
        ("Password", True)
    ]


    entries = {}


    for row, (label_text, is_password) in enumerate(fields):

        tk.Label(
            form,
            text=label_text,
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=TEXT_COLOR
        ).grid(
            row=row,
            column=0,
            padx=20,
            pady=10,
            sticky="w"
        )


        entry = create_entry(form, 35)

        if is_password:
            entry.config(show="*")

        entry.grid(
            row=row,
            column=1,
            padx=20,
            pady=10
        )

        entries[label_text] = entry


    def register():

        student_id = entries["Student ID"].get().strip()
        name = entries["Full Name"].get().strip()
        department = entries["Department"].get().strip()
        year = entries["Year"].get().strip()
        email = entries["Email"].get().strip()
        phone = entries["Phone"].get().strip()
        password = entries["Password"].get().strip()


        if (
            student_id == ""
            or name == ""
            or department == ""
            or year == ""
            or email == ""
            or phone == ""
            or password == ""
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return


        for student in students:

            if student["id"] == student_id:

                messagebox.showerror(
                    "Registration Error",
                    "This Student ID already exists."
                )

                return


        new_student = {

            "id": student_id,
            "name": name,
            "department": department,
            "year": year,
            "email": email,
            "phone": phone,
            "password": password

        }


        students.append(new_student)

        save_data()


        messagebox.showinfo(
            "Registration Successful",
            "Student account created successfully!"
        )


        home_page()


    button_frame = tk.Frame(
        container,
        bg=BG_COLOR
    )

    button_frame.pack()


    create_button(
        button_frame,
        "Create Account",
        register,
        20
    ).grid(
        row=0,
        column=0,
        padx=10
    )


    tk.Button(
        button_frame,
        text="Back",
        command=home_page,
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        width=18,
        pady=8,
        cursor="hand2"
    ).grid(
        row=0,
        column=1,
        padx=10
    )


# ============================================================
# STUDENT LOGIN
# ============================================================

def student_login():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    left = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        width=450
    )

    left.pack(
        side="left",
        fill="y"
    )

    left.pack_propagate(False)


    tk.Label(
        left,
        text="👨‍🎓",
        font=("Segoe UI Emoji", 55),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=(150, 10))


    tk.Label(
        left,
        text="Student Portal",
        font=("Segoe UI", 25, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack()


    tk.Label(
        left,
        text="Manage your extracurricular\n"
             "activities and track your progress.",
        font=("Segoe UI", 11),
        bg=PRIMARY_COLOR,
        fg="#DBEAFE",
        justify="center"
    ).pack(pady=15)


    right = tk.Frame(
        main,
        bg=WHITE
    )

    right.pack(
        side="left",
        fill="both",
        expand=True
    )


    tk.Label(
        right,
        text="Welcome Back",
        font=("Segoe UI", 24, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(pady=(150, 10))


    tk.Label(
        right,
        text="Login to continue",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY
    ).pack(pady=(0, 25))


    form = tk.Frame(
        right,
        bg=WHITE
    )

    form.pack()


    tk.Label(
        form,
        text="Student ID",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=8
    )


    id_entry = create_entry(form, 32)

    id_entry.grid(
        row=1,
        column=0,
        pady=(0, 15)
    )


    tk.Label(
        form,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=8
    )


    password_entry = create_entry(form, 32)

    password_entry.config(show="*")

    password_entry.grid(
        row=3,
        column=0,
        pady=(0, 20)
    )


    def login():

        student_id = id_entry.get().strip()
        password = password_entry.get().strip()


        for student in students:

            if (
                student["id"] == student_id
                and student["password"] == password
            ):

                global current_student

                current_student = student

                student_dashboard(student)

                return


        messagebox.showerror(
            "Login Failed",
            "Incorrect Student ID or Password."
        )


    create_button(
        right,
        "Login",
        login,
        25
    ).pack(pady=10)


    tk.Button(
        right,
        text="Create New Account",
        command=student_registration,
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=PRIMARY_COLOR,
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)


    tk.Button(
        right,
        text="← Back to Home",
        command=home_page,
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY,
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)


# ============================================================
# STUDENT DASHBOARD
# ============================================================

def student_dashboard(student):

    clear_window()


    sidebar = tk.Frame(
        root,
        bg=SIDEBAR_COLOR,
        width=240
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)


    tk.Label(
        sidebar,
        text="STUDENT",
        font=("Segoe UI", 20, "bold"),
        bg=SIDEBAR_COLOR,
        fg=WHITE
    ).pack(pady=(35, 0))


    tk.Label(
        sidebar,
        text="ACTIVITY TRACKER",
        font=("Segoe UI", 9),
        bg=SIDEBAR_COLOR,
        fg="#94A3B8"
    ).pack(pady=(0, 30))


    tk.Label(
        sidebar,
        text="👤 " + student["name"],
        font=("Segoe UI", 11, "bold"),
        bg=SIDEBAR_COLOR,
        fg=WHITE,
        wraplength=190
    ).pack(pady=10)


    def side_button(text, command):

        button = tk.Button(
            sidebar,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            bg=SIDEBAR_COLOR,
            fg="#CBD5E1",
            activebackground="#334155",
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            pady=10,
            cursor="hand2"
        )

        button.pack(
            fill="x"
        )


    side_button(
        "▣   Dashboard",
        lambda: student_dashboard(student)
    )

    side_button(
        "👤   My Profile",
        lambda: student_profile(student)
    )

    side_button(
        "＋   Add Activity",
        lambda: add_activity(student)
    )

    side_button(
        "☷   My Activities",
        lambda: view_my_activities(student)
    )

    side_button(
        "↻   Update Activity",
        lambda: update_activity(student)
    )

    side_button(
        "✕   Delete Activity",
        lambda: delete_activity(student)
    )

    side_button(
        "★   My Progress",
        lambda: student_progress(student)
    )


    tk.Button(
        sidebar,
        text="Logout",
        command=home_page,
        font=("Segoe UI", 10, "bold"),
        bg="#334155",
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        pady=10
    ).pack(
        side="bottom",
        fill="x",
        padx=20,
        pady=25
    )


    # Main content

    content = tk.Frame(
        root,
        bg=BG_COLOR
    )

    content.pack(
        side="left",
        fill="both",
        expand=True
    )


    # Header

    header = tk.Frame(
        content,
        bg=WHITE,
        height=80
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)


    tk.Label(
        header,
        text="Dashboard",
        font=("Segoe UI", 22, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        side="left",
        padx=30,
        pady=25
    )


    tk.Label(
        header,
        text="Student Portal",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY
    ).pack(
        side="right",
        padx=30
    )


    body = tk.Frame(
        content,
        bg=BG_COLOR
    )

    body.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )


    tk.Label(
        body,
        text="Welcome, " + student["name"] + " 👋",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(anchor="w")


    tk.Label(
        body,
        text="Here is your extracurricular activity overview.",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=GRAY
    ).pack(anchor="w", pady=(3, 20))


    # Calculate statistics

    my_activities = []

    for activity in activities:

        if activity["student_id"] == student["id"]:

            my_activities.append(activity)


    total = len(my_activities)

    completed = 0
    ongoing = 0
    certificates = 0


    for activity in my_activities:

        if activity["status"] == "Completed":
            completed += 1

        if activity["status"] == "Ongoing":
            ongoing += 1

        if activity["certificate"] == "Yes":
            certificates += 1


    # Cards

    cards = tk.Frame(
        body,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        pady=5
    )


    for i in range(4):

        cards.columnconfigure(
            i,
            weight=1
        )


    create_card(
        cards,
        "Total Activities",
        total,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=0,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Completed",
        completed,
        GREEN
    ).grid(
        row=0,
        column=1,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Ongoing",
        ongoing,
        ORANGE
    ).grid(
        row=0,
        column=2,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Certificates",
        certificates,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=3,
        padx=7,
        sticky="nsew"
    )


    # Recent activities

    recent_frame = tk.Frame(
        body,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    recent_frame.pack(
        fill="both",
        expand=True,
        pady=25
    )


    tk.Label(
        recent_frame,
        text="Recent Activities",
        font=("Segoe UI", 14, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )


    if len(my_activities) == 0:

        tk.Label(
            recent_frame,
            text="No activities added yet.\n"
                 "Click 'Add Activity' to add your first activity.",
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=GRAY,
            justify="center"
        ).pack(
            expand=True
        )

    else:

        recent = my_activities[-5:]


        for activity in reversed(recent):

            row = tk.Frame(
                recent_frame,
                bg=WHITE
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )


            tk.Label(
                row,
                text=activity["name"],
                font=("Segoe UI", 10, "bold"),
                bg=WHITE,
                fg=TEXT_COLOR,
                width=28,
                anchor="w"
            ).pack(
                side="left"
            )


            tk.Label(
                row,
                text=activity["type"],
                font=("Segoe UI", 9),
                bg=WHITE,
                fg=GRAY,
                width=20,
                anchor="w"
            ).pack(
                side="left"
            )


            status_color = GREEN

            if activity["status"] == "Ongoing":
                status_color = ORANGE

            tk.Label(
                row,
                text=activity["status"],
                font=("Segoe UI", 9, "bold"),
                bg=WHITE,
                fg=status_color,
                width=15
            ).pack(
                side="left"
            )


# ============================================================
# STUDENT PROFILE
# ============================================================

def student_profile(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=100
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="My Profile",
        font=("Segoe UI", 24, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(
        side="left",
        padx=35,
        pady=30
    )


    card = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    card.pack(
        padx=100,
        pady=40,
        fill="x"
    )


    information = [

        ("Student ID", student["id"]),
        ("Full Name", student["name"]),
        ("Department", student["department"]),
        ("Year", student["year"]),
        ("Email", student["email"]),
        ("Phone", student["phone"])

    ]


    for row, (label_text, value) in enumerate(information):

        tk.Label(
            card,
            text=label_text,
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=GRAY
        ).grid(
            row=row,
            column=0,
            padx=30,
            pady=12,
            sticky="w"
        )


        tk.Label(
            card,
            text=value,
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=TEXT_COLOR
        ).grid(
            row=row,
            column=1,
            padx=30,
            pady=12,
            sticky="w"
        )


    create_button(
        main,
        "Back to Dashboard",
        lambda: student_dashboard(student),
        22
    ).pack()


# ============================================================
# ADD ACTIVITY
# ============================================================

def add_activity(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Add New Activity",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=27)


    form = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    form.pack(
        padx=120,
        pady=25,
        fill="x"
    )


    # Activity Type

    tk.Label(
        form,
        text="Activity Type *",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=0,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    type_box = ttk.Combobox(
        form,
        width=37,
        values=[
            "Course",
            "Workshop",
            "Hackathon",
            "Competition",
            "Internship",
            "Seminar",
            "Event",
            "Sports",
            "Cultural Activity",
            "Paper Presentation",
            "Certification",
            "Other"
        ],
        state="readonly"
    )

    type_box.grid(
        row=0,
        column=1,
        padx=25,
        pady=10
    )


    # Activity Name

    tk.Label(
        form,
        text="Activity Name *",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=1,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    name_entry = create_entry(
        form,
        40
    )

    name_entry.grid(
        row=1,
        column=1,
        padx=25,
        pady=10
    )


    # Organization

    tk.Label(
        form,
        text="College / Organization *",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=2,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    organization_entry = create_entry(
        form,
        40
    )

    organization_entry.grid(
        row=2,
        column=1,
        padx=25,
        pady=10
    )


    # Date

    tk.Label(
        form,
        text="Date *",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=3,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    date_entry = create_entry(
        form,
        40
    )

    date_entry.grid(
        row=3,
        column=1,
        padx=25,
        pady=10
    )


    # Status

    tk.Label(
        form,
        text="Status *",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=4,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    status_box = ttk.Combobox(
        form,
        width=37,
        values=[
            "Completed",
            "Ongoing",
            "Participated"
        ],
        state="readonly"
    )

    status_box.grid(
        row=4,
        column=1,
        padx=25,
        pady=10
    )


    # Certificate

    tk.Label(
        form,
        text="Certificate",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=5,
        column=0,
        padx=25,
        pady=10,
        sticky="w"
    )


    certificate_box = ttk.Combobox(
        form,
        width=37,
        values=[
            "Yes",
            "No"
        ],
        state="readonly"
    )

    certificate_box.grid(
        row=5,
        column=1,
        padx=25,
        pady=10
    )


    # Description

    tk.Label(
        form,
        text="Description",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).grid(
        row=6,
        column=0,
        padx=25,
        pady=10,
        sticky="nw"
    )


    description = tk.Text(
        form,
        width=40,
        height=5,
        font=("Segoe UI", 10),
        relief="solid",
        bd=1
    )

    description.grid(
        row=6,
        column=1,
        padx=25,
        pady=10
    )


    def save_activity():

        activity_type = type_box.get()
        activity_name = name_entry.get().strip()
        organization = organization_entry.get().strip()
        date = date_entry.get().strip()
        status = status_box.get()
        certificate = certificate_box.get()
        description_text = description.get(
            "1.0",
            tk.END
        ).strip()


        if (
            activity_type == ""
            or activity_name == ""
            or organization == ""
            or date == ""
            or status == ""
            or certificate == ""
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please fill all required fields."
            )

            return


        activity_number = len(activities) + 1

        activity_id = "A" + str(activity_number)


        new_activity = {

            "activity_id": activity_id,
            "student_id": student["id"],
            "type": activity_type,
            "name": activity_name,
            "organization": organization,
            "date": date,
            "status": status,
            "certificate": certificate,
            "description": description_text

        }


        activities.append(new_activity)

        save_data()


        messagebox.showinfo(
            "Activity Added",
            "Your activity has been saved successfully!"
        )


        student_dashboard(student)


    buttons = tk.Frame(
        main,
        bg=BG_COLOR
    )

    buttons.pack()


    create_button(
        buttons,
        "Save Activity",
        save_activity,
        20
    ).grid(
        row=0,
        column=0,
        padx=10
    )


    tk.Button(
        buttons,
        text="Cancel",
        command=lambda: student_dashboard(student),
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        width=18,
        pady=8,
        cursor="hand2"
    ).grid(
        row=0,
        column=1,
        padx=10
    )


# ============================================================
# VIEW MY ACTIVITIES
# ============================================================

def view_my_activities(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="My Activities",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(
        side="left",
        padx=30,
        pady=25
    )


    frame = tk.Frame(
        main,
        bg=WHITE
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )


    columns = (
        "ID",
        "Type",
        "Activity",
        "Organization",
        "Date",
        "Status",
        "Certificate"
    )


    table = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        table.heading(
            column,
            text=column
        )

        table.column(
            column,
            width=130
        )


    for activity in activities:

        if activity["student_id"] == student["id"]:

            table.insert(
                "",
                tk.END,
                values=(
                    activity["activity_id"],
                    activity["type"],
                    activity["name"],
                    activity["organization"],
                    activity["date"],
                    activity["status"],
                    activity["certificate"]
                )
            )


    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=table.yview
    )

    table.configure(
        yscrollcommand=scrollbar.set
    )


    table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    create_button(
        main,
        "Back to Dashboard",
        lambda: student_dashboard(student),
        22
    ).pack(pady=15)


# ============================================================
# UPDATE ACTIVITY
# ============================================================

def update_activity(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Update Activity",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=27)


    form = tk.Frame(
        main,
        bg=WHITE
    )

    form.pack(
        pady=50
    )


    tk.Label(
        form,
        text="Activity ID",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE
    ).grid(
        row=0,
        column=0,
        padx=15,
        pady=15
    )


    id_entry = create_entry(
        form,
        30
    )

    id_entry.grid(
        row=0,
        column=1,
        padx=15
    )


    tk.Label(
        form,
        text="New Status",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE
    ).grid(
        row=1,
        column=0,
        padx=15,
        pady=15
    )


    status_box = ttk.Combobox(
        form,
        width=27,
        values=[
            "Completed",
            "Ongoing",
            "Participated"
        ],
        state="readonly"
    )

    status_box.grid(
        row=1,
        column=1,
        padx=15
    )


    def update():

        activity_id = id_entry.get().strip()
        new_status = status_box.get()


        if activity_id == "" or new_status == "":

            messagebox.showwarning(
                "Missing Information",
                "Enter Activity ID and select a status."
            )

            return


        for activity in activities:

            if (
                activity["activity_id"] == activity_id
                and activity["student_id"] == student["id"]
            ):

                activity["status"] = new_status

                save_data()


                messagebox.showinfo(
                    "Updated",
                    "Activity updated successfully!"
                )


                student_dashboard(student)

                return


        messagebox.showerror(
            "Not Found",
            "Activity not found."
        )


    create_button(
        main,
        "Update Activity",
        update,
        20
    ).pack(pady=15)


    tk.Button(
        main,
        text="Back",
        command=lambda: student_dashboard(student),
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        width=20,
        pady=8
    ).pack()


# ============================================================
# DELETE ACTIVITY
# ============================================================

def delete_activity(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=RED,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Delete Activity",
        font=("Segoe UI", 23, "bold"),
        bg=RED,
        fg=WHITE
    ).pack(pady=27)


    tk.Label(
        main,
        text="Enter the Activity ID you want to delete.",
        font=("Segoe UI", 11),
        bg=BG_COLOR,
        fg=GRAY
    ).pack(pady=(50, 10))


    id_entry = create_entry(
        main,
        30
    )

    id_entry.pack()


    def delete():

        activity_id = id_entry.get().strip()


        for activity in activities:

            if (
                activity["activity_id"] == activity_id
                and activity["student_id"] == student["id"]
            ):

                answer = messagebox.askyesno(
                    "Confirm Delete",
                    "Are you sure you want to delete this activity?"
                )


                if answer:

                    activities.remove(activity)

                    save_data()

                    messagebox.showinfo(
                        "Deleted",
                        "Activity deleted successfully!"
                    )


                student_dashboard(student)

                return


        messagebox.showerror(
            "Not Found",
            "Activity not found."
        )


    create_button(
        main,
        "Delete Activity",
        delete,
        20
    ).pack(pady=20)


    tk.Button(
        main,
        text="Cancel",
        command=lambda: student_dashboard(student),
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        width=20,
        pady=8
    ).pack()


# ============================================================
# STUDENT PROGRESS
# ============================================================

def student_progress(student):

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="My Progress",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=27)


    my_activities = []


    for activity in activities:

        if activity["student_id"] == student["id"]:

            my_activities.append(activity)


    total = len(my_activities)
    completed = 0
    ongoing = 0
    participated = 0
    certificates = 0


    for activity in my_activities:

        if activity["status"] == "Completed":
            completed += 1

        elif activity["status"] == "Ongoing":
            ongoing += 1

        elif activity["status"] == "Participated":
            participated += 1

        if activity["certificate"] == "Yes":
            certificates += 1


    cards = tk.Frame(
        main,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=50,
        pady=40
    )


    for i in range(5):

        cards.columnconfigure(
            i,
            weight=1
        )


    create_card(
        cards,
        "Total",
        total,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=0,
        padx=5,
        sticky="nsew"
    )


    create_card(
        cards,
        "Completed",
        completed,
        GREEN
    ).grid(
        row=0,
        column=1,
        padx=5,
        sticky="nsew"
    )


    create_card(
        cards,
        "Ongoing",
        ongoing,
        ORANGE
    ).grid(
        row=0,
        column=2,
        padx=5,
        sticky="nsew"
    )


    create_card(
        cards,
        "Participated",
        participated,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=3,
        padx=5,
        sticky="nsew"
    )


    create_card(
        cards,
        "Certificates",
        certificates,
        GREEN
    ).grid(
        row=0,
        column=4,
        padx=5,
        sticky="nsew"
    )


    report = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    report.pack(
        fill="both",
        expand=True,
        padx=50,
        pady=10
    )


    tk.Label(
        report,
        text="Activity Progress Summary",
        font=("Segoe UI", 15, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        anchor="w",
        padx=25,
        pady=20
    )


    if total == 0:

        tk.Label(
            report,
            text="No activity data available yet.",
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=GRAY
        ).pack(pady=30)

    else:

        progress_items = [
            ("Completed Activities", completed, GREEN),
            ("Ongoing Activities", ongoing, ORANGE),
            ("Participated Activities", participated, PRIMARY_COLOR),
            ("Certificates Received", certificates, PRIMARY_COLOR)
        ]


        for label_text, value, color in progress_items:

            row = tk.Frame(
                report,
                bg=WHITE
            )

            row.pack(
                fill="x",
                padx=25,
                pady=7
            )


            tk.Label(
                row,
                text=label_text,
                font=("Segoe UI", 10),
                bg=WHITE,
                fg=TEXT_COLOR,
                width=28,
                anchor="w"
            ).pack(side="left")


            percentage = int(
                (value / total) * 100
            ) if total > 0 else 0


            bar_background = tk.Frame(
                row,
                bg="#E2E8F0",
                height=14,
                width=400
            )

            bar_background.pack(
                side="left",
                padx=10
            )

            bar_background.pack_propagate(False)


            bar = tk.Frame(
                bar_background,
                bg=color,
                height=14,
                width=max(5, int(400 * percentage / 100))
            )

            bar.pack(
                side="left"
            )


            tk.Label(
                row,
                text=str(value) + " (" + str(percentage) + "%)",
                font=("Segoe UI", 10, "bold"),
                bg=WHITE,
                fg=TEXT_COLOR
            ).pack(side="left")


    create_button(
        main,
        "Back to Dashboard",
        lambda: student_dashboard(student),
        22
    ).pack(pady=15)


# ============================================================
# MENTOR LOGIN
# ============================================================

def mentor_login():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    left = tk.Frame(
        main,
        bg=SIDEBAR_COLOR,
        width=450
    )

    left.pack(
        side="left",
        fill="y"
    )

    left.pack_propagate(False)


    tk.Label(
        left,
        text="👨‍🏫",
        font=("Segoe UI Emoji", 55),
        bg=SIDEBAR_COLOR,
        fg=WHITE
    ).pack(pady=(150, 10))


    tk.Label(
        left,
        text="Mentor Portal",
        font=("Segoe UI", 25, "bold"),
        bg=SIDEBAR_COLOR,
        fg=WHITE
    ).pack()


    tk.Label(
        left,
        text="Monitor student activities\n"
             "and overall progress.",
        font=("Segoe UI", 11),
        bg=SIDEBAR_COLOR,
        fg="#CBD5E1",
        justify="center"
    ).pack(pady=15)


    right = tk.Frame(
        main,
        bg=WHITE
    )

    right.pack(
        side="left",
        fill="both",
        expand=True
    )


    tk.Label(
        right,
        text="Mentor Login",
        font=("Segoe UI", 24, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(pady=(150, 10))


    tk.Label(
        right,
        text="Enter mentor credentials",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY
    ).pack(pady=(0, 25))


    form = tk.Frame(
        right,
        bg=WHITE
    )

    form.pack()


    tk.Label(
        form,
        text="Username",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=8
    )


    username_entry = create_entry(
        form,
        32
    )

    username_entry.grid(
        row=1,
        column=0,
        pady=(0, 15)
    )


    tk.Label(
        form,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=8
    )


    password_entry = create_entry(
        form,
        32
    )

    password_entry.config(
        show="*"
    )

    password_entry.grid(
        row=3,
        column=0,
        pady=(0, 20)
    )


    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()


        if username == "mentor" and password == "1234":

            mentor_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid mentor username or password."
            )


    create_button(
        right,
        "Login",
        login,
        25
    ).pack(pady=10)


    tk.Button(
        right,
        text="← Back to Home",
        command=home_page,
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY,
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)


# ============================================================
# MENTOR DASHBOARD
# ============================================================

def mentor_dashboard():

    clear_window()


    sidebar = tk.Frame(
        root,
        bg=SIDEBAR_COLOR,
        width=240
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)


    tk.Label(
        sidebar,
        text="MENTOR",
        font=("Segoe UI", 20, "bold"),
        bg=SIDEBAR_COLOR,
        fg=WHITE
    ).pack(pady=(35, 0))


    tk.Label(
        sidebar,
        text="ADMIN PANEL",
        font=("Segoe UI", 9),
        bg=SIDEBAR_COLOR,
        fg="#94A3B8"
    ).pack(pady=(0, 35))


    def side_button(text, command):

        button = tk.Button(
            sidebar,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            bg=SIDEBAR_COLOR,
            fg="#CBD5E1",
            activebackground="#334155",
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            pady=11,
            cursor="hand2"
        )

        button.pack(
            fill="x"
        )


    side_button(
        "▣   Dashboard",
        mentor_dashboard
    )

    side_button(
        "👥   All Students",
        view_all_students
    )

    side_button(
        "☷   All Activities",
        view_all_activities
    )

    side_button(
        "⌕   Search Student",
        search_student
    )

    side_button(
        "▤   Overall Report",
        overall_report
    )


    tk.Button(
        sidebar,
        text="Logout",
        command=home_page,
        font=("Segoe UI", 10, "bold"),
        bg="#334155",
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        pady=10
    ).pack(
        side="bottom",
        fill="x",
        padx=20,
        pady=25
    )


    content = tk.Frame(
        root,
        bg=BG_COLOR
    )

    content.pack(
        side="left",
        fill="both",
        expand=True
    )


    header = tk.Frame(
        content,
        bg=WHITE,
        height=80
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Mentor Dashboard",
        font=("Segoe UI", 22, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        side="left",
        padx=30,
        pady=25
    )


    tk.Label(
        header,
        text="Student Activity Management",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=GRAY
    ).pack(
        side="right",
        padx=30
    )


    body = tk.Frame(
        content,
        bg=BG_COLOR
    )

    body.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )


    tk.Label(
        body,
        text="Overview",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(anchor="w")


    tk.Label(
        body,
        text="Monitor student extracurricular participation.",
        font=("Segoe UI", 10),
        bg=BG_COLOR,
        fg=GRAY
    ).pack(
        anchor="w",
        pady=(3, 20)
    )


    total_students = len(students)
    total_activities = len(activities)

    completed = 0
    ongoing = 0
    certificates = 0


    for activity in activities:

        if activity["status"] == "Completed":
            completed += 1

        if activity["status"] == "Ongoing":
            ongoing += 1

        if activity["certificate"] == "Yes":
            certificates += 1


    cards = tk.Frame(
        body,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x"
    )


    for i in range(4):

        cards.columnconfigure(
            i,
            weight=1
        )


    create_card(
        cards,
        "Total Students",
        total_students,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=0,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Total Activities",
        total_activities,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=1,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Completed",
        completed,
        GREEN
    ).grid(
        row=0,
        column=2,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Certificates",
        certificates,
        ORANGE
    ).grid(
        row=0,
        column=3,
        padx=7,
        sticky="nsew"
    )


    # Quick actions

    actions = tk.Frame(
        body,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    actions.pack(
        fill="x",
        pady=25
    )


    tk.Label(
        actions,
        text="Quick Actions",
        font=("Segoe UI", 14, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )


    action_buttons = tk.Frame(
        actions,
        bg=WHITE
    )

    action_buttons.pack(
        pady=(0, 20)
    )


    create_button(
        action_buttons,
        "View Students",
        view_all_students,
        18
    ).grid(
        row=0,
        column=0,
        padx=8
    )


    create_button(
        action_buttons,
        "View Activities",
        view_all_activities,
        18
    ).grid(
        row=0,
        column=1,
        padx=8
    )


    create_button(
        action_buttons,
        "Search Student",
        search_student,
        18
    ).grid(
        row=0,
        column=2,
        padx=8
    )


    create_button(
        action_buttons,
        "View Report",
        overall_report,
        18
    ).grid(
        row=0,
        column=3,
        padx=8
    )


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_all_students():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="All Students",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(
        side="left",
        padx=30,
        pady=27
    )


    frame = tk.Frame(
        main,
        bg=WHITE
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )


    columns = (
        "ID",
        "Name",
        "Department",
        "Year",
        "Email",
        "Phone"
    )


    table = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        table.heading(
            column,
            text=column
        )

        table.column(
            column,
            width=150
        )


    for student in students:

        table.insert(
            "",
            tk.END,
            values=(
                student["id"],
                student["name"],
                student["department"],
                student["year"],
                student["email"],
                student["phone"]
            )
        )


    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=table.yview
    )

    table.configure(
        yscrollcommand=scrollbar.set
    )


    table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    create_button(
        main,
        "Back to Dashboard",
        mentor_dashboard,
        22
    ).pack(pady=15)


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Search Student",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=27)


    search_frame = tk.Frame(
        main,
        bg=BG_COLOR
    )

    search_frame.pack(
        pady=30
    )


    tk.Label(
        search_frame,
        text="Student ID",
        font=("Segoe UI", 10, "bold"),
        bg=BG_COLOR
    ).grid(
        row=0,
        column=0,
        padx=10
    )


    id_entry = create_entry(
        search_frame,
        30
    )

    id_entry.grid(
        row=0,
        column=1,
        padx=10
    )


    result_frame = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    result_frame.pack(
        fill="x",
        padx=120,
        pady=10
    )


    result_label = tk.Label(
        result_frame,
        text="Enter a Student ID and click Search.",
        font=("Segoe UI", 11),
        bg=WHITE,
        fg=GRAY,
        justify="left"
    )

    result_label.pack(
        anchor="w",
        padx=25,
        pady=25
    )


    def search():

        student_id = id_entry.get().strip()


        for student in students:

            if student["id"] == student_id:

                count = 0
                completed = 0


                for activity in activities:

                    if activity["student_id"] == student_id:

                        count += 1

                        if activity["status"] == "Completed":

                            completed += 1


                result = (
                    "Student ID: " + student["id"] + "\n\n"
                    "Name: " + student["name"] + "\n\n"
                    "Department: " + student["department"] + "\n\n"
                    "Year: " + student["year"] + "\n\n"
                    "Email: " + student["email"] + "\n\n"
                    "Phone: " + student["phone"] + "\n\n"
                    "Total Activities: " + str(count) + "\n\n"
                    "Completed Activities: " + str(completed)
                )


                result_label.config(
                    text=result,
                    fg=TEXT_COLOR
                )

                return


        result_label.config(
            text="Student not found.",
            fg=RED
        )


    create_button(
        main,
        "Search",
        search,
        20
    ).pack(pady=10)


    tk.Button(
        main,
        text="Back",
        command=mentor_dashboard,
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        width=20,
        pady=8
    ).pack()


# ============================================================
# VIEW ALL ACTIVITIES
# ============================================================

def view_all_activities():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="All Student Activities",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(
        side="left",
        padx=30,
        pady=27
    )


    frame = tk.Frame(
        main,
        bg=WHITE
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )


    columns = (
        "ID",
        "Student ID",
        "Type",
        "Activity",
        "Organization",
        "Date",
        "Status",
        "Certificate"
    )


    table = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        table.heading(
            column,
            text=column
        )

        table.column(
            column,
            width=120
        )


    for activity in activities:

        table.insert(
            "",
            tk.END,
            values=(
                activity["activity_id"],
                activity["student_id"],
                activity["type"],
                activity["name"],
                activity["organization"],
                activity["date"],
                activity["status"],
                activity["certificate"]
            )
        )


    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=table.yview
    )

    table.configure(
        yscrollcommand=scrollbar.set
    )


    table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    create_button(
        main,
        "Back to Dashboard",
        mentor_dashboard,
        22
    ).pack(pady=15)


# ============================================================
# OVERALL REPORT
# ============================================================

def overall_report():

    clear_window()


    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )


    header = tk.Frame(
        main,
        bg=PRIMARY_COLOR,
        height=90
    )

    header.pack(fill="x")
    header.pack_propagate(False)


    tk.Label(
        header,
        text="Overall College Report",
        font=("Segoe UI", 23, "bold"),
        bg=PRIMARY_COLOR,
        fg=WHITE
    ).pack(pady=27)


    total_students = len(students)
    total_activities = len(activities)


    completed = 0
    ongoing = 0
    participated = 0
    certificates = 0


    activity_types = {

        "Course": 0,
        "Workshop": 0,
        "Hackathon": 0,
        "Competition": 0,
        "Internship": 0,
        "Seminar": 0,
        "Event": 0

    }


    for activity in activities:

        if activity["status"] == "Completed":
            completed += 1

        elif activity["status"] == "Ongoing":
            ongoing += 1

        elif activity["status"] == "Participated":
            participated += 1


        if activity["certificate"] == "Yes":
            certificates += 1


        if activity["type"] in activity_types:

            activity_types[activity["type"]] += 1


    cards = tk.Frame(
        main,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=40,
        pady=30
    )


    for i in range(4):

        cards.columnconfigure(
            i,
            weight=1
        )


    create_card(
        cards,
        "Students",
        total_students,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=0,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Activities",
        total_activities,
        PRIMARY_COLOR
    ).grid(
        row=0,
        column=1,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Completed",
        completed,
        GREEN
    ).grid(
        row=0,
        column=2,
        padx=7,
        sticky="nsew"
    )


    create_card(
        cards,
        "Certificates",
        certificates,
        ORANGE
    ).grid(
        row=0,
        column=3,
        padx=7,
        sticky="nsew"
    )


    report = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground=BORDER_COLOR,
        highlightthickness=1
    )

    report.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=5
    )


    tk.Label(
        report,
        text="Activity Type Summary",
        font=("Segoe UI", 15, "bold"),
        bg=WHITE,
        fg=TEXT_COLOR
    ).pack(
        anchor="w",
        padx=25,
        pady=15
    )


    for activity_type, count in activity_types.items():

        row = tk.Frame(
            report,
            bg=WHITE
        )

        row.pack(
            fill="x",
            padx=25,
            pady=4
        )


        tk.Label(
            row,
            text=activity_type,
            font=("Segoe UI", 10),
            bg=WHITE,
            fg=TEXT_COLOR,
            width=20,
            anchor="w"
        ).pack(
            side="left"
        )


        tk.Label(
            row,
            text=str(count),
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=PRIMARY_COLOR
        ).pack(
            side="left"
        )


    create_button(
        main,
        "Back to Dashboard",
        mentor_dashboard,
        22
    ).pack(pady=15)


# ============================================================
# START APPLICATION
# ============================================================

load_data()

home_page()

root.mainloop()
