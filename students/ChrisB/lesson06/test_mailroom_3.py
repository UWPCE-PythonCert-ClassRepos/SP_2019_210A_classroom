"""
tests for mailroom
"""

import mailroom_3 as mr


def test_formulate_mail():
    letter = mr.formulate_mail(("Bob Smith", [100.00, 50.00, 200.00]),
                            echo_terminal=False)

    print(letter)

    assert letter.startswith("Attn: Bob Smith")
    assert "Dear Bob Smith" in letter




