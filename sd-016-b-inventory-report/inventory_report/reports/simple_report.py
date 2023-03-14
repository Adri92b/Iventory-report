from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate_fabrication(list):
        date = set()
        for fabrication in list:
            date.add(fabrication["data_de_fabricacao"])
        return min(date)

    def generate_validate(list):
        validate = set()
        atual_date = datetime.today()
        date_text = atual_date.strftime('%Y-%m-%d')

        for validate_date in list:
            if validate_date["data_de_validade"] > date_text:
                validate.add(validate_date["data_de_validade"])
        return min(validate)

    def generate_quantity(list):
        companies = [product["nome_da_empresa"] for product in list]
        company_with = max(set(companies), key=companies.count)
        return company_with

    def generate(list):
        data_fabrication = SimpleReport.generate_fabrication(list)
        validate = SimpleReport.generate_validate(list)
        empresa = SimpleReport.generate_quantity(list)
        return (
            f"Data de fabricação mais antiga: {data_fabrication}\n"
            f"Data de validade mais próxima: {validate}\n"
            f"Empresa com mais produtos: {empresa}"
        )
