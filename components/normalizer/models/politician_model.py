class PoliticianModel:
    def __init__(self, first_name, last_name, functions, declaration_type, investments, assets, vehicles, debts, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.functions = functions
        self.declaration_type = declaration_type
        self.assets = assets
        self.vehicles = vehicles
        self.investments = investments
        self.debts = debts
        self.salary = salary
        self.isCorrupt = 2  # 0 - not corrupt, 1 - corrupt, 2 - unclassified
