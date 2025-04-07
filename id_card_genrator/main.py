import os
import json
from id_card_genrator.genrate_id_card import VoterIDCardGenerator

class IDCardApp:
    def __init__(self, json_path, canvas_path, qr_dir="qrcodes", output_dir="id_cards"):
        self.json_path = json_path
        self.canvas_path = canvas_path
        self.qr_dir = qr_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.qr_dir, exist_ok=True)
        self.generator = VoterIDCardGenerator(self.canvas_path, self.qr_dir, self.output_dir)

    def load_voter_data(self):
        with open(self.json_path, 'r') as f:
            return json.load(f)

    def generate_all_cards(self):
        data = self.load_voter_data()
        for uid, details in data.items():
            self.generator.create_card(details)

    def run(self):
        print("🚀 Starting ID Card generation...")
        self.generate_all_cards()
        print("✅ All ID cards generated successfully!")

if __name__ == "__main__":
    json_path = input("Enter the path to the JSON file: ")
    if not json_path:
        json_path = "Voter_id_web_server/database/database_storage/uid_as_key_dict.json"
    canvas_path = "sample.png"

    app = IDCardApp(json_path, canvas_path)
    app.run()
