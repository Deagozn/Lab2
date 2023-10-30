import Lab2
def test_find_min_max():
    result = []
    input_arr = [1,25,35,50]
    test_arr = [1, 50]

    result = Lab2.find_min_max(input_arr)

    assert(result == test_arr)

def test_calc_average():
    result = []
    input_arr = [2, 4, 6, 8]
    test_value = 5

    result = Lab2.calc_average(input_arr)

    assert(result == test_value)

def test_calc_median_temperature_odd():
    result = []
    input_arr = [2, 4, 6, 8, 10]
    test_value = 6

    result = Lab2.calc_median_temperature(input_arr)

    assert(result == test_value)

def test_calc_median_temperature_even():
    result = []
    input_arr = [2, 4, 6, 8]
    test_value = 5

    result = Lab2.calc_median_temperature(input_arr)

    assert(result == test_value)
