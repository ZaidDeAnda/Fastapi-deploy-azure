import requests

url = 'http://localhost:8000/predict'
image_path = 'foto_1.jpeg'  # Ruta de la imagen que deseas enviar

with open(image_path, 'rb') as file:
    response = requests.post(url, files={'file': file})

prediction = response.json()
if 'cat' in prediction.values():
    print(f"En la imagen hay un {prediction['prediction']} :D")
else:
    print("No hay un gato :(")