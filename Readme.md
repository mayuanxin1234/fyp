# Setup Instructions
### 1. Create a Virtual Environment
To ensure a clean installation, start by creating a virtual environment:

```
python3 -m venv myenv
```

### 2. Activate the Virtual Environment
Activate the environment you just created:

macOS/Linux:
```
source myenv/bin/activate
```
Windows:
```
myenv\Scripts\activate
```

### 3. Install Required Packages
Run the following commands to install all necessary dependencies:

```
pip install -r requirements.txt
```


### 4. Start the Chatbot Interface
Navigate to the root directory of the project and run:
```
python3 ui.py
```

### 5. Access the Chatbot
Once the program is running, open your browser and go to:

http://127.0.0.1:7860

### Important Notes
Keep It Secure: This project uses OpenAI secret keys. Please do not share these keys with anyone.