# Loyiha xartiyasi (Project Charter) — Internet Shop

| Band | Mazmuni |
|---|---|
| Loyiha nomi | Internet Shop — onlayn do'kon boshqaruv tizimi |
| Loyiha menejeri / ijrochi | Baxtiyorova Shahlo (Masofaviy KIDT-236) |
| Buyurtmachi | Kichik chakana do'kon egasi (o'quv ssenariysi) |
| Boshlanish – tugash | 01.12.2026 – 29.12.2026 (4 hafta) |

## 1. Muammo
Do'kon buyurtmalarni Telegram, telefon va daftar orqali qabul qiladi. Natijada mahsulot qoldig'i noto'g'ri hisoblanadi, buyurtmalar yo'qoladi, to'lov holatini kuzatish qiyin.

## 2. Maqsad
Mahsulotlar katalogi, savatcha, buyurtma, mijozlar va to'lov holatini yagona web tizimda boshqarish.

**Asosiy natija:** ishlaydigan MVP — xaridor mahsulotni topib buyurtma beradi, menejer buyurtmani qayta ishlaydi, administrator to'lov holatini kuzatadi.

**O'lchanadigan mezonlar:**
- 100 ta mahsulot katalogga kiritilgan, qidiruv 2 soniyadan tez;
- buyurtma berish 3 qadamdan oshmaydi (savatcha → ma'lumotlar → tasdiqlash);
- ombor qoldig'i har bir buyurtmadan keyin avtomatik yangilanadi.

## 3. Manfaatdor tomonlar
| Tomon | Qiziqishi |
|---|---|
| Xaridor | Mahsulotni tez topish, qulay buyurtma, holatni kuzatish |
| Do'kon menejeri | Katalog va qoldiqni yuritish, buyurtmalarni qayta ishlash |
| Administrator | Xodimlar, rollar va to'lovlarni nazorat qilish |
| Do'kon egasi | Savdo hisobotlari, daromad |

## 4. Qamrov (Scope)
**Kiradi:** ro'yxatdan o'tish va login; katalog, qidiruv va filtr; savatcha; buyurtma va uning holati; mahsulot va qoldiqni boshqarish; to'lov holati (naqd / Click / Payme test rejimi); savdo hisoboti (CSV).

**Kirmaydi:** mobil ilova; yetkazib berish xizmati bilan integratsiya; real pul o'tkazmalari (faqat test rejimi); omborni shtrix-kod bilan boshqarish; ko'p tilli interfeys.

## 5. Bosqichlar (milestone)
| Hafta | Bosqich | Natija |
|---|---|---|
| 1 (01–08.12) | Talablar va dizayn | User story'lar, maketlar — **M1: dizayn tasdiqlandi** |
| 2 (09–15.12) | Backend | Katalog, savatcha va buyurtma API |
| 3 (16–22.12) | Frontend va to'lov | Sahifalar, admin panel, to'lov test rejimi |
| 4 (22–29.12) | Test va namoyish | Integratsiya, test, deploy — **M2: MVP ishga tushirildi** |

## 6. Resurslar va cheklovlar
- Jamoa: 1 kishi (o'quv loyihasi) — dasturchi, tester va menejer rollarini bajaradi.
- Texnologiyalar: Python, SQLite, HTML/CSS/JS, GitHub (versiyalash, Issues, Actions).
- Byudjet: 0 so'm (bepul vositalar); muddat qat'iy — 29.12.2026.

## 7. Asosiy xatarlar
- To'lov tizimi test kalitlarini olish kechikishi;
- mahsulot ma'lumotlari (rasm, narx) kech taqdim etilishi;
- yagona ijrochining band bo'lib qolishi.
