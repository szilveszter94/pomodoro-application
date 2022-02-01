from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
# ez a funkció lenullázza az időt, az ismétléseket és a check boxot
def reset_timer():
    global marks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg=GREEN)
    reps = 0
    check_box.config(text="")

#ez a funkció elindítja az időt, hozzáad egy ismétlést


def start_timer():
    global reps
    reps += 1

    # milyen hosszú legyen a tanulásra szánt idő és a szünet
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    # ha megtörtént 8 ismétlés, akkor hosszú szünet
    if reps % 8 == 0:
        text_label.config(text="Break", fg=RED)
        count_down(long_break_min)
    # ha megtörtént 2 ismétlés, akkor rövid szünet
    elif reps % 2 == 0:
        text_label.config(text="Break", fg=PINK)
        count_down(short_break_min)
    # ha egyik sem, akkor a tanulási idő pörög
    else:
        text_label.config(text="Work", fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#számláló, átváltja a megadott számot idő formátummá

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # ha a másodperc 10 alatt van, akkor elé ír egy nullát
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # ha a másodperc nagyobb, mint 0, akkor pörög a számláló
    if count >= 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    # ha egyik sem, akkor újból indítja az időt, hozzáad egy pipát ami az ismétlést jelzi
    else:
        global marks
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
            check_box.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #
#felhasználói felület konfigurálása
window = Tk()
#ablak
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
#kép
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato)
#gombok
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=3, row=3)
#check box
check_box = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_box.grid(column=1, row=4)
#szövegmező
text_label = Label(text="Timer", font=("BioRhyme", 30, "bold"), fg=GREEN, bg=YELLOW)
text_label.grid(column=1, row=0)
#idő
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=("Impact", 25, "normal"))
canvas.grid(column=1, row=1)
#ablak folyamatos frissítése
window.mainloop()
