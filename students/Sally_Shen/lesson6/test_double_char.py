from double_char import double_char

def test_THE():
    assert "TTHHEE" == double_char("THE")

def test_AAbb():
    assert "AAAAbbbb" == double_char("AAbb")

def test_HiThere():
    assert "HHii--TThheerree" == double_char("Hi-There")
