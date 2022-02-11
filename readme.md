# Calculadora de dolar argentina

- Ingresas valor en pesos y te devuelve la cantidad de dolares que son
- Valor del dolar blue recibido de [dolar-blue-API](https://api-dolar-argentina.herokuapp.com/api/dolarblue)
- Valor del dolar oficial recibido de [dolar-oficial-API](https://api-dolar-argentina.herokuapp.com/api/dolaroficial)

## Instalación

```bash
git clone https://github.com/jd-apprentice/dolar-argentina.git
cd dolar-argentina
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ./src/main.py
```