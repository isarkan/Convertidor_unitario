from flask import Flask, render_template, request

convertidor = Flask(__name__)

# =========================
# FACTORES DE CONVERSIÓN
# =========================
longitud = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34
}

peso = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
    "lb": 453.592
}


def convertir_generico(valor, de, a, tabla):
    en_base = valor * tabla[de]
    return en_base / tabla[a]


@convertidor.route("/", methods=["GET", "POST"])
def longitud_page():
    resultado = None
    if request.method == "POST":
        valor = float(request.form["valor"])
        de = request.form["de"]
        a = request.form["a"]
        resultado = convertir_generico(valor, de, a, longitud)
    return render_template("longitud.html", resultado=resultado)


@convertidor.route("/peso", methods=["GET", "POST"])
def peso_page():
    resultado = None
    if request.method == "POST":
        valor = float(request.form["valor"])
        de = request.form["de"]
        a = request.form["a"]
        resultado = convertir_generico(valor, de, a, peso)
    return render_template("peso.html", resultado=resultado)


@convertidor.route("/temperatura", methods=["GET", "POST"])
def temperatura_page():
    resultado = None
    if request.method == "POST":
        valor = float(request.form["valor"])
        de = request.form["de"]
        a = request.form["a"]

        if de == "C" and a == "F":
            resultado = (valor * 9/5) + 32
        elif de == "F" and a == "C":
            resultado = (valor - 32) * 5/9
        elif de == "C" and a == "K":
            resultado = valor + 273.15
        elif de == "K" and a == "C":
            resultado = valor - 273.15
        elif de == "F" and a == "K":
            resultado = (valor - 32) * 5/9 + 273.15
        elif de == "K" and a == "F":
            resultado = (valor - 273.15) * 9/5 + 32
        else:
            resultado = valor

    return render_template("temperatura.html", resultado=resultado)


if __name__ == "__main__":
    convertidor.run(debug=True)