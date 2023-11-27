from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_compra', methods=['POST'])
def calcular_compra():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_tarro = 9000
    total_sin_descuento = tarros * precio_tarro

    descuento = 0
    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25

    total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

    return render_template('resultado_compra.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento, descuento=descuento)


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

def verificar_credenciales(usuario, contraseña):
    usuarios_registrados = {
        'juan': 'admin',
        'pepe': 'user'
    }

    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        return True
    else:
        return False

@app.route('/verificar_credenciales', methods=['POST'])
def verificar_credenciales_route():
    usuario_ingresado = request.form['usuario']
    contraseña_ingresada = request.form['contraseña']

    if verificar_credenciales(usuario_ingresado, contraseña_ingresada):
        mensaje_bienvenida = f'Bienvenido {"administrador" if usuario_ingresado == "juan" else "usuario"} {usuario_ingresado}'
    else:
        mensaje_bienvenida = 'Credenciales incorrectas'

    return render_template('resultado_credenciales.html', mensaje_bienvenida=mensaje_bienvenida)

if __name__ == '__main__':
    app.run(debug=True)