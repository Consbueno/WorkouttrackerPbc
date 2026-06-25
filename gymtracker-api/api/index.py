import sys
import os

# Garante que o diretório raiz do backend está no path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Vercel procura a variável 'app' (WSGI) neste arquivo
app = create_app()
