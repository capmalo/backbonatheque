Creator: Malo FERNDNADEZ
Test technique - stage d�veloppeur Python Valoo

Ce readme apporte quelques explications n�cessaires sur mon travail sur ce test technique.

Tout d'abord, je tiens � dire que j'ai trait� les 3 contraintes, mais que ce n'est pas fonctionnel car je ne connais pas du tout Django et je n'ai pas eu le temps d'�tudier comment faire des bases de donn�es avec.
Par cons�quent, j'ai mis ce que je ne connaissait pas en pseudo-code/commentaire.

Donc, des modifications ont �t�s apport�es au fichier models.py (contraintes n�1 & 2) et j'ai cr�� un fichier syncro.py (contrainte n�3):

models.py:
- J'ai cr�� deux m�thodes error_handling et timeout handling pour g�rer les deux types d'erreurs, et enregistrer les informations dans les bdd correspondantes.
- J'ai d�plac� la partie envoi de donn�es de la m�thode toggle_playing dans une m�thode send_data (�vite les copi�-coll�).
- J'effectue un ping sur le serveur major avant tout envoi de donn�es (pas la peine d'essayer si il est injoignable).
- Ensuite soit le serveur n'a pas �t� timeout derni�rement et on envoie normalement, soit on envoie les donn�es en cache, on les efface puis on envoie normalement.

syncro.py:
- Deux m�thodes sont int�ressantes ici: check_sync et restart_sync
- check_sync affiche toutes les erreurs stock�es dans la dase de donn�es des erreurs
- restart_sync renvoie les donn�es au majour sur m�me base qua dans models.py


Si vous avez des questions n'h�sitez pas, je suis � votre disposition.
Merci d'avoir pris le temps d'�tudier mon travail.