import random
import time

from flask import Flask, render_template
import prometheus_client as prom
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online",
					"Número de usuários online no momento")

## Funcao de simulacao de latencia e afins
def simula_latencia():
    time.sleep(random.randint(1, 10))
    quantidade_usuarios_online.set(random.randint(1, 100))

## Renda Fixa
@app.route('/renda-fixa')
def renda_fixa():
    simula_latencia()
    return render_template('lista.html', titulo='Renda Fixa')

## Renda Variavel
@app.route('/renda-variavel')
def renda_variavel():
    simula_latencia()
    return render_template('lista.html', titulo='Renda Variável')

## Criptomoedas
@app.route('/cripto')
def cripto():
    simula_latencia()
    return render_template('lista.html', titulo='Criptomoedas')

## Fundos Imobiliarios
@app.route('/fii')
def fii():
    simula_latencia()
    return render_template('lista.html', titulo='Fundos Imobiliários')

if __name__ == "__main__":
    app.run(host="0.0.0.0")