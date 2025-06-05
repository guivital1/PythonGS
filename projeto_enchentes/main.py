import math
import matplotlib.pyplot as plt

def f(t):
    "Função da vazão de água: f(t) = 500 * e(0.1 *t) * sin(0.5 * t)"
    return 500 * math.exp(0.1 * t) * math.sin(0.5 * t)

def derivada_aproximada(f, t, h=0.1):
    "Aproximação da derivada com diferença central"
    return (f(t + h) - f(t - h)) / (2 * h)

def integral_trapezio(f, a, b, n=1000):
    "Integral pelo método dos trapézios"
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        soma += f(a + i * h)
    return soma * h

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

def main():
    print("=== SISTEMA DE MONITORAMENTO DE ENCHENTES ===\n")
    
    # Pergunta ao responsável o limite de volume
    try:
        limite_volume = float(input("Informe o limite de volume de segurança (em litros): "))
    except ValueError:
        print("Valor inválido! Usando limite padrão de 10000 litros.")
        limite_volume = 10000

    # 1. Mostrar gráfico
    print("Gerando gráfico da vazão...")
    gerar_grafico_vazao()

    # 2. Derivada aproximada em t = 10
    derivada = derivada_aproximada(f, 10)
    print(f"\n[INFO] Derivada f'(10): {derivada:.2f} L/min²")

    # 3. Integral entre t = 0 e 20
    volume = integral_trapezio(f, 0, 20)
    print(f"[INFO] Volume total acumulado entre 0 e 20 min: {volume:.2f} litros")

  
    with open("alerta.txt", "w", encoding="utf-8") as file:
        if volume > limite_volume:
            msg = "🚨 ALERTA CRÍTICO: RISCO DE ENCHENTE DETECTADO!"
        else:
            msg = "✅ Situação sob controle. Nenhum risco de enchente."
        file.write(msg)
        print(f"\n[ALERTA] {msg}")

if __name__ == "__main__":
    main()