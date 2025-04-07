---
# Voter-ID-Verify

A web-based system to verify Voter ID cards using QR codes.  
Special thanks to [py-hariom](https://github.com/py-hariom/py-hariom) for inspiration.

## 🔍 What It Does

This system uses QR codes to check voter identities quickly and securely. It’s easy to use and makes the voting process faster and more reliable.

## ✅ Features

- Scan Voter ID QR codes
- Check voter details instantly
- Store voter data securely
- Easy-to-use web interface
- Clear messages for any errors

## 📁 Project Structure

```
Voter-ID-Verify/
├── app.py                    # Main web app (Flask)
├── verification.py           # Logic for checking voter info
├── database/
│   ├── __init__.py
│   └── storage_manage.py     # Manages saved data
│   └── database_storage/
│       ├── uid_as_key_dict.json    # Voter data by UID
│       └── uid_voterid_list.json   # UID to Voter ID link
└── templates/
    └── index.html            # Web page for scanning
```

## 🧰 Requirements

- Python 3.x
- Flask
- A QR code scanner (for testing)

## 🚀 How to Install

1. **Clone the project:**
   ```bash
   git clone https://github.com/tripoora/Voter-ID-Verify.git
   cd Voter-ID-Verify
   ```

2. **Install Python libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app:**
   ```bash
   python app.py
   ```

## 🌐 How to Use

1. Run `app.py`
2. Open your browser and go to [http://localhost:5000](http://localhost:5000)
3. Scan the Voter ID QR code
4. The system shows whether the voter is valid or not

## 🔗 API Endpoints

- `GET /` → Main page  
- `POST /qr-data` → Checks the QR code  
   - **Input:** QR code data in JSON  
   - **Output:** JSON with results

## 🎯 Why Use This

- **Fast:** Verifies quickly
- **Accurate:** Reduces human mistakes
- **Safe:** Keeps data protected
- **Easy:** Simple for anyone to use
- **Scalable:** Works for many voters at once

## ⚠️ Error Messages

The app shows clear messages if something goes wrong:

- Invalid or fake QR code
- Voter not found
- Data loading issues
- Server problems

## 🤝 Contribute

Want to help?

1. Fork this repo
2. Make a new branch (`git checkout -b new-feature`)
3. Add your code and commit it
4. Push the changes (`git push origin new-feature`)
5. Make a pull request

## 📄 License

This project uses the **MIT License**.  
Check the `LICENSE` file for details.

## 💡 Coming Soon

- Mobile app support
- Fingerprint/Face verification
- Real-time stats dashboard
- Support for more languages
- Stronger security options

---
