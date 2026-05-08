# Модель: Метод Ейлера (5 семестр)
# Автор: Самсонов Віталій, група АІ-233

from fastapi import FastAPI
from typing import Optional
import numpy as np

app = FastAPI()

def euler_method(f, x0, y0, h, a, b):
    n = int((b - a) / h) + 1
    x_values = np.linspace(a, b, n)
    y_values = np.zeros(n)
    y_values[0] = y0
    for i in range(1, n):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])
    return x_values.tolist(), y_values.tolist()

def f(x, y):
    return x + np.sin(y / 3)

@app.get("/")
def root():
    return {"message": "Лабораторна робота №5: API для методу Ейлера"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Привіт, {name}!"}

@app.get("/calculate")
def calculate(x0: float = 1.6, y0: float = 4.6, a: float = 1.6, b: float = 2.6, h: float = 0.1):
    x_vals, y_vals = euler_method(f, x0, y0, h, a, b)
    return {"x": x_vals, "y": y_vals}
