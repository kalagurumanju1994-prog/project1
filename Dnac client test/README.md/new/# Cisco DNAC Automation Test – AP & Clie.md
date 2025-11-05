# Cisco DNAC Automation Test – AP & Client Join (PyATS)

This project automates the verification of Access Point (AP) and Client join functionality
in Cisco DNAC (Digital Network Architecture Center) using **PyATS**.

---

## Overview

The test connects to a Cisco Wireless LAN Controller (WLC) and a client device via SSH,
then performs automated checks for:
- AP registration status
- Client connection status
- Network connectivity via ping

---

##  Project Structure

# ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/dnac-ap-client-test.git
cd dnac-ap-client-test
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Configure Your Testbed
Update testbed.yaml with your WLC and Client details:

yaml
Copy code
ip: 10.10.10.5
username: admin
password: Cisco123
4️⃣ Run the Test
bash
Copy code
python tests/test_ap_client_join.py
📊 Example Output
yaml
Copy code
✅ AP Registration: PASSED
✅ Client Join: PASSED
✅ Client Ping: PASSED
🧹 Cleanup Completed
A log file is also generated in the logs/ folder, and a PyATS HTML report appears in reports/.

🧰 Tools Used
Cisco PyATS

Cisco Genie

Python 3.9+

SSH/SFTP for device connectivity

👨‍💻 Author
Manjunath Sai
Test Engineer – Cisco DNAC Project
Jan 2023 – Present

📜 License
MIT License

yaml
Copy code

---

