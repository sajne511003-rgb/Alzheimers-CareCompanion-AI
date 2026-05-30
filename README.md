1. What is CareCompanion AI?

CareCompanion AI is a smart chatbot app built to help family members and caregivers look after patients with early to moderate-stage Alzheimer's disease. It doesn't just answer questions—it is programmed with special safety rules and digital "tools" to give practical, real-world help when a caregiver is facing a stressful situation.

2. How the App Works

We designed this app using two main types of knowledge:

A. The Rules 
The chatbot follows strict guidelines to keep things safe and helpful:
- No Medical Diagnoses: To keep things safe, the AI is not allowed to give medical prescriptions or diagnose a patient. 
- Patience First: If a caregiver mentions that a patient keeps asking the same question over and over, the AI is programmed to give calm advice and remind the caregiver to respond gently.
- Easy to Read: The AI automatically breaks down long, complicated paragraphs into short, simple bullet points so a busy caregiver can read it quickly.

B. The Tools (What the AI can do)
When you type a scenario into the chat, the AI automatically recognizes what is happening and triggers special background functions to help:

- Emergency ID Generator: If you mention a patient wandering outside alone, it triggers a tool to create an emergency contact card layout to print out.
- Environmental Note Scheduler: If a patient is forgetting where things are, this tool sets up text for visual reminders (like sticky notes) around the house.
- Repetitive Action Tracker: If a patient keeps doing the same thing (like asking for lunch 4 times), this tool logs the event and suggests using gentle audio cues to remind them they already ate.
- Observation Log Analyzer: This helps track patient behavior changes over a whole month rather than just judging things day-by-day.
- Stage Proximity Mapper: It looks at the behaviors you describe and guesses whether the patient is in the early, moderate, or late stage of the disease, just to help you organize the house safely.

The file included iion this repository:
   `src/streamlit_app.py` - The main Python file containing our chatbot code and interface.
   `requirements.txt` - A simple text list telling the hosting platform which libraries it needs to install to run our code.

3. How to Run This App Locally

If you want to download our project and run it on your own computer, just follow these simple steps:

Step 1: Clone (Download) the Project
Open your computer's terminal or command prompt and type:
```bash
git clone https://github.com/sajne511003-rgb/Alzheimers-CareCompanion-AI.git
cd Alzheimers-CareCompanion-AI

4. Run it on Hugging Face

How to Host and Run This App on Hugging Face Spaces
If you don't want to run the app on your local computer, you can easily link your GitHub files to Hugging Face Spaces to host it online for free.

   Step 1: Create a New Space
Go to huggingface.co and sign up for a free account (or log in).

Click on your profile picture in the top right corner and click "New Space".

Fill in these basic settings:

Space Name: Choose a name (like Alzheimers-CareCompanion-AI).

SDK: Click and select Streamlit.

Space Hardware: Keep the default free "CPU Basic" option.

Visibility: Choose Public (everyone can see it) or Private (only you can see it).

Click the "Create Space" button at the bottom.

   Step 2: Import Your Files Directly From GitHub
Instead of uploading files manually, you can pull them instantly from your GitHub repository using Git:

Open your computer's terminal or command prompt.

Clone your Hugging Face Space repository locally by copying the command provided on your new blank Space page. It will look like this:

Bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
3. Copy the files (`app.py` or `src/streamlit_app.py` and `requirements.txt`) from your local GitHub folder into this new Space folder. 
4. *Note: For Hugging Face to launch the interface automatically, make sure your main script file is named **`app.py`** and sits in the root (main) folder.*
5. Save, commit, and push the files to Hugging Face by typing:
   ```bash
   git add .
   git commit -m "Import files from GitHub repository"
   git push

   Step 3: Set Up Your Secret API Keys (Important!)
Because CareCompanion AI connects to an external AI model, you need to securely give Hugging Face your private API keys:

On your Hugging Face Space page, click on the "Settings" tab at the top.

Scroll down to the "Variables and secrets" section and click "New secret".

In the Name box, type the exact key your code looks for (for example: OPENAI_API_KEY or GEMINI_API_KEY).

In the Value box, paste your actual secret API key string.

Click "Save".

   Step 4: Launch the App
Go back to the "App" tab at the top of your Space page. Hugging Face will automatically read your requirements.txt file, install the necessary libraries, and start your Streamlit chatbot app. This setup process usually takes 1 to 2 minutes. Once the status bar turns green and says "Running," your online app is live and ready to use!
