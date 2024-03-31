from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

uzbekistan_viloyatlar = InlineKeyboardMarkup(row_width=3)

uzbekistan_viloyatlar.add(
    InlineKeyboardButton("Toshkent", callback_data="Toshkent"),
    InlineKeyboardButton("Samarqand", callback_data="Samarqand"),
    InlineKeyboardButton("Namangan", callback_data="Namangan"),
    InlineKeyboardButton("Andijon", callback_data="Andijon"),
    InlineKeyboardButton("Farg'ona", callback_data="Fargona"),
    InlineKeyboardButton("Qashqadaryo", callback_data="Qashqadaryo"),
    InlineKeyboardButton("Surxondaryo", callback_data="Surxondaryo"),
    InlineKeyboardButton("Jizzax", callback_data="Jizzax"),
    InlineKeyboardButton("Xorazm", callback_data="Xorazm"),
    InlineKeyboardButton("Navoiy", callback_data="Navoiy"),
    InlineKeyboardButton("Buxoro", callback_data="Buxoro"),
    InlineKeyboardButton("Sirdaryo", callback_data="Sirdaryo"),
    InlineKeyboardButton("Qoraqalpog'iston", callback_data="Qoraqalpogiston"),
)

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
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti tarbiyachisi", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti psixologi", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti direktori", callback_data="2"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti metodisti", callback_data="3"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti defektologi/logopedi", callback_data="4"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti musiqa rahbari", callback_data="5"),
        ],
        [
            InlineKeyboardButton(text="Maktabgacha ta’lim tashkiloti oshpazi", callback_data="6"),
        ]
    ])

response_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ XA", callback_data="yes"),
    ],
    [
        InlineKeyboardButton(text="❌ YO'Q", callback_data="no"),
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

passport_seria = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="AA", callback_data="AA"),
    ],
    [
        InlineKeyboardButton(text="AD", callback_data="AD"),
    ],

])

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = KeyboardButton(text="📞 Telefon raqamingizni yuboring", request_contact=True)
keyboard.add(button)

