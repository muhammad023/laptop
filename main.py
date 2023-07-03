import logging

from aiogram import Bot, Dispatcher, executor, types
from button import bosh_menu,laptop_menu,office_laptop

API_TOKEN = '6282307778:AAEu6w2_RoXK0WyP1aRKjyyWitxqcE64lTc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('''Hello welcome to the LAPTOP FOR GAMERS bot
                            choose one of the buttons''',reply_markup=bosh_menu)

@dp.message_handler(text="Game Laptop")
async def echo(message: types.Message):
    await message.answer("this are gamers Laptop",reply_markup=laptop_menu)

@dp.message_handler(text="acer")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/ch9om6125ku4lq0objvg/original.jpg,
    Кратко о товаре:
Процессор - AMD Ryzen 5 5500U (2.1 - 4.0 ГГц) Шестиядерный
Оперативная память - 8 ГБ DDR4 3200МГц
Видеокарта - Nvidia GeForce GTX 1650 4 ГБ 128Bit GDDR5
Разъемы и порты ввода-вывода - 1 x USB 2.0 (Type-A),2 x USB 3.1\3.2 Gen 1 (Type-A),1 х USB 3.2 Gen 1 (Type-C),1 x HDMI,1 x 3.5 mm Headphone-Microphone Jack,RJ-45
Объем накопителя - 512ГБ NVMe PCIe M.2 Gen 3.0x
Экран - Full HD (1920x1080) Тип экрана IPS Частота обновления экрана 60 Гц
Подсветка клавиатуры - Есть / Web-камера - Есть
Батарея - 48 Вт⋅ч
Беспроводная связь - Wi-Fi 6 (802.11ax) / Bluetooth 5.0
Материал корпуса - Алюминий + Пластик''')


@dp.message_handler(text="Lenovo")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/cguv7nr57mg9720fcutg/original.jpg,
    Protsessor: Intel i7-12700H 2.3G protsessor
Storage: 512GB(SSD)
RAM: 8GB
Battery: 4 CELL
Display: 15.6" FHD
GPU: RTX
Color: CLACIER_White''')


@dp.message_handler(text="victus")
async def echo(message: types.Message):
    await message.answer('''https://olcha.uz/image/700x700/products/2022-12-22/noutbuk-hp-victus-15-fa0051tx-i5-12450h-8256-gb-ssd-rtx-3050-156-fhd-184613-0.jpeg,
    Количество ядер процессора
8 ядер
Процессор
i5-12450H
Видеокарта
NVIDIA GeForce RTX 3050
Яркость
250 нит
Техпроцесс
7 nm
Количество потоков
12
Частота процессора
2.00 GHz
Оперативная память
8 ГБ
Антибликовое покрытие
есть
Тип
игровой ноутбук
Общий объем накопителей
256GB SSD
Частота обновления экрана
144 Hz
Объем видеопамяти
4 GB
Тип матрицы экрана
IPS
Вес
2.3 кг
Веб-камера
Есть
Экран
15.6" Full HD (1920x1080)''')


@dp.message_handler(text="HP")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/ch3qpdfhj8j9g69eetfg/original.jpg,
    Процессор: Core i5-11300H
Видеокарта: RTX 3050
Экран: 17' 1920 * 1080 144 Гц
ОЗУ: 8 гб DDR4
SSD: 512 гб''')

@dp.message_handler(text="asus")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/ch9l4fvhj8j9aj19a1f0/original.jpg,
    Процессор - Intel® Core™ i7-1165G7 2,8 ГГц (кэш 12 МБ, до 4,7 ГГц, 4 ядра)
Графика - Intel Iris Xᵉ Graphics
Оперативная Память - 16 ГБ DDR4 3200МГц на борту
Хранилище - 512 ГБ Твердотельный накопитель M.2 NVMe™ PCIe® 3.0
Порты ввода/вывода - 1x USB 2.0 Type-A 1x USB 3.2 Gen 1 Type-C с поддержкой дисплея/подачи питания 2x USB 3.2 Gen 2 Type-A 1x Thunderbolt™ 4, совместимый с USB4, 1x HDMI 1.4 1x 3,5-мм комбинированный аудиоразъем 1x RJ45 Gigabit Ethernet
Слоты расширения - 1x слот DDR4 SO-DIMM 1x M.2 2280 PCIe 3.0x2 1x стандартный 2,5-дюймовый жесткий диск SATA
Камера - HD-камера 720p С защитной шторкой
Аудио - Встроенный динамик Встроенный массив микрофонов с поддержкой Cortana
Сеть и связь - Wi-Fi 6 (802.11ax) (двухдиапазонный) 2*2 + беспроводная карта Bluetooth® 5.2
Экран - FHD (1920 * 1080) 16:9 , Широкий угол обзора, дисплей с антибликовым покрытием, светодиодной подсветкой, 250 нит, NTSC: 45 %, соотношение площади экрана к корпусу: 90 % дисплей ''')

