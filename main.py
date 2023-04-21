import kitsu
import asyncio
from tkinter import *
from tkinter.ttk import *
from KitsuApi import KitsuApi


app = Tk()
app.title("Anime Hledani")
app.geometry("500x500")

hledat_text = StringVar()

hledat_label = Label(app, text="Hedat anime:")
hledat_label.grid(row=0, column=0, sticky=W)

search = StringVar()
hledat_entry = Entry(app, textvariable=hledat_text)
hledat_entry.grid(row=0, column=1)

vysledky_list = Listbox(app)
vysledky_list.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)
# Tlacitko pro hledani
def hledat_anime():
    text = hledat_text.get()
    vysledek_hledani = KitsuApi.hledat_anime(text)

    # vykresleni vysledku hledani
    vysledky_list.delete(0, END)
    if len(vysledek_hledani) == 0:
        vysledky_list.insert(END, "Nic nenalezeno")
    for item in vysledek_hledani:
        vysledky_list.insert(END, item["id"] + " - " + item["attributes"]["canonicalTitle"])

def zobrazit_detial(event):
    vybrano = vysledky_list.curselection()
    # pokud je vybrano vic nez 1 polozka, tak se zobrazi jen prvni
    if len(vybrano) > 1:
        vybrano = vybrano[0]
    # ziskani hodnoty z listboxu
    vybrano_id = vysledky_list.get(vybrano).split(" - ")[0]

    
    # ziskani detailu o vybranem anime
    detail = KitsuApi.zobrazit_detial(vybrano_id)

    # vytvoreni okna pro zobrazeni detailu
    detail_window = Toplevel(app)
    detail_window.title("Detail")
    detail_window.geometry("500x500")
    
    # zobrazeni detailu s popisky
    nazev_stitek = Label(detail_window, text="Nazev:")
    nazev_stitek.grid(row=0, column=0, sticky=W)

    nazev_hodnota = Label(detail_window, text=detail["attributes"]["canonicalTitle"])
    nazev_hodnota.grid(row=0, column=1, sticky=W)


    popis_stitek = Label(detail_window, text="Popis:")
    popis_stitek.grid(row=1, column=0, sticky=W)

    popis_hodnota = Label(detail_window, text=detail["attributes"]["synopsis"], wraplength=400)
    popis_hodnota.grid(row=1, column=1, sticky=W)


    hodnoceni_stitek = Label(detail_window, text="Hodnoceni:")
    hodnoceni_stitek.grid(row=2, column=0, sticky=W)

    hodnoceni_hodnota = Label(detail_window, text=detail["attributes"]["averageRating"])
    hodnoceni_hodnota.grid(row=2, column=1, sticky=W)


    zacatek_stitek = Label(detail_window, text="Zacatek:")
    zacatek_stitek.grid(row=3, column=0, sticky=W)

    zacatek_hodnota = Label(detail_window, text=detail["attributes"]["startDate"])
    zacatek_hodnota.grid(row=3, column=1, sticky=W)

    konec_stitek = Label(detail_window, text="Konec:")
    konec_stitek.grid(row=4, column=0, sticky=W)
    konec_hodnota = Label(detail_window, text=detail["attributes"]["endDate"])
    konec_hodnota.grid(row=4, column=1, sticky=W)

    epizody_stitek = Label(detail_window, text="Epizody:")
    epizody_stitek.grid(row=5, column=0, sticky=W)
    # list pro zobrazeni epizod
    epizody_list = Listbox(detail_window)
    epizody_list.grid(row=6, column=0, columnspan=3, sticky=W+E+N+S)

    epizody = KitsuApi.zobrazit_epizody(vybrano_id)
    # zobrazeni epizod
    for epizoda in epizody:
        epizody_list.insert(END, str(epizoda["attributes"]["canonicalTitle"]) + " - " + str(epizoda["attributes"]["number"]) + " - " + str(epizoda["attributes"]["airdate"]))


    

    
    

vysledky_list.bind("<<ListboxSelect>>", zobrazit_detial)
hledat_button = Button(app, text="hledat", command=hledat_anime)
hledat_button.grid(row=0, column=2, sticky=W)




app.mainloop()

