import socket

print("\n########## Client Socket ##########")

# Ciclo principal
url = "."
while url != "":

    # Obtengo url
    url = input("\nIngrese la url del sitio web a obtener mediante sockets: ")
    print()

    # Si la url es distinta de vacio intenta mostrar el sitio
    if url != "":
        try:
            # Creo conexion
            st = socket.socket()
            st.connect((url, 80))

            # Realizo peticion
            request = "GET / HTTP/1.1\r\n" \
                      "Host: %s\r\n" \
                      "Accept-Languaje: es\r\n\r\n" % url
            st.send(request.encode())

            # Obtengo encabezados y cuerpo de respuesta
            response = st.recv(4096).decode()
            headers = response.split("\r\n\r\n")[0]
            body = response.split("\r\n\r\n")[1]

            # Muestro respuesta por consola
            print("HEADERS")
            print(headers)
            print("\n")
            print("BODY")
            print(body)

            # Cierro conexion
            st.close()

        except Exception as ex:
            print("Se encontro el siguiente problema al obtener el sitio")
            print("########################################")
            print(ex)
            print("########################################")

print("Fin del programa")
