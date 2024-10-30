#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.2'
__author__ = 'Neviim'

import os
from flask import Flask, render_template, request, flash


app = Flask(__name__)


### defini as rotas

@app.route("/", methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/resultado_mensal')
def resultado_mensal():
  return render_template('resultado_mensal.html')



### defini as rotas

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


# servidor do render

