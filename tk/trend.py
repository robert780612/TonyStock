
from tkinter import *
from tkinter.ttk import *
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class Trend:
    def __init__(self, master=None):
        self.master = master
        self.master.maxsize(800, 600)
        self.master.minsize(800, 600)

        self.frame_start_time = Frame(self.master)
        self.frame_start_time.grid(row=0)
        self.create_start_time_widget()

        self.frame_end_time = Frame(self.master)
        self.frame_end_time.grid(row=1)
        self.create_end_time_widget()

        self.frame_ok = Frame(self.master)
        self.frame_ok.grid(row=2)
        self.button_ok = Button(self.frame_ok, text='OK', command=self.plot)
        self.button_ok.grid(row=0)

    def create_start_time_widget(self):
        self.label_from = Label(self.frame_start_time, text='Start Time:')
        self.label_from.grid(row=0, column=0)
        # Year label
        self.label_year = Label(self.frame_start_time, text='Year')
        self.label_year.grid(row=0, column=1)

        # Set year menu
        self.year = StringVar()
        self.menu_year = Menu(self.frame_start_time, tearoff=0)
        self.menu_year.add_radiobutton(label='2016', variable=self.year, value='2016', command=self.show_year)
        self.menu_year.add_radiobutton(label='2015', variable=self.year, value='2015', command=self.show_year)
        self.menubutton_year = Menubutton(self.frame_start_time, menu=self.menu_year, text='Select Year')
        self.menubutton_year.grid(row=0, column=2)

        # Month label
        self.label_month = Label(self.frame_start_time, text='Month')
        self.label_month.grid(row=0, column=3)

        # Set month menu
        self.month = StringVar()
        self.menu_month = Menu(self.frame_start_time, tearoff=0)
        for i in range(1,13):
            self.menu_month.add_radiobutton(label=str(i), variable=self.month, value=i, command=self.show_month)

        self.menubutton_month = Menubutton(self.frame_start_time, menu=self.menu_month, text='Select Month')
        self.menubutton_month.grid(row=0, column=4)

        # Day label
        self.label_day = Label(self.frame_start_time, text='Day')
        self.label_day.grid(row=0, column=5)

        # Set day menu
        self.day = StringVar()
        self.menu_day = Menu(self.frame_start_time, tearoff=0, postcommand=self.generate_days)

        self.menubutton_day = Menubutton(self.frame_start_time, menu=self.menu_day, text='Select Day')
        self.menubutton_day.grid(row=0, column=6)

    def create_end_time_widget(self):
        self.label_end = Label(self.frame_end_time, text='End Time:')
        self.label_end.grid(row=0, column=0)
        # Year label
        self.label_end_year = Label(self.frame_end_time, text='Year')
        self.label_end_year.grid(row=0, column=1)

        # Set year menu
        self.end_year = StringVar()
        self.menu_end_year = Menu(self.frame_end_time, tearoff=0)
        self.menu_end_year.add_radiobutton(label='2016', variable=self.end_year, value='2016', command=self.show_end_year)
        self.menu_end_year.add_radiobutton(label='2015', variable=self.end_year, value='2015', command=self.show_end_year)
        self.menubutton_end_year = Menubutton(self.frame_end_time, menu=self.menu_end_year, text='Select Year')
        self.menubutton_end_year.grid(row=0, column=2)

        # Month label
        self.label_end_month = Label(self.frame_end_time, text='Month')
        self.label_end_month.grid(row=0, column=3)

        # Set month menu
        self.end_month = StringVar()
        self.menu_end_month = Menu(self.frame_end_time, tearoff=0)
        for i in range(1,13):
            self.menu_end_month.add_radiobutton(label=str(i), variable=self.end_month, value=i, command=self.show_end_month)

        self.menubutton_end_month = Menubutton(self.frame_end_time, menu=self.menu_end_month, text='Select Month')
        self.menubutton_end_month.grid(row=0, column=4)

        # Day label
        self.label_end_day = Label(self.frame_end_time, text='Day')
        self.label_end_day.grid(row=0, column=5)

        # Set day menu
        self.end_day = StringVar()
        self.menu_end_day = Menu(self.frame_end_time, tearoff=0, postcommand=self.generate_end_days)

        self.menubutton_end_day = Menubutton(self.frame_end_time, menu=self.menu_end_day, text='Select Day')
        self.menubutton_end_day.grid(row=0, column=6)

    def show_year(self):
        self.menubutton_year.config(text=self.year.get())
        # Prevent the day exceed the maximum of this month
        self.day.set(0)
        self.menubutton_day.config(text='Select Day')

    def show_month(self):
        self.menubutton_month.config(text=self.month.get())
        # Prevent the day exceed the maximum of this month
        self.day.set(0)
        self.menubutton_day.config(text='Select Day')

    def generate_days(self):
        year = int(self.year.get())
        month = int(self.month.get())
        max_day = self.calculate_days(year, month)
        # Generate the menu of day
        self.menu_day.delete(0,31)
        for i in range(1, max_day+1):
            self.menu_day.add_radiobutton(label=str(i), variable=self.day, value=i, command=self.show_day)

    def show_day(self):
        self.menubutton_day.config(text=self.day.get())

    def show_end_year(self):
        self.menubutton_end_year.config(text=self.end_year.get())
        # Prevent the day exceed the maximum of this month
        self.end_day.set(0)
        self.menubutton_end_day.config(text='Select Day')

    def show_end_month(self):
        self.menubutton_end_month.config(text=self.end_month.get())
        # Prevent the day exceed the maximum of this month
        self.end_day.set(0)
        self.menubutton_end_day.config(text='Select Day')

    def generate_end_days(self):
        year = int(self.end_year.get())
        month = int(self.end_month.get())
        max_day = self.calculate_days(year, month)
        # Generate the menu of day
        self.menu_end_day.delete(0,31)
        for i in range(1, max_day+1):
            self.menu_end_day.add_radiobutton(label=str(i), variable=self.end_day, value=i, command=self.show_end_day)

    def show_end_day(self):
        self.menubutton_end_day.config(text=self.end_day.get())

    @staticmethod
    def calculate_days(year, month):
        if year % 400 == 0:
            leaf = 1
        elif year % 100 == 0:
            leaf = 0
        elif year % 4 == 0:
            leaf = 1
        else:
            leaf = 0
        day_in_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        max_day = day_in_month[month]
        if month == 2 and leaf:
            max_day = 29
        return max_day

    def plot(self):
        # Create figure
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        a.plot(t, s)

        self.frame_figure = Frame(self.master)
        self.frame_figure.grid(row=3)
        self.canvas = FigureCanvasTkAgg(f, self.frame_figure)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0)
        self.frame_toolbar = Frame(self.master)
        self.frame_toolbar.grid(row=4)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame_toolbar)
        self.toolbar.update()


root = Tk()
app = Trend(master=root)
root.mainloop()
