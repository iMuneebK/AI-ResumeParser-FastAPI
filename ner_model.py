import spacy

class CustomNER:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            self.nlp = spacy.blank("en")
            
    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = {"ORG": [], "PERSON": [], "GPE": []}
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent.text)
        
        skills_db = ['python', 'java', 'sql', 'aws', 'machine learning', 'react']
        found_skills = [s for s in skills_db if s in text.lower()]
        
        return {"extracted_entities": entities, "skills": found_skills}
