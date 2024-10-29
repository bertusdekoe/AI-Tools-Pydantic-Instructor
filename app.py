from pydantic import BaseModel
from typing import List
from helpers import structured_generator

#Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

#Replace with your input
input = "school test"

#Replace with your prompt
prompt = f"Je bent een AI-model dat de antwoorden op toet vragen van leerlingen nakijkt. Het is jouw taak om voor elke vraag een overzicht te geven van gelijkwaardige of soortgelijke antwoorden die leerlingen hebben gegeven. Deze overzichtslijst moet enkel betrekking hebben op antwoorden die inhoudelijk overeenkomen, zonder aan te geven wat het juiste antwoord is. Geef per vraag de verzameling van deze gelijkwaardige antwoorden in een overzichtelijk overzicht. 
Tijdens het identificeren van gelijkwaardige antwoorden. Zorg ervoor dat je de antwoorden zeer kritisch analyseert. Als er geen gelijkwaardige antwoorden zijn, zorg ervoor om ook dan het gehele antwoord en namen van de leerlingen zijn weergeven. Zorg ervoor dat alle leerling elke vraag is weergegeven 

Uitvoerformaat:
- **Vraag 1:
[overzicht van gelijkwaardige antwoord] [namen van leerlingen] [waarom heb je deze leerlingen bij elkaar gekoppeld]
[overzicht van gelijkwaardige antwoord] [namen van leerlingen] [waarom heb je deze leerlingen bij elkaar gekoppeld]
dit totdat alle gelijkwaardige antwoorden zijn benoemd.
- **Vraag 2:** 
[overzicht van gelijkwaardige antwoord] [namen van leerlingen] [waarom heb je deze leerlingen bij elkaar gekoppeld]
[overzicht van gelijkwaardige antwoord] [namen van leerlingen] [waarom heb je deze leerlingen bij elkaar gekoppeld]
dit totdat alle gelijkwaardige antwoorden zijn benoemd.
 
Herhaal dit format voor alle vragen in de toets.
{input}" 

#Replace With Your Model
openai_model = "gpt-3.5-turbo"

result = structured_generator(openai_model,prompt,Titles)
print(result.titles)
