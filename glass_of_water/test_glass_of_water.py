from glass_of_water import Glass


def test_glass_init():
    assert Glass(2).capacity == 2
    assert Glass(5).capacity == 5
    assert Glass(123).capacity == 123

    assert Glass(2).amount == 0
    assert Glass(5).amount == 0
    assert Glass(123).amount == 0

 
def test_glass_pour_in():
    glass1 = Glass(2)
    glass2 = Glass(5)
    glass3 = Glass(123)

    glass1.pour_in(3)
    glass2.pour_in(3)
    glass3.pour_in(3)

    assert glass1.amount == 2
    assert glass2.amount == 3
    assert glass3.amount == 3

    glass1.pour_in(1)
    glass2.pour_in(1)
    glass3.pour_in(1)

    assert glass1.amount == 2
    assert glass2.amount == 4
    assert glass3.amount == 4

    glass1.pour_in(1)
    glass2.pour_in(1)
    glass3.pour_in(1)

    assert glass1.amount == 2
    assert glass2.amount == 5
    assert glass3.amount == 5

    glass1.pour_in(1)
    glass2.pour_in(1)
    glass3.pour_in(1)

    assert glass1.amount == 2
    assert glass2.amount == 5
    assert glass3.amount == 6


def test_pour_out():
    glass1 = Glass(2)
    glass2 = Glass(5)
    glass3 = Glass(123)

    glass1.amount = 2
    glass2.amount = 5
    glass3.amount = 123

    glass1.pour_out(3)
    glass2.pour_out(3)
    glass3.pour_out(3)

    assert glass1.amount == 0
    assert glass2.amount == 2
    assert glass3.amount == 120

    glass1.pour_out(1)
    glass2.pour_out(1)
    glass3.pour_out(1)     

    assert glass1.amount == 0
    assert glass2.amount == 1
    assert glass3.amount == 119

    glass1.pour_out(1)
    glass2.pour_out(1)
    glass3.pour_out(1)

    assert glass1.amount == 0
    assert glass2.amount == 0
    assert glass3.amount == 118

    glass1.pour_out(1)
    glass2.pour_out(1)
    glass3.pour_out(1)

    assert glass1.amount == 0
    assert glass2.amount == 0
    assert glass3.amount == 117

