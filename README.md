# eventProject

### Kratki opis aplikacije

Aplikacija služi za prikaz raznih događanja (u ovoj aplikaciji nazvani *Eventi*) koje ovlašteni korsinici (administratori) kreiraju. Administratori su korisnici koji ili privatno ili u ime neke grupe/organizacije kreiraju neki event i postavljaju ga na sustav pomoću objave. Korisnici mogu iskazati zainteresiranost za neki event, ili mogu potvrditi dolazak na event. Također mogu filtrirati evente po vremenu ili nekim drugim obilježjima. 


### ToDo

- [x] create initial database schema
- [x] create login, signup with django-allauth
- [x] update events model (relation with user model)
- [x] update number of users attending event
- [x] create basic user view
- [x] display events created by the selected user   
- [x] user can change picture and update profile
- [x] add more fields to user
- [ ] creating admin users? (TBD if needed)
- [x] edit: ~~admin~~ user can create/delete/update new events? (TBD if only admin permission)
- [x] add img field to event creation
- [x] creating new events
- [ ] style the website
    - [ ] style landing
    - [ ] style events
    - [ ] style forms
    - [ ] style user view
- [ ] connect with S3

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

