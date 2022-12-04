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

Toiminnallisuutta täytyy vielä laajentaa. Ensimmäisten viikkojen aikana suuri osa ajasta kului SQL:n ja Flask-riippuvuuksien konfigurointiin (ja niiden toiminnan ymmärtämiseen). Nyt kun konfiguraatio on tehty riittävän onnistuneesti uskon, että sovellus etenee tulevilla viikoilla paremmin.

Kurssimateriaalin mukaisesti lopulliseen applikaatioon on tarkoitus lisätä seuraavaa toiminnallisuutta:

- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.

Puutteita on itse toiminnallisuuden lisäksi tietoturvassa, johon ei juuri ole vielä kiinnitetty erityistä huomiota. Tarkoitus on lisätä käyttöön ainakin CSRF-tokenit.

## Välipalautus 3

Sovellus on viimeistelyä vaille valmis. Toteutettua toiminnallisuutta:

- Käyttäjä voi luoda tilin joka on joko normaali käyttäjä tai admin.
- Käyttäjä voi kirjautua luodulla käyttäjällä ja salasanalla.
- Käyttäjä voi luoda uuden ketjun.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Käyttäjä voi lisätä aiheen omiin aiheisiinsa.
- Käyttäjä voi antaa pisteen aiheen luojalle.

Aiempaan verrattuna tässä versiossa virheviestejä on paranneltu, CSRF-tokenit lisätty käyttöön ja ulkoasu luotu CSS:ää käyttäen.

fly.io ei ole käytettävissä, koska pankkitunnuksia vaadittiin. Ohjelmaa voi halutessaan testata kloonamalla sen GitHub-repositorion ja käyttämällä ohjelmaa paikallisesti.

Seuraavalla tavalla voidaan asentaa venv, flask ja tarvittavat riippuvuudet. Kommennot tulee suorittaa kansiossa, johon projekti kloonattiin:

```python3 -m venv venv```

```source venv/bin/activate```

```pip install flask```

```pip install flask-sqlalchemy```

```pip install psycopg2```

```pip install python-dotenv```

Applikaation käyttöön (projektin juureen) tulee konfiguroida .env-tiedosto, joka sisältää kurssimateriaalin kaltaisesti seuraavat tiedot:

```DATABASE_URL=postgresql+psycopg2::///***insert username here***```

```SECRET_KEY=***insert secretkey here***```

Olettaen, että postgre on asennettu kurssimateriaalin mukaan voidaan tietokanta käynnistää ajamalla:

```start-pg.sh```

Otetaan oikea schema käyttöön ja käynnistetään applikaatio paikallisesti ajamaalla projektin kansiossa:

```psql < schema.sql```

```flask run```
