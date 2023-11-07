import balloons
import pytest


def test_sword_balloon():
    assert issubclass(balloons.SwordBalloon, balloons.Balloon)
    assert balloons.SwordBalloon.pump is balloons.Balloon.pump
    assert balloons.SwordBalloon.release is balloons.Balloon.release

    sword = balloons.SwordBalloon()
    assert sword.capacity == 5
    assert sword.amount == 0

    sword.pump()
    assert sword.capacity == 5
    assert sword.amount == 3

    with pytest.raises(balloons.BalloonTooFull):
        sword.pump()

    sword = balloons.SwordBalloon()
    assert sword.capacity == 5
    assert sword.amount == 0

    sword.pump()
    assert sword.capacity == 5
    assert sword.amount == 3

    sword.release()
    assert sword.capacity == 5
    assert sword.amount == 1

    sword.pump()
    assert sword.capacity == 5
    assert sword.amount == 4

    with pytest.raises(balloons.BalloonTooFull):
        sword.pump()


def test_dog_balloon():
    assert issubclass(balloons.DogBalloon, balloons.Balloon)
    assert balloons.DogBalloon.pump is balloons.Balloon.pump
    assert balloons.DogBalloon.release is balloons.Balloon.release

    dog = balloons.DogBalloon()
    assert dog.capacity == 7
    assert dog.amount == 0


def test_triforce_balloon():
    assert issubclass(balloons.TriforceBalloon, balloons.Balloon)
    assert balloons.TriforceBalloon.pump is balloons.Balloon.pump
    assert balloons.TriforceBalloon.release is balloons.Balloon.release

    triforce = balloons.TriforceBalloon()
    assert triforce.capacity == 11
    assert triforce.amount == 0

