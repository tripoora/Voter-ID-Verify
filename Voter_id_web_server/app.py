from flask import Flask, render_template, request, jsonify
from Voter_id_web_server.verification import Verification  # Assuming this is the correct import path
import json

class VoterVerificationApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.verifier = Verification()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')  # Web UI for QR scanner

        @self.app.route('/qr-data', methods=['POST'])
        def qr_data():
            try:
                data = request.json
                print("📥 Received data:", data)

                # Step 1: Verify voter (also marks them voted if valid)
                result = self.verifier.verify_data(data)
                if not result[0]:
                    print("❌ Verification failed:", result[1])
                    return jsonify({'error': result[1]}), 400

                # Step 2: Get full voter details
                response = self.verifier.send_data()
                print("✅ Final response from send_data:", response)

                if response[0]:
                    return jsonify(response[1]), 200
                else:
                    return jsonify({'error': response[1]}), 400

            except Exception as e:
                print("❌ Server Exception:", e)
                return jsonify({'error': f"Server error: {str(e)}"}), 500

    def run(self, debug=True):
        self.app.run(debug=debug)

if __name__ == '__main__':
    app = VoterVerificationApp()
    app.run()
