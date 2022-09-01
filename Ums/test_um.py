from Ums.um import count


def test_um_in_words():
    assert count('Tummy') == 0
    assert count('album') == 0


def test_normal_um():
    assert count('Um, hello.') == 1
    assert count('Hello, um, who are you') == 1
