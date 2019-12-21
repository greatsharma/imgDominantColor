import requests


def test_code400():
    response = requests.get(url='https://img-dominant-color.herokuapp.com/')

    assert response.json()['status']['code'] == 404


def test_code404():
    response = requests.get(
        url='https://img-dominant-color.herokuapp.com/?src=https://imas.unsplash.com/photo-1487530811176-3780de880c2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')

    assert response.json()['status']['code'] == 404


def test_code200():
    response = requests.get(
        url='https://img-dominant-color.herokuapp.com/?src=https://images.unsplash.com/photo-1487530811176-3780de880c2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')

    assert response.json()['status']['code'] == 200


if __name__ == '__main__':
    test_code400()
    test_code404()
    test_code200()
