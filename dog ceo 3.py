import requests

breed = input("Enter dog breed: ").strip().lower()

url = f"https://dog.ceo/api/breed/{breed}/images/random"

response = requests.get(url)

if response.status_code == 200:
    dog = response.json()
    print(dog["message"])
else:
    print("Breed not found")
