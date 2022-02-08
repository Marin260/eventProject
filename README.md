# eventProject

### Kratki opis aplikacije

Aplikacija služi za prikaz raznih događanja (u ovoj aplikaciji nazvani *Eventi*) koje ovlašteni korsinici (administratori) kreiraju. Administratori su korisnici koji ili privatno ili u ime neke grupe/organizacije kreiraju neki event i postavljaju ga na sustav pomoću objave. Korisnici mogu iskazati zainteresiranost za neki event, ili mogu potvrditi dolazak na event. Također mogu filtrirati evente po vremenu ili nekim drugim obilježjima. 

### Kratki opis modela

Klasa Mjesto sadrži informacije o pojedinom mjestu - poštanski broj, naziv mjesta i državu. Klasa AdminKorisnici sadrži informacije o administracijskom korisniku koji kreira objave na sustavu (ime admina, adresa ustanove adminove organizacije, kontakt broj admina i mjesto u kojem se admin nalazi). Klasa Event koristi se za definiranje nekog eventa koji se održava. Klasa Objava pohranjuje informaciju o pojedinoj objavi i stranim ključem vezana je za objekt klase Event. Klasa korisnik sadrži informacije o pojedinom korisniku te broj evenata za koje je iskazao interes.

### ToDo

- [x] create initial database schema
- [x] create login, signup with django-allauth
- [x] update events model (relation with user model)
- [x] update number of users attending event
- [ ] creating admin users? (TBD if needed)
- [ ] admin can create/delete/update new events? (TBD if only admin permission)
- [ ] admin can add image to event
- [ ] creating new events
- [ ] style the website

###### Later plans
- [ ] google registration (with allauth)
- [ ] infinite scroll
- [ ] async
- [ ] extend user model
- [ ] user profile/stats/pfp/bio
- [ ] calendar tracker
- [ ] search
- [ ] dispaly filters
- [ ] maps

