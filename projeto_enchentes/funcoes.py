import math

def f(t):
    """Função da vazão de água: f(t) = 500 * e^(0.1 * t) * sin(0.5 * t)"""
    return 500 * math.exp(0.1 * t) * math.sin(0.5 * t)

def derivada_aprox(f, t, h=0.01):
    """Aproximação da derivada com Diferença Central"""
    return (f(t + h) - f(t - h)) / (2 * h)

def integral_trapezio(f, a, b, n=1000):
    """Integral pelo método dos trapézios"""
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        soma += f(a + i * h)
    return soma * h
