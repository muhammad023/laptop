from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=
    [
   
        [
            KeyboardButton(text="Game Laptop"),
            KeyboardButton(text="office Laptop"),
        
        ],
      
],
resize_keyboard=True
)
laptop_menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="acer"),
          
        ],
        [
            KeyboardButton(text="Lenovo"),
            KeyboardButton(text="victus"),
        
        ],
        [
            KeyboardButton(text="HP"),
            KeyboardButton(text="asus"),
            KeyboardButton(text="dell"),

        ],
        [
            KeyboardButton(text="⬅go back")
        ]
],
resize_keyboard=True
)
office_laptop = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="lenovo"),
            KeyboardButton(text="mackbok")

        ],
          [
            KeyboardButton(text="Asus"),
            KeyboardButton(text="hp")

        ],
        [
        KeyboardButton(text="⬅go back")
        ]
    ],
    resize_keyboard=True
)

