from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/bemtech/v1")
def debut() :
    return "API BEMTECH - Gestion des Etudiants"

class etudiants(BaseModel):
    id:int
    nom:str
    prenom:str
    age:int
    sexe:str
    filiere:str

#On crée un dictionnaire vide qui va recevoir les données des etudiants qu'on va enregistrer et les conserver en mémoire
liste_etudiant =[]
#Route pour creer un nouvel etudiant
@app.post("/bemtech/v1/etudiants")
def nouvel_etudiant(etudiant:etudiants):
    liste_etudiant.append(etudiant)
    return {
        "statut": "Etudiant enregistré avec succès",
        "données": etudiant
    }

    #Route pour afficher la liste des etudiants
@app.get("/bemtech/v1/etudiants")
def afficher_tous_les_etudiants():
    return liste_etudiant