from solution import parse, solve_1, solve_2


def test_solve_1a():
    data = parse("8A004A801A8002F478")
    result = solve_1(data)
    assert result == 16
    print("Test 1a passed!")


def test_solve_1b():
    data = parse("620080001611562C8802118E34")
    result = solve_1(data)
    assert result == 12
    print("Test 1b passed!")


def test_solve_1c():
    data = parse("C0015000016115A2E0802F182340")
    result = solve_1(data)
    assert result == 23
    print("Test 1c passed!")


def test_solve_1d():
    data = parse("A0016C880162017C3686B18A3D4780")
    result = solve_1(data)
    assert result == 31
    print("Test 1d passed!")


def test_solve_2a():
    data = parse("C200B40A82")
    result = solve_2(data)
    assert result == 3
    print("Test 2a passed!")


def test_solve_2b():
    data = parse("04005AC33890")
    result = solve_2(data)
    assert result == 54
    print("Test 2b passed!")


def test_solve_2c():
    data = parse("880086C3E88112")
    result = solve_2(data)
    assert result == 7
    print("Test 2c passed!")


def test_solve_2d():
    data = parse("CE00C43D881120")
    result = solve_2(data)
    assert result == 9
    print("Test 2d passed!")


def test_solve_2e():
    data = parse("D8005AC2A8F0")
    result = solve_2(data)
    assert result == 1
    print("Test 2e passed!")


def test_solve_2f():
    data = parse("F600BC2D8F")
    result = solve_2(data)
    assert result == 0
    print("Test 2f passed!")


def test_solve_2g():
    data = parse("9C005AC2F8F0")
    result = solve_2(data)
    assert result == 0
    print("Test 2g passed!")


def test_solve_2h():
    data = parse("9C0141080250320F1802104A08")
    result = solve_2(data)
    assert result == 1
    print("Test 2h passed!")


if __name__ == '__main__':
    test_solve_1a()
    test_solve_1b()
    test_solve_1c()
    test_solve_1d()
    test_solve_2a()
    test_solve_2b()
    test_solve_2c()
    test_solve_2d()
    test_solve_2e()
    test_solve_2f()
    test_solve_2g()
    test_solve_2h()
