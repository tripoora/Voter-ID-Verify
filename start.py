from Voter_id_web_server import VoterVerificationApp
from id_card_genrator import IDCardApp

json_path = r'Voter_id_web_server\database\database_storage\uid_as_key_dict.json'
canvas_path = r'id_card_genrator\sample.png'
id_card_app = IDCardApp(json_path=json_path, canvas_path=canvas_path)

#  id genrator
id_card_app.run()

#  web server
web_app = VoterVerificationApp()
web_app.run(debug=True)
