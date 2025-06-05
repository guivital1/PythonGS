import matplotlib.pyplot as plt
from funcoes import f

def gerar_grafico_vazao():
    t_vals = [i * 0.1 for i in range(100)]
    f_vals = [f(t) for t in t_vals]
    
    plt.figure(figsize=(10,5))
    plt.plot(t_vals, f_vals, color='blue', label='Vazão de Água f(t)')
    plt.title("Vazão da Bacia de Contenção")
    plt.xlabel("Tempo (min)")
    plt.ylabel("Vazão (L/min)")
    plt.grid(True)
    plt.legend()
    plt.savefig("grafico_vazao.png")
    plt.show()