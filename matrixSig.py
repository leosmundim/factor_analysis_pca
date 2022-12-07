from scipy.stats import pearsonr
import pandas as pd

#Função que cria Matriz de Significância
def matrixSig (matriz_corr, df):
    matriz_sig = [[0]*len(matriz_corr) for i in range(len(matriz_corr))]
    for l in range(len(matriz_corr)):
        for c in range(len(matriz_corr.columns)):
            materia_l = matriz_corr.index[l]
            materia_c = matriz_corr.index[c]

            if materia_l == materia_c:
                matriz_sig[l][c] = 'NA'

            else:     
                stat, p_value = pearsonr(df[materia_l], df[materia_c])
                matriz_sig[l][c] = round(p_value,5)
                
    #Transforma o array em DataFrame
    matriz_sig = pd.DataFrame(matriz_sig)

    #Renomeia as colunas e o índice
    matriz_sig.columns = matriz_corr.index.get_level_values(0).values
    matriz_sig = matriz_sig.set_index(matriz_corr.index.get_level_values(0).values)
    
    return matriz_sig