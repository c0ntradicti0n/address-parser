import pprint

import spacy

nlp=spacy.load("output/models/model-best")


"""
The function that will be called when the processor processes.
"""
def f(intent=None, userinput=None, **other_arguments_from_context):

    text = userinput if userinput else intent

    doc = nlp(text)
    ent_list = [(ent.text, ent.label_) for ent in doc.ents]
    print("Address string -> " + text)
    print ("entities:")
    pprint.pprint((ent_list))

    return {
        "entities": ent_list
    }
