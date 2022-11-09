class PoliticianModel:
    def __init__(self, first_name, last_name, functions, declaration_type, region, number_of_declarations):
        self.first_name = first_name
        self.last_name = last_name
        self.functions = functions
        self.declaration_type = declaration_type
        self.region = region
        self.number_of_declaration = number_of_declarations
        self.isCorrupt = 2  # 0 - not corrupt, 1 - corrupt, 2 - unclassified
