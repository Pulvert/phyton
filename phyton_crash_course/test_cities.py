from city_functions import location

def test_city_country():
    formatted_location = location("Santiago","Chile")
    assert formatted_location == "Santiago, Chile"