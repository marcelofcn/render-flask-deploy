#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.1'
__author__ = 'Neviim'
__version__= '0.2'
__author__= 'MarceloF'

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def teste_servidor():
        return 'Olá Servidor, está disponivel ?'

@app.route('/servidor')
def ping():
        return 'novos testes internet'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
