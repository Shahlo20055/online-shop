import pytest
from app import valid_price, valid_quantity, savatcha_jami


@pytest.mark.parametrize("narx, kutilgan", [
    (15000, True), (1, True),
    (0, False), (-500, False), (True, False), ("15000", False), (99.9, False),
])
def test_valid_price(narx, kutilgan):
    assert valid_price(narx) is kutilgan


def test_quantity_oddiy():
    assert valid_quantity(2, 10)


def test_quantity_butun_qoldiqni_olish():
    # US-02: xaridor ombordagi oxirgi donalarni ham sotib ola olishi kerak
    assert valid_quantity(5, 5)


def test_quantity_qoldiqdan_oshadi():
    assert not valid_quantity(6, 5)


def test_quantity_nol_va_bool():
    assert not valid_quantity(0, 5)
    assert not valid_quantity(True, 5)


def test_savatcha_jami():
    assert savatcha_jami([(15000, 2, 10), (40000, 1, 1)]) == 70000


def test_savatcha_xato_qator():
    with pytest.raises(ValueError, match="2-qator"):
        savatcha_jami([(15000, 1, 3), (40000, 4, 3)])
