prepare:
	python3 -m venv venv && source venv/bin/activate && pip install flask

run:
	PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python3 app.py

tls-cert:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout miapp.key -out miapp.crt -subj "/CN=miapp.local"

nginx:
	sudo systemctl restart nginx

check-http:
	curl -v http://127.0.0.1:8080/

check-tls:
	curl -k https://miapp.local/

dns-demo:
	dig +short miapp.local
