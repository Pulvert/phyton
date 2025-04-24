class Company:
    def __init__(self, company_id, company_name, company_country):
        self.company_id = company_id
        self.company_name = company_name
        self.company_country = company_country

    def pr(self):
        print(self.company_id)
        print(self.company_name)
        print(self.company_country)


companies_list = []


# Bucle para agregar empresas
while True:
    company_name = input("Ingresa el nombre de la empresa (o 'salir' para terminar): ")
    if company_name.lower() == "salir":
        break
    company_country = input("Ingresa el país de la empresa: ")
    company_id = input("Ingresa el código la empresa: ")

    new_company = Company( company_id, company_name, company_country)  # Crear objeto de empresa
    companies_list.append(new_company)  # Agregarlo a la lista
    

print("\nEmpresas registradas:")
for b in companies_list:
    print(b.company_name)
    print(b.company_country)











