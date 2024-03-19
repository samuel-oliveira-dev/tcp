from socket import *

portaServidor = 12000

socketServidor = socket(AF_INET, SOCK_STREAM)

socketServidor.bind(('', portaServidor))

socketServidor.listen(1)

# HTML da página que será retornada para o cliente
pagina_html = """
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Página HTML Simples</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma página HTML simples retornada pelo servidor Python.</p>
</body>
</html>
"""

print("O servidor está pronto para receber")

while True:
    socketConexao, endereco = socketServidor.accept()

    # Envia a página HTML para o cliente
    socketConexao.send(pagina_html.encode('utf-8'))

    socketConexao.close()
