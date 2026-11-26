# US-07: Login va rollar — spetsifikatsiya

**Issue:** #6 · **Sprint:** Sprint 1 · **SP:** 8

## Rollar va ruxsatlar
| Rol | Ruxsat etilgan bo'limlar |
|---|---|
| admin | Barcha bo'limlar, xodimlar va rollar, to'lov sozlamalari |
| menejer | Katalog, mahsulotlar, buyurtmalar, hisobotlar |
| omborchi | Mahsulot qoldig'i, buyurtmani yig'ish |
| xaridor | Katalog, savatcha, o'z buyurtmalari |

## Login oqimi
1. Foydalanuvchi e-pochta va parolni kiritadi.
2. Server parolni xesh bilan solishtiradi (bcrypt).
3. Muvaffaqiyatli bo'lsa sessiya ochiladi va rolga mos sahifaga yo'naltiriladi.
4. 5 marta noto'g'ri urinishdan keyin hisob 15 daqiqaga bloklanadi.

## Acceptance criteria
- [ ] E-pochta noyobligi tekshiriladi, takror e-pochta rad etiladi
- [ ] Rolga mos bo'lmagan sahifaga kirishda 403 «Ruxsat yo'q» xabari chiqadi
- [ ] Parol kamida 8 belgi, xeshlangan holda saqlanadi
