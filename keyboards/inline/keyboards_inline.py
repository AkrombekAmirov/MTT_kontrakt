from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

uzbekistan_viloyatlar = InlineKeyboardMarkup(row_width=3)

uzbekistan_viloyatlar.add(
    InlineKeyboardButton("Toshkent viloyati", callback_data="reg0"),
    InlineKeyboardButton("Toshkent shahri", callback_data="reg1"),
    InlineKeyboardButton("Samarqand", callback_data="reg2"),
    InlineKeyboardButton("Namangan", callback_data="reg3"),
    InlineKeyboardButton("Andijon", callback_data="reg4"),
    InlineKeyboardButton("Farg'ona", callback_data="reg5"),
    InlineKeyboardButton("Qashqadaryo", callback_data="reg6"),
    InlineKeyboardButton("Surxondaryo", callback_data="reg7"),
    InlineKeyboardButton("Jizzax", callback_data="reg8"),
    InlineKeyboardButton("Xorazm", callback_data="reg9"),
    InlineKeyboardButton("Navoiy", callback_data="reg10"),
    InlineKeyboardButton("Buxoro", callback_data="reg11"),
    InlineKeyboardButton("Sirdaryo", callback_data="reg12"),
    InlineKeyboardButton("Qoraqalpog'iston", callback_data="reg13"),
)
list_regioin = ["reg0", "reg1", "reg2", "reg3", "reg4", "reg5", "reg6", "reg7", "reg8", "reg9", "reg10", "reg11",
                "reg12", "reg13"]
list_region1 = ["Toshkent viloyati", "Toshkent shahri", "Samarqand viloyati", "Namangan viloyati", "Andijon viloyati",
                "Fargona viloyati", "Qashqadaryo viloyati", "Surxondaryo viloyati", "Jizzax viloyati",
                "Xorazm viloyati", "Navoiy viloyati", "Buxoro viloyati", "Sirdaryo viloyati",
                "Qoraqalpogʻiston Respublikasi"]
rasmiylashtirish = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📄 1-kurslar uchun", callback_data="1")
    ],
    [
        InlineKeyboardButton(text="📄 2-kurslar uchun", callback_data="2")
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga", callback_data="registration")
    ]
])

choose_visitor = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📄 Malaka oshirish instituti haqida malumot olish", callback_data="information"),
    ],
    [
        InlineKeyboardButton(text="📝 Ariza qoldirish", callback_data="registration"),
    ]
])

yonalish_nomi_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti tarbiyachisi 864 soatlik kurs",
                                 callback_data="faculty0"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti tarbiyachisi 576 soatlik kurs",
                                 callback_data="faculty1"),
        ],
        [
            InlineKeyboardButton(text="Defektologiya (logopediya)", callback_data="faculty2"),
        ],
        [
            InlineKeyboardButton(text="Amaliy psixologiya", callback_data="faculty3"),
        ],
    ])

response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ XA", callback_data="yes"),
    ],
    [
        InlineKeyboardButton(text="❌ YO'Q", callback_data="no"),
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu"),
    ]
])

choose_contract_ = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📝 ARIZA QOLDIRISH", callback_data="qabul_yes"),
    ],
    [
        InlineKeyboardButton(text="❌ INKOR QILISH", callback_data="inkor_no"),
    ]
])

til_shakli_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="1"),
    ],
    [
        InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="2"),
    ]
])

choose_language = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="O'zbek tili"),
    ],
    [
        InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="Rus tili"),
    ]
])

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = KeyboardButton(text="📞 Telefon raqamingizni yuboring", request_contact=True)
keyboard.add(button)
