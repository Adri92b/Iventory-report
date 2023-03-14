from inventory_report.reports.simple_report import SimpleReport


def products_for_company(list):
    company_list = {}
    for products in list:
        if products["nome_da_empresa"] not in company_list:
            company_list[products["nome_da_empresa"]] = 1
        else:
            company_list[products["nome_da_empresa"]] += 1
    list_products = ""
    company = company_list.items()
    for prod in company:
        list_products += f"- {prod[0]}: {prod[1]}\n"

    return list_products


class CompleteReport:
    @staticmethod
    def generate(list):
        return (
            f"{SimpleReport.generate(list)}\n"
            "Produtos estocados por empresa:\n"
            f"{products_for_company(list)}"
        )
