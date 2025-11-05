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

## 🚀 6. Upload to GitHub

Run these commands:

```bash
git init
git add .
git commit -m "Initial commit - Enhanced DNAC PyATS AP Client Test"
git branch -M main
git remote add origin https://github.com/<your-username>/dnac-ap-client-test.git
git push -u origin main
🎁 Bonus (Optional Add-ons)
Later, you can add:

✅ pytest wrapper for CI/CD pipeline

✅ Jenkins job for automation

✅ REST API calls to DNAC for real-time status checks

✅ HTML report auto-upload to artifacts

Would you like me to help you add a Jenkins pipeline YAML or GitHub Actions workflow file next — so it runs automatically when you push updates to GitHub (CI/CD setup)?







You said:
can u add those files to my github repostry



ChatGPT said:
I don’t have direct access to your GitHub account — so I can’t push the files for you.
But don’t worry 😊 — I’ll walk you step-by-step through exactly how to add everything to your repo (it’ll take only a few minutes).

🧭 Step-by-Step: Add Files to Your GitHub Repository
1️⃣ Create the Repo (if not already done)
Go to 👉 https://github.com/new

Set the repo name — for example:
dnac-ap-client-test

Choose Public (so you can showcase it)

Don’t add any files yet (no README)

Click Create repository

2️⃣ Prepare the Project Locally
Open a terminal (VS Code or command prompt) and run:

bash
Copy code
# Go to where you want to keep the project
cd Desktop

# Clone your new empty repo
git clone https://github.com/<your-username>/dnac-ap-client-test.git
cd dnac-ap-client-test
3️⃣ Create the Files
Now copy and paste these commands (or create the files manually):

bash
Copy code
mkdir tests logs reports
Then create these files (you can copy from my previous message):

tests/test_ap_client_join.py

tests/utils.py

testbed.yaml

requirements.txt

README.md

You can use VS Code or notepad command in terminal:

bash
Copy code
code tests/test_ap_client_join.py
and paste the code I gave earlier.

4️⃣ Commit & Push
Once all files are in place:

bash
Copy code
git add .
git commit -m "Initial commit - Enhanced DNAC PyATS AP Client Test"
git branch -M main
git push -u origin main
After this, refresh your GitHub repo page — you’ll see all the folders and files beautifully organized 🎉

5️⃣ (Optional) Run Locally to Verify
If you have Python installed, test it locally:

bash
Copy code
pip install -r requirements.txt
python tests/test_ap_client_join.py
You should see log files inside /logs/ and the console output.

