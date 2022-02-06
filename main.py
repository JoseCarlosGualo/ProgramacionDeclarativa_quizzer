import pandas as pd

def read_table(file_name):
    data = pd.read_excel(file_name)
    return data

def ask_question(enunciado, op1, op2, op3, op4):
    print(enunciado)
    opciones = [op1,op2,op3,op4]
    for i in range(0,4):
        num_qtn = i + 1
        print("\t" + str(num_qtn) + "- " + opciones[i])

def is_correct(correcta, respuesta):
    if int(correcta) == int(respuesta):
        return True
    else:
        return False

def main():
    preguntas = read_table("Preguntas\BasePreguntas_2.xlsx")
    aciertos = 0
    for i in preguntas.index:
        ask_question(preguntas['ENUNCIADO'][i],preguntas['OPC1'][i],preguntas['OPC2'][i],preguntas['OPC3'][i],preguntas['OPC4'][i])
        
        respuesta = input('INTRODUCE RESPUESTA (ENTRE 1 Y 4):')
        
        while not respuesta.isnumeric() or int(respuesta) < 1 or int(respuesta) > 4:
            print('ERROR DE FORMATO DE LA RESPUESTA')
            print('LA RESPUESTA DEBE SER UN NUMERO ENTRE EL 1 Y 4')
            respuesta = input('INTRODUCE RESPUESTA (ENTRE 1 Y 4):')
        
        if is_correct(preguntas['RESPUESTA'][i], respuesta):
            print('####CORRECTO####')
            aciertos = aciertos + 1
        else:
            print('####FALLO####')
            correcta_str = ""
            
            if int(preguntas['RESPUESTA'][i]) == 1:
                correcta_str = preguntas['OPC1'][i]
            elif int(preguntas['RESPUESTA'][i]) == 2:
                correcta_str = preguntas['OPC2'][i]
            elif int(preguntas['RESPUESTA'][i]) == 3:
                correcta_str = preguntas['OPC3'][i]
            elif int(preguntas['RESPUESTA'][i]) == 4:
                correcta_str = preguntas['OPC4'][i]
            
            print('LA RESPUESTA CORRECTA ERA: \n{}'.format(correcta_str))
                
    print('####FIN DEL CUESTIONARIO####')
    print('###RESULTADO ==> {}/{} ACIERTOS'.format(aciertos,preguntas.shape[0]))
            
if __name__ =='__main__':
    main()