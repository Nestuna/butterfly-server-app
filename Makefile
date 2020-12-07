-include butterfly_api/.env
export


build:  # Créer l'image localement du serveur web Django et du serveur DB MySQL (à faire la première fois ou si ça bug)
		# Et les lance ensuite
	sudo docker-compose up --build

run: #Lance les serveurs seulement
	sudo docker-compose up

shell : # Ouvre la console python dans l'environnement de Django
	sudo docker-compose run web python manage.py shell

makemigrations : # Inscrit les modifications de la DB dans le registre
	sudo docker-compose run web python manage.py makemigrations

migrate: # Applique les modifications
	sudo docker-compose run web python manage.py migrate

bash: # Ouvre un shell bash dans le serveur
	sudo docker-compose run web /bin/bash

sql: # Ouvre MySQL en ligne de commande
	sudo docker exec -it butterfly_project_back_db_1 mysql --user=root --password=${DATABASE_PASSWORD} --database=butterfly-db