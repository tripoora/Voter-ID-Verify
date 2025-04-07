from Voter_id_web_server.database import storage_manage
import json

storage_manage = storage_manage.StorageManage()

class Verification:
    def __init__(self):
        self.uid = None

    def verify_data(self, data):
        if not data or 'qr' not in data:
            return [False, 'Invalid input: Missing QR.']

        try:
            qr_data = json.loads(data['qr'])  # Parse QR string
            voter_id = qr_data.get('voter_id')
            print(f"🧾 Verifying voter_id: {voter_id}")
            print(f"🧾 Looking For Voter : {voter_id}")
        except Exception as e:
            return [False, f"Invalid QR format: {e}"]

        if not voter_id:
            return [False, "Voter ID is missing in QR."]

        result = storage_manage.find_uid_by_voter_id(voter_id)
        if not result[0]:
            return [False, result[1]]

        # Save UID for data fetch
        self.uid = result[1]
        return [True, voter_id]  # Now return voter_id for marking voted later


    def send_data(self):
        if self.uid:
            return storage_manage.get_data(self.uid)
        return [False, "UID not found."]
