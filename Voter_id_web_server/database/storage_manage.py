import json
import os

class StorageManage:
    def __init__(self):
        self.uid_dict_path = r'Voter_id_web_server\database\database_storage\uid_as_key_dict.json'
        self.uid_voterid_path = r'Voter_id_web_server\database\database_storage\uid_voterid_list.json'
        self.voted_status_path = r'Voter_id_web_server\database\database_storage\voted_status.json'

    def get_data(self, uid: str):
        """Fetch full voter data by UID"""
        print(f"🔐 Looking up UID: {uid}")
        try:
            with open(self.uid_dict_path, 'r') as file:
                data = json.load(file)
                if uid in data:
                    print("✅ Voter data found.")
                    return [True, data[uid]]
                return [False, f"UID '{uid}' not found."]
        except Exception as e:
            print(f"❌ Error: {e}")
            return [False, f"Error reading UID data: {e}"]

    def find_uid_by_voter_id(self, voter_id: str):
        """Find UID using voter ID"""
        print(f"🔎 Searching for Voter ID: {voter_id}")
        try:
            with open(self.uid_voterid_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    if item.get('voter_id') == voter_id:
                        uid = item.get('uid')
                        print(f"🎯 Found UID: {uid}")
                        return [True, uid]
                return [False, f"Voter ID '{voter_id}' not found."]
        except Exception as e:
            return [False, f"Error reading voter ID list: {e}"]


    def check_and_mark_voted(self, voter_id: str):
        """
        Checks if a voter has already voted.
        If not, marks them as voted.
        Returns True if allowed to vote (first time), False otherwise.
        """
        voted_status_path = 'database/database_storage/voted_status.json'

        # Ensure file exists
        if not os.path.exists(voted_status_path):
            with open(voted_status_path, 'w') as f:
                json.dump({}, f)

        try:
            with open(voted_status_path, 'r+') as file:
                data = json.load(file)

                if voter_id in data and data[voter_id] is True:
                    print(f"❌ Voter {voter_id} has already voted.")
                    return False  # Already voted

                # Mark as voted
                data[voter_id] = True
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

                print(f"✅ Voter {voter_id} marked as voted.")
                return True  # First-time vote allowed

        except Exception as e:
            print(f"❌ Error checking vote status: {e}")
            return False
