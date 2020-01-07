import calc

def test_add():
    if calc.add(5, 7) == 12:
        print("Test add(a, b) is OK")
    else:
        print("Test add(a, b) is Fail")

def test_sub():
    if calc.sub(5, 2) == 3:
        print("Test sub(a, b) is OK")
    else:
        print("Test sub(a, b) is Fail")

def test_mul():
    if calc.mul(4, 4) == 16:
        print("Test mul(a, b) is OK")
    else:
        print("Test mul(a, b) is Fail")

def test_div():
    if calc.div(16, 4) == 4:
        print("Test div(a, b) is OK")
    else:
        print("Test div(a, b) is Fail")

def test_exp():
    if calc.exp(7, 3) == 343:
        print("Test exp(a, b) is OK")
    else:
        print("Test exp(a, b) is Fail")

test_add()
test_sub()
test_mul()
test_div()
test_exp()