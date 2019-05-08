from refactor import test_data, create_donors_report

TEST_DATA = test_data()


def test_1():
    result = create_donors_report(TEST_DATA)

    print(result)

    assert len(result) == len(TEST_DATA)
    donor = result[1]
    assert donor[-1] == donor[1] / donor[2]

    assert result[0][1] > result[-1][1]
