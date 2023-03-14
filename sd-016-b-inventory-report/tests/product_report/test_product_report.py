from inventory_report.inventory.product import Product


def test_relatorio_produto():
    testProduct = Product(
        '3',
        'chocolate',
        'Adriana',
        '06-09-2020',
        '17-09-2023',
        '1',
        'dentro da geladeira'
    )

    assert repr(testProduct) == (
        'O produto chocolate '
        'fabricado em 06-09-2020 '
        'por Adriana '
        'com validade até 17-09-2023 '
        'precisa ser armazenado dentro da geladeira.'
    )
