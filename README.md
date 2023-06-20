# FIPU chatbot

<img src="https://fipu.unipu.hr/_news/icons/4de20a3c357bc3c8867a35ea220f4f9b8983_icon.jpg" width="350" height="200">

The FIPU Chatbot 🤖 is AI-powered chatbot developed as part of the FIPU Lab research and development initiative at the Faculty of Informatics in Pula. 
The chatbot employs the latest iteration of OpenAI's GPT-3.5-Turbo-0613 model with function calling capabilities and is built upon the RASA framework. 
FIPU Chatbot analzyes and interprets JSON data to show a list of availalbe companies for student internships and provides detailed informatoin about each internship.

## Features
- **Function Calling:** Utilizes the function calling capabilities of GPT-3.5-Turbo-0613 to interact effectively with JSON data.
- **Dual User Intents:** Manages two specific user intents — displaying available companies for student internships and providing comprehensive information about each internship.
- **Advanced Conversation Handling:** Leverages the RASA framework for efficient user conversation management.
- **In-depth AI Analysis:** Employs GPT-3.5-Turbo-0613 to accurately analyze and interpret JSON data.

## Instalation

1. Clone the repository:
```bash
git clone https://github.com/lukablaskovic/fipu-chatbot
```

2. Navigate to the project directory
```bashbash
cd fipu-chatbot
```

3. Install the necessary dependencies in your virtual environment
```bash
pip install -r requirements.txt
```

4. Obtain the API keys for GPT-3.5-Turbo and set them as environment variables in .env file
```bash
OPENAI_API_KEY = "Enter your OPENAI KEY here"
```

## Usage

1. Check whether Rasa has installed successfully:
```bash
rasa --version
```

2. Train the RASA model:
```bash
rasa train
```

3. Run the RASA actions server (in separate terminal):
```bash
rasa run actions
```

4. Initiate the RASA shell to interact with the chatbot:
```bash
rasa shell
```

## Video demonstration
https://www.youtube.com/watch?v=VqQtCIG_Wmw

## Customization
The FIPU Chatbot is built on the flexible RASA framework, allowing for easy customization. 
If you want to introduce more intents or enhance its functionality, modify the domain.yml, nlu.yml, and stories.yml files accordingly.

The actions.py file manages the GPT-3.5-Turbo function calls. Here, you can add more function calls or modify existing ones to customize how the chatbot analyzes and interprets JSON data.

## License
The project is licensed under the terms of the MIT license.