@dp.message_handler(text="dell")
async def echo(message: types.Message):
    await message.answer('''https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/g-series/g15-5520/media-gallery/g15-5520-bk-coralkb/notebook-g-15-5520-gallery-1.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=457&qlt=100,1&resMode=sharp2&size=457,402&chrss=full,
    Количество ядер процессора
8 ядер
Экран
15.6" Full HD (1920x1080)
Вес
2.39 kg
Тип матрицы экрана
IPS
Объем видеопамяти
8 GB
Общий объем накопителей
1 TB SSD
Тип
игровой ноутбук
Видеокарта
GeForce RTX 3070
Тип памяти
DDR4
Частота памяти
3200 МГц
Количество потоков
16
Оперативная память
32 ГБ
Частота процессора
2.3 GHz
Процессор
Intel Core i7-11800H
Веб-камера
720p HD''')

@dp.message_handler(text="office Laptop")
async def echo(message: types.Message):
    await message.answer("this are office Laptop",reply_markup=office_laptop)

@dp.message_handler(text="lenovo")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/chq9qh3ltlh4bk4kidrg/original.jpg,
    Диагональ экрана, дюймы 15.6 IPS
Разрешение экрана: 1920x1080
Макс. частота обновления, Гц 60
Тип видеокарты: Встроенная
Интерфейсы и разъемы: USB 3.2, USB Type-C, HDMI, 3.5 мм
Видеокарта Intel UHD Graphics
Нет операционной системы
Процессор: Intel Core i3-1115G4 (3.0 ГГц)
Число ядер процессора: 2''')
    
@dp.message_handler(text="Asus")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/ci6qmnt6sfhndlbog7h0/original.jpg,
    Процессор: Intel Core i3-10110
Оперативная память: 4GB DDR4
Хранилище: 1TB HDD
ОС: Windows 11
Intel UHD Graphics
Дисплей: FHD 15.6 LED''')
    
@dp.message_handler(text="mackbok")
async def echo(message: types.Message):
    await message.answer('''https://olcha.uz/image/original/products/2021-01-28/apple-macbook-air-13-m1-8gb256gb-2020-20979-0.jpeg,
 Процессор
M1 Apple SoC
Датчик Touch ID
Есть
ОЗУ
8GB
Общий объем накопителей
256GB SSD
Вес
1.29 кг
Веб-камера
HD‑камера FaceTime 720p
Разрешение дисплея
2560x1600
Установленная ОС
macOS
Количество ядер процессора
8 ядер
Видеокарта
встроенная, Apple graphics 7-core
Диагональ дисплея
13.3"
Цвет
Gold
Цвет
Space Gray
Цвет
Silver
Подсветка клавиатуры
Есть
Отпечаток пальца
Есть
Жесткий диск
256GB SSD''')

@dp.message_handler(text="hp")
async def echo(message: types.Message):
    await message.answer('''https://images.uzum.uz/ch9qpe16i6dim8r6su5g/original.jpg,
Гарантия: 12 месяцев
RAM: 4 GB
ROM: 256 GB
Материал корпуса: пластик/ алюминий
Работа от аккумулятора: до 9 часов
Процессор: Intel Core i3-1215U
Диагональ/разрешение: 15.6"/1920x1080 пиксБез операционной системы
Без операционной системы''')

@dp.message_handler(text="⬅go back")
async def echo(message: types.Message):
    await message.answer(".",reply_markup=bosh_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)