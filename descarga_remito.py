import requests
import time
import json
from getpass import getuser
from autenticarse import loguearse

def descarga_remitos(entrega, token, ruta_descarga):
    # DEFINIMOS LA URL BASE DE LA API DE TSDOCS.
    url_base = "https://api.nosconecta.com.ar:443"

    # DECLARAMOS CABECERAS DE LA PETICION.
    headers = {'accept':'application/json', 'Authorization': token}

    # DEFINIMOS LOS PARAMETROS (datos a consultar)
    parametros = (
        ('filter', '[{"key":"entrega_id", "value":"'+ entrega +'"}]'),
    )

    response = requests.get(url = f"{url_base}/search/353", headers = headers, params = parametros, verify = False)

    id_doc = ""
    if response.status_code == 200:
        payload = response.json()
        results = payload['message']['results']
        
        if results != []:
            id_doc = results[0]["id"]
            print(f"ID TSDC: {id_doc}")

            # PASAMOS A DESCARGAR EL PDF CON EL ID OBTENIDO #
            # Realizamos la solicitud al endpoint de descarga
            response_descarga = requests.get(url = f"{url_base}/file/353/{id_doc}", headers = headers, stream = True, verify = False)

            # Verificamos el status de la solicitud
            if response_descarga.status_code == 200:
                print(f"Todo ok para descargar entrega: {entrega}, ID: {id_doc}.")

                # Creamos un pdf vacio con la ruta completa de descarga.
                nombre_pdf = entrega + ".pdf"
                with open(ruta_descarga + "/" + nombre_pdf, "wb") as pdf:
                    print("Descargando pdf...")
                    for data_file_entrega in response_descarga.iter_content():
                        pdf.write(data_file_entrega)
            else:
                print(f"Error en la solicitud de descarga. {response_descarga.text}")
        else:
            print(f"No se encontraron datos en TsDocs para la entrega: {entrega}")