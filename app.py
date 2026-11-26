"""Internet Shop: savatcha qiymatlarini tekshirish funksiyalari (5-laboratoriya)."""


def _is_int(x):
    """bool ham int ning bolasi, shuning uchun uni alohida chiqarib tashlaymiz."""
    return isinstance(x, int) and not isinstance(x, bool)


def valid_price(narx):
    """Mahsulot narxi (so'm) musbat butun son bo'lishi kerak."""
    return _is_int(narx) and narx > 0


def valid_quantity(soni, qoldiq):
    """Savatchadagi miqdor 1 dan ombordagi qoldiqgacha (qoldiq ham kiradi)."""
    return _is_int(soni) and _is_int(qoldiq) and 1 <= soni <= qoldiq


def savatcha_jami(qatorlar):
    """qatorlar: [(narx, soni, qoldiq), ...]; noto'g'ri qatorda ValueError."""
    jami = 0
    for i, (narx, soni, qoldiq) in enumerate(qatorlar, start=1):
        if not valid_price(narx):
            raise ValueError(f"{i}-qator: noto'g'ri narx {narx!r}")
        if not valid_quantity(soni, qoldiq):
            raise ValueError(f"{i}-qator: omborda faqat {qoldiq} dona bor (so'ralgan: {soni!r})")
        jami += narx * soni
    return jami
