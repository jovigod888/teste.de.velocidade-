# Importar a biblioteca speedtest
import speedtest

# Criar um objeto speedtest
st = speedtest.Speedtest()

# Obter a lista de servidores disponíveis
st.get_servers()

# Escolher o melhor servidor
st.get_best_server()

# Obter a velocidade de download em bytes
download = st.download()

# Obter a velocidade de upload em bytes
upload = st.upload()

# Obter o ping em milissegundos
ping = st.results.ping

# Converter bytes em megabytes
def bytes_to_mb(bytes):
  return round(bytes / (1024 ** 2), 2)

# Exibir os resultados na tela
print(f"Velocidade de download: {bytes_to_mb(download)} MB/s")
print(f"Velocidade de upload: {bytes_to_mb(upload)} MB/s")
print(f"Ping: {ping} ms")
