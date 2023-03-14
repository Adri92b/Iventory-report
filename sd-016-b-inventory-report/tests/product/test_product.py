from inventory_report.inventory.product import Product


def test_cria_produto():
    products = Product(
        10,
        'Vestido',
        'Florir',
        2021,
        2022,
        7,
        'Longe das amigas!'
    )

    assert products.id == 10
    assert products.nome_do_produto == 'Vestido'
    assert products.nome_da_empresa == 'Florir'
    assert products.data_de_fabricacao == '2021'
    assert products.data_de_validade == '2022'
    assert products.numero_de_serie == 7
    assert products.instrucoes_de_armazenamento == 'Longe das amigas!'
