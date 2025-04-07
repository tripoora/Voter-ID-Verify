import os
import json
import qrcode
from PIL import Image, ImageDraw, ImageFont

class VoterIDCardGenerator:
    def __init__(self, canvas_path, qr_output_dir, card_output_dir):
        self.canvas_path = canvas_path
        self.qr_output_dir = qr_output_dir
        self.card_output_dir = card_output_dir

        try:
            self.font_bold = ImageFont.truetype("arialbd.ttf", 28)
            self.font_regular = ImageFont.truetype("arial.ttf", 28)
            self.font_header = ImageFont.truetype("arialbd.ttf", 36)
        except:
            self.font_bold = self.font_regular = self.font_header = ImageFont.load_default()

    def generate_qr_code(self, voter_id, name):
        qr_data = json.dumps({"voter_id": voter_id, "name": name})
        qr = qrcode.make(qr_data)
        filename = f"{voter_id}-{name.replace(' ', '_')}.png"
        path = os.path.join(self.qr_output_dir, filename)
        qr.save(path)
        return path

    def create_card(self, details):
        canvas = Image.open(self.canvas_path).copy()
        draw = ImageDraw.Draw(canvas)

        voter_id = details["voter_id"]
        name = details["name"]
        qr_path = self.generate_qr_code(voter_id, name)
        qr_img = Image.open(qr_path).resize((200, 200))

        canvas.paste(qr_img, (750, 180))

        draw.text((370, 30), "Dummy Voter Identy Card", fill="black", font=self.font_header)

        info = {
            "Voter ID Number": voter_id,
            "Name": name,
            "Gender": details["gender"],
            "Father Name": details["father_name"],
            "Address": details["address"]
        }

        x_label = 120
        x_value = 380
        y_start = 120
        line_gap = 60

        for idx, (label, value) in enumerate(info.items()):
            y = y_start + idx * line_gap
            draw.text((x_label, y), label, fill="black", font=self.font_bold)
            draw.text((x_value, y), value, fill="black", font=self.font_regular)

        filename = f"{voter_id}-{name.replace(' ', '_')}_card.png"
        canvas.save(os.path.join(self.card_output_dir, filename))
        print(f"✅ Card generated: {filename}")
