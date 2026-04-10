class Etudiant {
  constructor(nom, prenom, sexe, age) {
    this.nom = nom;
    this.prenom = prenom;
    this.sexe = sexe;
    this.age = age;
  }

  etudier() {
    console.log(`${this.nom} âgé de ${this.age} ans et sexe ${this.sexe}`);
  }
}

// Exemple d'utilisation :
const monEtudiant = new Etudiant("Zongo", "Marc", "Masculin", 22);
monEtudiant.etudier(); 
// Affiche : Zongo âgé de 22 ans et sexe Masculin
