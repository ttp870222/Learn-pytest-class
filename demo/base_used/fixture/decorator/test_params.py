import pytest


@pytest.fixture(params=["www.baidu.com", "www.bing.com"], ids=["baidu", "bing"])
def urls(request):
    return request.param


def test_url(urls):
    url = urls
    print(f"visit - > http://{url}")


def idfn(fixture_value):
    """自定义 ids"""
    if fixture_value == "tomato":
        return "vegetable"
    else:
        return "fruits"


@pytest.fixture(params=["watermelon", "tomato"], ids=idfn)
def garden_stuff(request):
    return request.param


def test_garden_stuff(garden_stuff):
    print(f"I like to eat: {garden_stuff}")
