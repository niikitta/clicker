from tkinter import *
window = Tk()
window.title("кликер")
window.geometry("1000x700")
count = 0
click_power = 1
upgrade_cost = 100
upgrade2_cost = 1000
upgrade3_cost = 14880
auto_active = False
auto_delay = 500
knopka = Label(window, text = "жми!", )
knopka.pack()

clickpower = Label(window, text = f"Сила клика: {click_power}", font = ("Arial", 15))
clickpower.place(relx = 0.72, rely= 0.05,)

frame = Frame(window)
frame.place(relx = 0, rely = 0, anchor = "nw")

def hello():
    global count
    count += click_power
    schetchik.config(text = count)
    if count >= 3000:
        button3.config(text=f"СУПЕР-улучшение за {upgrade3_cost} кликов")

button = Button(window, text = "Жми", command = hello, width = 30, height = 15, bg = "blue", fg = "white", activebackground = "light green")
button.pack()

schetchik = Label(window, text = 0, font = ("Arial", 30))
schetchik.place(relx = 0.8, rely= 0.1,)

def bye():
    global count, click_power, upgrade_cost
    if count >= upgrade_cost:
        count -= upgrade_cost
        schetchik.config(text = count)
        print("Куплено улучшение! +1 клик")
        click_power += 1
        clickpower.config(text=f"Сила клика: {click_power}")
        upgrade_cost = round(upgrade_cost * 1.3)
        button1.config(text = f"улучшение за {upgrade_cost} кликов")
    else:
        print(f"Недостаточно кликов! Нужно {upgrade_cost}, у вас:", count)

button1 = Button(frame, text = f"улучшение за {upgrade_cost} кликов", command = bye, width = 30, height = 5, bg = "red", fg = "white", activebackground = "gray")
button1.pack()


def priv():
    global count, click_power, upgrade_cost, upgrade2_cost
    if count >= upgrade2_cost:
        count -= upgrade2_cost
        schetchik.config(text = count)
        print("Куплено большое улучшение! В 2 раза больше кликов!")
        click_power *= 2
        clickpower.config(text=f"Сила клика: {click_power}")
        upgrade2_cost = round(upgrade2_cost * 5)
        button2.config(text = f"улучшение за {upgrade2_cost} кликов",)
    else:
        print(f"Недостаточно кликов! Нужно {upgrade2_cost}, у вас:", count)

button2 = Button(frame, text = f"улучшение за {upgrade2_cost} кликов", command = priv, width = 30, height = 5, bg = "red", fg = "white", activebackground = "gray")
button2.pack()

def pok():
    global count, click_power, upgrade3_cost
    if count >= upgrade3_cost:
        count -= upgrade3_cost
        schetchik.config(text = count)
        print("Куплено МЕГА-УЛУЧШЕНИЕ! ВСЕ КЛИКИ умножаются на 10")
        click_power *= 10
        clickpower.config(text = f"Сила клика: {click_power}")
        upgrade3_cost = round(upgrade3_cost * 100)
        button3.config(text = f"улучшение за {upgrade3_cost} кликов")
    else:
        print(f"Недостаточно кликов! Нужно {upgrade3_cost}, у вас:", count)

button3 = Button(frame, text = "???", command = pok, width = 30, height = 5, bg = "red", fg = "white", activebackground = "gray")
button3.pack()

def auto_click():
    global auto_active
    if auto_active:
        hello()
        window.after(auto_delay, auto_click)

def toggle_auto():
    global auto_active
    if auto_active:
        auto_active = False
        autoclick.config(text="автокликер(для слабых)", bg="red")
        print("Автокликер остановлен")
    else:
        auto_active = True
        autoclick.config(text="автокликер(ВКЛЮЧЁН(слабак))", bg="green")
        print("Автокликер запущен")
        auto_click()
autoclick = Button(window, text = "автокликер(для слабых)", command = toggle_auto, width = 30, height = 5, bg = "red", fg = "white")
autoclick.pack()

def secret():
    okno = Tk()
    okno.title("загадки")
    okno.geometry("1000x700")
    def otvet():
        print("ЛОХ")
        okno.destroy()
        button4.destroy()
    def otvet2():
        print("ЛОХ")
        okno.destroy()
        button4.destroy()
    def otvet3():
        global click_power
        click_power += 5
        clickpower.config(text = f"Сила клика: {click_power}")
        print("КРАСАВА!!!!!!!! ДЕРЖИ ОБЕЩАННЫЕ КЛИКИ ГЕНИЙ")
        okno.destroy()
        button4.destroy()

    zagadka = Label(okno, text="Отгадай загадку - получи +5 за клик", font=("Arial", 30))
    zagadka.pack()
    zagtext = Label(okno, text = "Что теряет голову утром, но получает обратно ночью?", font=("Arial", 15))
    zagtext.pack()
    butzag = Button(okno, text = "Петух", command = otvet, width = 15, height = 5, bg = "black", fg = "white", font = ("Arial", 20))
    butzag.place(relx = 0.15, rely = 0.4)
    butzag2 = Button(okno, text = "Гвоздь", command = otvet2, width = 15, height = 5, bg = "black", fg = "white", font = ("Arial", 20))
    butzag2.pack()
    butzag3 = Button(okno, text = "Подушка", command = otvet3, width = 15, height = 5, bg = "black", fg = "white", font = ("Arial", 20))
    butzag3.place(relx=0.55, rely=0.4)
button4 = Button(window, text = "ЗАГАДКА", command = secret, width = 20, height = 5, bg = "black", fg = "white", font = ("Arial", 10))
button4.place(relx = 0.9, rely = 0.9,)

window.mainloop()




