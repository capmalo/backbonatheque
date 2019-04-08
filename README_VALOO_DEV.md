Creator: Malo FERNDNADEZ
Test technique - stage développeur Python Valoo

Ce readme apporte quelques explications nécessaires sur mon travail sur ce test technique.

Tout d'abord, je tiens à dire que j'ai traité les 3 contraintes, mais que ce n'est pas fonctionnel car je ne connais pas du tout Django et je n'ai pas eu le temps d'étudier comment faire des bases de données avec.
Par conséquent, j'ai mis ce que je ne connaissait pas en pseudo-code/commentaire.

Donc, des modifications ont étés apportées au fichier models.py (contraintes n°1 & 2) et j'ai créé un fichier syncro.py (contrainte n°3):

models.py:
- J'ai créé deux méthodes error_handling et timeout handling pour gérer les deux types d'erreurs, et enregistrer les informations dans les bdd correspondantes.
- J'ai déplacé la partie envoi de données de la méthode toggle_playing dans une méthode send_data (évite les copié-collé).
- J'effectue un ping sur le serveur major avant tout envoi de données (pas la peine d'essayer si il est injoignable).
- Ensuite soit le serveur n'a pas été timeout dernièrement et on envoie normalement, soit on envoie les données en cache, on les efface puis on envoie normalement.

syncro.py:
- Deux méthodes sont intéressantes ici: check_sync et restart_sync
- check_sync affiche toutes les erreurs stockées dans la dase de données des erreurs
- restart_sync renvoie les données au majour sur même base qua dans models.py


Si vous avez des questions n'hésitez pas, je suis à votre disposition.
Merci d'avoir pris le temps d'étudier mon travail.