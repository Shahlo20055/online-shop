# online-shop — Internet Shop

Mahsulotlar katalogi, savatcha, buyurtma, mijozlar va to'lov holatini boshqaruvchi web tizim.
«Loyihalarni boshqarish» fanidan laboratoriya loyihasi (2-mavzu).

## Maqsad
Kichik do'kon buyurtmalarini Telegram va daftar o'rniga yagona tizimda qabul qilish: xaridor mahsulotni topib buyurtma beradi, menejer buyurtmani qayta ishlaydi, administrator to'lov holatini kuzatadi. Batafsil — [loyiha xartiyasi](docs/project-charter.md).

## Imkoniyatlar (MVP)
- Katalog: turkum, narx va nom bo'yicha qidiruv va filtr
- Savatcha va buyurtma berish
- Buyurtma holati: qabul qilindi → yig'ilmoqda → yo'lda → yetkazildi
- Menejer paneli: mahsulot, narx va qoldiq
- To'lov holati: kutilmoqda / to'landi / qaytarildi

## O'rnatish
```bash
git clone https://github.com/Shahlo20055/online-shop.git
cd online-shop
python -m venv venv
venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
pip install -r requirements-dev.txt
```

## Foydalanish
```bash
python -m pytest -q          # testlarni ishga tushirish
```
Web ilova MVP bosqichida qo'shiladi (rejaga ko'ra 29.12.2026 gacha).

## Jamoa
| Ism | Rol |
|---|---|
| Baxtiyorova Shahlo (Masofaviy KIDT-236) | Loyiha menejeri, dasturchi, tester |
| Shixnazar Xusainov | Ilmiy rahbar (o'qituvchi) |

## Vazifalar
Ishlar [GitHub Issues](https://github.com/Shahlo20055/online-shop/issues) orqali yuritiladi.

## Litsenziya
MIT
