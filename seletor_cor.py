class SeletorCor:


   _CORES = {
       "Preto": "black",
       "Vermelho": "red",
       "Verde": "green",
       "Azul": "blue",
       "Amarelo": "yellow",
       "Cinza": "gray",
       "Roxo": "purple",
   }
   @staticmethod
   def converter(nome):
       return SeletorCor._CORES.get(nome, "black")
