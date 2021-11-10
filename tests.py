from data import get_data_from_weather_api


def test_get_data_from_weather_api():
    assert type(
        get_data_from_weather_api()) == dict, "Should be a dictionary"
    print("Data is dictionary. Test 1 passed.")


def test_response_get_data_from_weather_api():
    assert get_data_from_weather_api(mode="test") == 200, "Should be 200"
    print("Status code 200. Test 2 passed.")


if __name__ == "__main__":
    test_get_data_from_weather_api()
    test_response_get_data_from_weather_api()
    print("*******All tests passed*******")
