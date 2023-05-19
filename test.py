import requests

url = 'https://test-fastapi-tigrehacks.azurewebsites.net/predict'
image_path = 'api/IMG_0009.JPG'  # Ruta de la imagen que deseas enviar

with open(image_path, 'rb') as file:
    response = requests.post(url, files={'file': file})

print(response)
prediction = response.json()
if 'cat' in prediction.values():
    print(f"En la imagen hay un {prediction['prediction']} :D")
else:
    print("No hay un gato :(")