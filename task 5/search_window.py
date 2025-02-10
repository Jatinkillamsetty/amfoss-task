from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap, QImage
import requests
import sys
import os

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pokémon Search")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-image: url('landing.jpg');")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)
        self.textbox.setStyleSheet("color: white;")

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 20, 280, 20)
        label1.setStyleSheet("color: white;")

        self.enter_button = QPushButton("Search", self)
        self.enter_button.setGeometry(50, 100, 160, 43)
        self.enter_button.setStyleSheet("color: white;")
        self.enter_button.clicked.connect(self.fetch_pokemon_data)

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.setGeometry(50, 150, 160, 43)
        self.capture_button.setStyleSheet("color: white;")
        self.capture_button.clicked.connect(self.capture_pokemon)

        self.display_button = QPushButton("Display", self)
        self.display_button.setGeometry(50, 200, 160, 43)
        self.display_button.setStyleSheet("color: white;")
        self.display_button.clicked.connect(self.display_captured_pokemons)

        self.info_layout = QVBoxLayout()
        self.info_widget = QWidget(self)
        self.info_widget.setGeometry(350, 50, 400, 500)
        self.info_widget.setLayout(self.info_layout)

    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text().lower()
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        print(f"Fetching data for: {pokemon_name} from {api_url}")
        
        response = requests.get(api_url)
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"Data fetched: {data}")
            self.display_pokemon_data(data)
        else:
            print(f"Pokémon '{pokemon_name}' not found! Status code: {response.status_code}")

    def display_pokemon_data(self, data):
        for i in reversed(range(self.info_layout.count())):
            self.info_layout.itemAt(i).widget().setParent(None)

        name = data["name"]
        image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
        abilities = [ability["ability"]["name"] for ability in data["abilities"]]
        types = [type_["type"]["name"] for type_ in data["types"]]
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

        self.image_url = image_url  # Save image URL for capturing
        self.pokemon_name = name  # Save Pokémon name for capturing

        name_label = QLabel(f"Name: {name}", self.info_widget)
        name_label.setStyleSheet("color: white;")
        self.info_layout.addWidget(name_label)

        image = QImage()
        image.loadFromData(requests.get(image_url).content)
        pixmap = QPixmap(image)

        image_label = QLabel(self.info_widget)
        image_label.setPixmap(pixmap)
        self.info_layout.addWidget(image_label)

        abilities_label = QLabel(f"Abilities: {', '.join(abilities)}", self.info_widget)
        abilities_label.setStyleSheet("color: white;")
        self.info_layout.addWidget(abilities_label)

        types_label = QLabel(f"Types: {', '.join(types)}", self.info_widget)
        types_label.setStyleSheet("color: white;")
        self.info_layout.addWidget(types_label)

        stats_label = QLabel("Stats:\n" + "\n".join([f"{key}: {value}" for key, value in stats.items()]), self.info_widget)
        stats_label.setStyleSheet("color: white;")
        self.info_layout.addWidget(stats_label)

    def capture_pokemon(self):
        if hasattr(self, 'image_url') and hasattr(self, 'pokemon_name'):
            image_url = self.image_url
            name = self.pokemon_name
            image_data = requests.get(image_url).content
            if not os.path.exists('captured'):
                os.makedirs('captured')
            with open(f"captured/{name}.png", "wb") as image_file:
                image_file.write(image_data)
            print(f"{name} captured!")
        else:
            print("No Pokémon data to capture. Please search for a Pokémon first.")

    def display_captured_pokemons(self):
        self.captured_pokemons = {
            name.split('.')[0]: os.path.join('captured', name)
            for name in os.listdir('captured') if name.endswith('.png')
        }
        self.captured_window = CapturedPokemonsWindow(self.captured_pokemons)
        self.captured_window.show()


class CapturedPokemonsWindow(QWidget):
    def __init__(self, captured_pokemons):
        super().__init__()
        self.setWindowTitle("Captured Pokémon")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        for name, image_path in captured_pokemons.items():
            label_name = QLabel(f"{name.capitalize()}", self)
            label_name.setStyleSheet("color: white;")
            self.layout.addWidget(label_name)

            image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            image_label.setPixmap(pixmap)
            self.layout.addWidget(image_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
