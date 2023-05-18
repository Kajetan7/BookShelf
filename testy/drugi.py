from datetime import datetime
from random import randint

from env.bin import pytest


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0

    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1

    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo

    if validate == 10:
        validate = 0

    gender = "male" if int(pesel[-2]) % 2 == 0 else "female"
    month = int(pesel[2:4])
    years = {
        0: '19',
        1: '20',
        2: '21',
        3: '22',
        4: '18'
    }
    year = int(years[month // 20] + pesel[0:2])
    month = month % 20
    birth_date = datetime(year, month, int(pesel[4:6]))

    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
            }

    return result


def test_if_pesel_field_ok_001():
    pesel = '50090349358'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


def test_if_pesel_field_ok_002():
    pesel = '05312931815'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


def test_if_pesel_field_ok_003():
    pesel = '78031873698'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


def test_if_pesel_field_ok_004():
    pesel = '56060995862'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


def test_if_pesel_field_ok_005():
    pesel = '75122199363'
    result = analyze_pesel(pesel)
    assert result['pesel'] == pesel


def test_if_validate_ok_001():
    pesel = '56032278612'
    result = analyze_pesel(pesel)
    assert result['valid'] is True


def test_if_validate_ok_002():
    pesel = '56032278712'
    result = analyze_pesel(pesel)
    assert result['valid'] is False


def test_if_validate_ok_003():
    pesel = '00291584144'
    result = analyze_pesel(pesel)
    assert result['valid'] is True


def test_if_validate_ok_004():
    pesel = '00291584134'
    result = analyze_pesel(pesel)
    assert result['valid'] is False


def test_if_validate_ok_005():
    pesel = '85122177371'
    result = analyze_pesel(pesel)
    assert result['valid'] is True


def test_if_gender_ok_001():
    pesel = '90101547878'
    result = analyze_pesel(pesel)
    gender = "male"
    assert result['gender'] == gender


def test_if_gender_ok_002():
    pesel = '61102184434'
    result = analyze_pesel(pesel)
    gender = "male"
    assert result['gender'] == gender


def test_if_gender_ok_003():
    pesel = '05230663649'
    result = analyze_pesel(pesel)
    gender = "female"
    assert result['gender'] == gender


def test_if_gender_ok_004():
    pesel = '02281237762'
    result = analyze_pesel(pesel)
    gender = "female"
    assert result['gender'] == gender


def test_if_birth_date_ok_001():
    pesel = '05230663649'
    result = analyze_pesel(pesel)
    assert result['birth_date'] == datetime(year=2005, month=3, day=6)


@pytest.mark.parametrize("pesel, result",
                         [
                             ('03302653459', True),
                             ('61080875438', True),
                             ('78081172959', False)
                         ])

