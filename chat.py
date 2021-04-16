from parlai.scripts.interactive_web import InteractiveWeb
# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty('rate',125)
# engine.say("I will speak this text")
# engine.runAndWait()

InteractiveWeb.main(
    model_file='zoo:dodecadialogue/empathetic_dialogues_ft/model',
    inference= 'beam',
    beam_size= 5,
    beam_min_length= 10,
    beam_block_ngram= 3,
    beam_context_block_ngram= 3
)