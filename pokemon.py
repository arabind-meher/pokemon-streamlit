import pandas as pd

class Pokemon:
    def __init__(self) -> None:
        self.pokemon = pd.read_pickle('./pokemon.pkl')
        self.pokemon.fillna('', inplace=True)
        print(self.pokemon)
    
    def get_pokemon_from_type(self, type1: str, type2: str) -> pd.DataFrame:
        if type1 == 'Any' and type2 == 'Any':
            return self.pokemon
        elif type2 == 'Any':
            return self.pokemon.loc[self.pokemon['Type1'] == type1]
        elif type1 == 'Any':
            return self.pokemon.loc[self.pokemon['Type2'] == type2]
        else:
            return self.pokemon.loc[(self.pokemon['Type1'] == type1) & (self.pokemon['Type2'] == type2)]
