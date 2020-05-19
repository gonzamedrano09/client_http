from http.client import HTTPConnection

print("\n########## Client HTTP ##########")

# Ciclo principal
url = "."
while url != "":

    # Obtengo url
    url = input("\nIngrese la url del sitio web a obtener mediante peticiones HTTP: ")
    print()

    # Si la url es distinta de vacio intenta mostrar el sitio
    if url != "":
        try:
            # Creo conexion
            connection = HTTPConnection(url)

            # Realizo peticion
            connection.request("GET", "/")

            # Obtengo encabezados y cuerpo de respuesta
            response = connection.getresponse()
            headers = "HTTP/1.0" if response.version == 10 else "HTTP/1.1" \
                      + " "  + str(response.status) \
                      + " "  + str(response.reason) \
                      + "\n"
            for x in response.getheaders():
                headers += x[0] + ": " + x[1] + "\n"
            body = response.read().decode()

            # Muestro respuesta por consola
            print("HEADERS")
            print(headers)
            print()
            print("BODY")
            print(body)

            # Cierro conexion
            connection.close()

        except Exception as ex:
            print("Se encontro el siguiente problema al obtener el sitio")
            print("########################################")
            print(ex)
            print("########################################")

print("Fin del programa")
