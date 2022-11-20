# hy-tsoha-keskustelusovellus

## Keskustelusovellus

Ajatuksena on toteuttaa keskustelusovellus. Sovelluksen ominaisuudet tulevat koostumaan kurssimateriaalissa ehdotetusta toiminnallisuudesta siinä määrin kun se keretään kurssin aikana toteuttaa.

Keskeisinä toimintoina pidän ainakin seuraavia:

- käyttäjätunnuksen luominen ja sen avulla sovellukseen kirjautuminen
- uuden ketjun luominen
- olemassaolevaan ketjuun kirjoittaminen

Alustava ajatus on lähteä yllämainituista liikkeelle ja sitten laajentaa sovellusta ajan puitteissa muuhun kurssimateriaalissa keskustelusovelluksen osalta mainittuun toiminnallisuuteen.

## Välipalautus 2

Sovelluksen pohja on toteutettu. Sovellukseen voi luoda käyttäjän joka on joko normaali käyttäjä tai admin. Sovellukseen voi kirjautua luodulla käyttäjällä ja salasanalla. Käyttäjä voi luoda uuden ketjun.

Toiminnallisuutta täytyy vielä laajentaa. Ensimmäisten viikkojen aikana suuri osa ajasta kului SQL:n ja Flask-riippuvuuksien konfigurointiin. Nyt kun konfiguraatio on tehty riittävän onnistuneesti uskon, että sovellus etenee tulevilla viikoilla paremmin.

Puutteita on itse toiminnallisuuden lisäksi tietoturvassa, johon ei juuri ole vielä kiinnitetty erityistä huomiota. Tarkoitus on lisätä käyttöön ainakin CSRF-tokenit.

fly.io ei ole käytettävissä, koska pankkitunnuksia vaadittiin. Ohjelmaa voi halutessaan testata kloonamalla sen GitHub-repositorion ja käyttämällä ohjelmaa paikallisesti.

Seuraavalla tavalla voidaan asentaa venv, flask ja tarvittavat riippuvuudet. Kommennot tulee suorittaa kansiossa, johon projekti kloonattiin:

python3 -m venv venv
source venv/bin/activate
pip install flask
pip install flask-sqlalchemy
pip install psycopg2
pip install python-dotenv

Applikaation käyttöön (projektin juureen) tulee konfiguroida .env-tiedosto, joka sisältää kurssimateriaalin kaltaisesti seuraavat tiedot:

DATABASE_URL=postgresql+psycopg2::///***insert username here***
SECRET_KEY=***insert secretkey here***

Olettaen, että postgre on asennettu kurssimateriaalin mukaan voidaan tietokanta käynnistää ajamalla:

start-pg.sh

Otetaan oikea schema käyttöön ja käynnistetään pplikaatio paikallisesti ajamaalla projektin kansiossa:

psql < schema.sql
flask run
