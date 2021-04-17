# Digital Social companion for the elderly 

The repository contains the code for a digital social companion designed fro the elderly. There are two parts of the code, the fultter application and the interactive chat bot currently implemented with a browser based UI. For more information please read the document "Final report"

## Taiga, the chatbot

The chatbot requires some basic python packages to run. We would highly recommend you to setup a virtual environment for this purpose. The following commands should let you run setup the chatbot:

`pip install -r requirements.txt`

Once the installation is complete, copy the following files to `/path/to/python/site-packages/parlai/scripts`:
- interactive.py
- sentiment_analysis.py
- interactive_web.py

Now, run the following command:
`python chat.py`

Now open localhost:8080 on your web browser and you are ready to interact with Taiga!


## Running the flutter app

The running of the flutter app requires you to setup flutter on your terminal, VSCode or Android Studio. The instructions are available on the following link:
https://flutter.dev/docs/get-started/install

Now once set up, clone the project and run the application. If setup on the terminal, the app would run with the following command:
`flutter run`

If the app continues to give errors, try running:
`flutter pub get`

followed by:
`flutter run`
