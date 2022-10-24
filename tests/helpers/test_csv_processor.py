from helpers.csv_processor import replace_csv


def test_replace_csv_normal_string_true():
    string_csv = 'Hola, prueba de cadena normal'
    expected_list = ['Hola, prueba de cadena normal']
    assert_msj = "Expected response ['Hola']"
    assert replace_csv(string_csv) == expected_list, assert_msj


def test_replace_csv_format_string_true():
    string_csv = 'H\x00o\x00l\x00a\x00\n'
    expected_list = ['Hola']
    assert_msj = "Expected response ['Hola']"
    assert replace_csv(string_csv) == expected_list, assert_msj


def test_replace_csv_normal_false():
    string_csv = 'Hola que hace\n como esta'
    expected_list = ['Hola que hace']
    assert_msj = "Expected response different from ['Hola que hace']"
    assert replace_csv(string_csv) != expected_list, assert_msj


def test_replace_csv_format_false():
    string_csv = 'H\x00o\x00l\x00a\x00que hace\n'
    expected_list = ['Hola']
    assert_msj = "Expected response different from ['Hola']"
    assert replace_csv(string_csv) != expected_list, assert_msj
