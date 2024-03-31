from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Toshkent = [
    "Bektemir tumani",
    "Chilonzor tumani",
    "Mirzo Ulug'bek tumani",
    "Shaykhontohur tumani",
    "Mirobod tumani",
    "Uchtepa tumani",
    "Yashnabad tumani",
    "Yunusobod tumani",
    "Orikzor tumani",
    "Sergeli tumani",
    "Olmazor tumani",
    "Yangiyo'l tumani",
]

Samarqand = [
    "Bulung'ur tumani",
    "Ishtixon tumani",
    "Jomboy tumani",
    "Kattaqo'rg'on tumani",
    "Koshrabot tumani",
    "Narpay tumani",
    "Nurobod tumani",
    "Oqdaryo tumani",
    "Pastdarg'om tumani",
    "Payariq tumani",
    "Samarkand tumani",
    "Toyloq tumani",
    "Urgut tumani"
]

Andijon = [
    "Andijon shahri",
    "Asaka tumani",
    "Baliqchi tumani",
    "Bo'z tumani",
    "Buloqboshi tumani",
    "Izboskan tumani",
    "Jalaquduq tumani",
    "Marhamat tumani",
    "Oltinko'l tumani",
    "Paxtaobod tumani",
    "Qo'rg'ontepa tumani",
    "Shahrixon tumani",
    "Ulug'nor tumani",
]

Buxoro = [
    "Alat tumani",
    "Buxoro tumani",
    "G'ijduvon tumani",
    "Jondor tumani",
    "Kog'on tumani",
    "Qorako'l tumani",
    "Romitan tumani",
    "Shofirkon tumani",
    "Vobkent tumani",
]

Navoiy = [
    "Karmana tumani",
    "Navbahor tumani",
    "Khatirchi tumani",
    "Qiziltepa tumani",
    "Uchquduq tumani",
    "Xatirchi tumani",
    "Zarafshon tumani",
]

Namangan = [
    "Bulung'ur tumani",
    "Ishtixon tumani",
    "Jomboy tumani",
    "Kattaqo'rg'on tumani",
    "Koshrabot tumani",
    "Nurobod tumani",
    "Oqdaryo tumani",
    "Pastdarg'om tumani",
    "Payariq tumani",
    "Samarqand tumani",
    "Toyloq tumani",
    "Urgut tumani",
]

# Namangan viloyati tumanlari
namangan = [
    "Chortoq tumani",
    "Kosonsoy tumani",
    "Mingbuloq tumani",
    "Namangan tumani",
    "Norin tumani",
    "Pop tumani",
    "To'raqo'rg'on tumani",
    "Uchko'prik tumani",
]

# Farg'ona viloyati tumanlari
Fargona = [
    "Buvayda tumani",
    "Dang'ara tumani",
    "Farg'ona tumani",
    "Furqat tumani",
    "Quva tumani",
    "Rishton tumani",
    "So'x tumani",
    "Toshloq tumani",
    "Uchqo'rg'on tumani",
    "Yozyovon tumani",
    "Oltiariq tumani",
]

# Qashqadaryo viloyati tumanlari
Qashqadaryo = [
    "Chirakchi tumani",
    "Dehqonobod tumani",
    "Kamashi tumani",
    "Kasbi tumani",
    "Kitob tumani",
    "Koson tumani",
    "Mirishkor tumani",
    "Muborak tumani",
    "Qamashi tumani",
    "Qarshi tumani",
    "Shahrisabz tumani",
    "Yakkabog' tumani",
]

# Surxondaryo viloyati tumanlari
Surxondaryo = [
    "Angor tumani",
    "Boysun tumani",
    "Denov tumani",
    "Jarqo'rg'on tumani",
    "Muzrabot tumani",
    "Oltinsoy tumani",
    "Sariosiyo tumani",
    "Sherobod tumani",
    "Termiz tumani",
    "Uzun tumani",
]

# Jizzax viloyati tumanlari
Jizzax = [
    "Arnasoy tumani",
    "Baxmal tumani",
    "Do'stlik tumani",
    "Forish tumani",
    "G'allaorol tumani",
    "Jizzax tumani",
    "Mirzacho'l tumani",
    "Paxtakor tumani",
    "Yangiobod tumani",
    "Zomin tumani",
]

# Xorazm viloyati tumanlari
Xorazm = [
    "Bag'at tumani",
    "Bog'ot tumani",
    "G'allaorol tumani",
    "Hazorasp tumani",
    "Qo'rg'ontepa tumani",
    "Shovot tumani",
    "Urganch tumani",
    "Xonqa tumani",
    "Yangibozor tumani",
]

# Sirdaryo viloyati tumanlari
Sirdaryo = [
    "Boyovut tumani",
    "Guliston tumani",
    "Sirdaryo tumani",
    "Mirzaobod tumani",
]

# Qoraqalpog'iston Respublikasi tumanlari
Qoraqalpogiston = [
    "Amudaryo tumani",
    "Beruniy tumani",
    "Bo'zatau tumani",
    "Chimboy tumani",
    "Ellikqala tumani",
    "Kegeyli tumani",
    "Mo'ynoq tumani",
    "Nukus tumani",
    "Qo'ng'irot tumani",
    "Qorao'zak tumani",
    "Qoshkopir tumani",
    "Shumanay tumani",
    "Taxtako'pir tumani",
    "To'rtko'l tumani",
    "Xo'jayli tumani",
]


# Tumanlar uchun InlineKeyboardMarkup yaratish
def create_tumanlar_keyboard(tumanlar):
    tumanlar_keyboard = InlineKeyboardMarkup(row_width=1)
    for tuman in tumanlar:
        tumanlar_keyboard.add(InlineKeyboardButton(tuman, callback_data=f"{tuman}"))
    return tumanlar_keyboard


async def inline_tumanlar(viloyat):
    region = None
    if viloyat == "Toshkent":
        region = Toshkent
    elif viloyat == "Samarqand":
        region = Samarqand
    elif viloyat == "Namangan":
        region = Namangan
    elif viloyat == "Andijon":
        region = Andijon
    elif viloyat == "Fargona":
        region = Fargona
    elif viloyat == "Qashqadaryo":
        region = Qashqadaryo
    elif viloyat == "Surxondaryo":
        region = Surxondaryo
    elif viloyat == "Jizzax":
        region = Jizzax
    elif viloyat == "Xorazm":
        region = Xorazm
    elif viloyat == "Navoiy":
        region = Navoiy
    elif viloyat == "Buxoro":
        region = Buxoro
    elif viloyat == "Sirdaryo":
        region = Sirdaryo
    elif viloyat == "Qoraqalpogiston":
        region = Qoraqalpogiston

    if region:
        return create_tumanlar_keyboard(region)
