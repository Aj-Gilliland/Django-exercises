from counting_machine import CountingMachine


def test_counting_machine():
    counter1 = CountingMachine()
    counter2 = CountingMachine()
    counter3 = CountingMachine()

    assert counter1.count == 0
    assert counter2.count == 0
    assert counter3.count == 0

    counter1.inc()
    counter2.inc() 
    counter3.inc()

    assert counter1.count == 1
    assert counter2.count == 1
    assert counter3.count == 1

    counter1.inc()

    assert counter1.count == 2
    assert counter2.count == 1
    assert counter3.count == 1

    counter2.dec()

    assert counter1.count == 2
    assert counter2.count == 0
    assert counter3.count == 1

    counter3.inc()

    assert counter1.count == 2
    assert counter2.count == 0
    assert counter3.count == 2

    for _ in range(5):
        counter1.dec()
        counter2.dec()
        counter3.dec()

    assert counter1.count == -3
    assert counter2.count == -5
    assert counter3.count == -3

    for _ in range(10):
        counter1.inc()
        counter2.inc()
        counter3.inc()

    assert counter1.count == 7
    assert counter2.count == 5
    assert counter3.count == 7
