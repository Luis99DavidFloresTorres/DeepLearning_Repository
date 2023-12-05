from flask import Flask
import joblib
import numpy as np
app = Flask(__name__)
modelo_cargado = joblib.load('modelo_entrenado3.pkl')
import json

with open('frecuencia.json', 'r') as archivo_json:
    frecuencia = json.load(archivo_json)
inverso_frecuencia = {v: k for k, v in frecuencia.items()}
max_edad =81
min_edad=20
max_monto=4200
min_monto=0
max_costo_programa =25750
min_costo_programa =0
max_dep_inicial =0
min_dep_inicial=100
max_tiempoTitulacion=0
min_tiempoTitulacion=60
def codigoPais(vector):
    dic = {0: 'AR', 1: 'BO',2:'LATE',3:'PE'}
    cont = 0
    for i in vector:
        if i > 0.5:
            break
        cont = cont + 1
    return dic[cont]
def sexoDecodificar(vector):
    dic = {0:'F',1:'M'}
    cont = 0
    for i in vector:
        if i >0.5:
            break
        cont=cont+1
    return dic[cont]
def estadoCivil(vector):
    dic = {0:'C',1:'O',2:'S'}
    cont = 0

    for i in vector:
        if i >0.5:
            break
        cont=cont+1
    return dic[cont]
def codigoDepartamento(vector):
    dic = {0:'CH',1:'CO',2:'LP',3:'OR',4:'OTHER',5:'PO',6:'SC'}
    cont = 0
    mayor = vector[0]
    boleano = False
    indiceBoleano = 0
    for i in vector:
        if mayor < i:
            mayor = i
            print(mayor)

            indiceBoleano = cont
            print('-',indiceBoleano)
        if i > 0.5:
            boleano = True
            break
        cont=cont+1
    if boleano:
        return dic[cont+1]
    return dic[indiceBoleano]
def desnormalizar(x_norm,max_x,min_x):
    return round(x_norm*(max_x-min_x)+min_x)
def normalizar(x_norm,max_x,min_x):
    return (x_norm-min_x)/(max_x- min_x)
def iniciales_nombre(vector,valorTrue):
    size = 6
    valor = np.zeros(size)
    valor[valorTrue-1]=1
    return np.concatenate((vector,valor))
def areas(vector,valorTrue):
    size = 5
    valor = np.zeros(size)
    valor[valorTrue-1]=1
    return np.concatenate((vector,valor))
def input(monto_tutoria,costo_programa,dep_inicial,sigla, inicial_nombre_index, area):
    #inpModel = np.array((monto_tutoria,costo_programa,dep_inicial,sigla))
    inpModel = np.array((0.535714,0.582524,0.10,0.000415))
    inpModel = iniciales_nombre(inpModel,inicial_nombre_index)
    inpModel= areas(inpModel, area)
    return inpModel

@app.route('/')
def predict():  # put application's code here
    monto =300
    costo =1100
    dep_in =20
    sigla ='MES'
    inicial_n_idx =5
    area_idx=4
    inp = input(normalizar(monto,max_monto,min_monto),normalizar(costo,max_costo_programa,min_costo_programa)
                ,normalizar(dep_in,max_dep_inicial,min_dep_inicial),frecuencia[sigla],
                inicial_n_idx,area_idx)
    print(inp)
    output = modelo_cargado.predict(np.array([inp]).astype('float32'))
    print('output: ')
    print(output)
    edad = desnormalizar(output[0][0],max_edad,min_edad)
    print(edad)
    tiempo_titulacion = desnormalizar(output[0][1],max_tiempoTitulacion,min_tiempoTitulacion)
    sexo = sexoDecodificar(output[0][2:4])
    estado_civilO = estadoCivil(output[0][4:7])
    codigoDepartamentoO = codigoDepartamento(output[0][7:14])
    codigoPaisO = codigoPais(output[0][14:18])
    outp= str(edad)+'\n'+str(tiempo_titulacion)+'\n'+sexo+'\n'+estado_civilO+'\n'+codigoDepartamentoO+'\n'+codigoPaisO
    print(outp)
    return outp


if __name__ == '__main__':
    app.run()
