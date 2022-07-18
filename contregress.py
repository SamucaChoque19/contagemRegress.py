import time

def contagem(quant_tempo):
        while quant_tempo:
            m, s = divmod(quant_tempo, 60)
            min_tempo ='{:02d}:{:02d}'.format(m, s)
            print(min_tempo, end = '\r')
            time.sleep(1)
            quant_tempo -= 1    
        print("BUMM!!!")
        
inp = int (input("Iniciando contagem regressiva: "))

contagem(inp)