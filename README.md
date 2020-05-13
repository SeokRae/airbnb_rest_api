# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

## Project Install Settings

1. git clone https://github.com/nomadcoders/airbnb-api.git --branch blueprint --single-branch awesome-api-course
2. git remote -v
3. git log
4. rm -rf .git
5. git init
6. git remote add origin {My Resitory}

## My Project Install Settings

1. git init
2. git clone add origin https://github.com/SeokRae/airbnb_rest_api.git

## Project Setting

0. db.sqlite3 삭제
1. pipenv install
2. pipenv shell
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py createsuperuser
6. `django_seed/__init__.py/Seed/faker`
   - 35 line: cls.fakers[code].seed(random.randint(1, 10000)) > cls.fakers[code].seed_instance(random.randint(1, 10000))
7. python manage.py mega_seed

## Django Rest Framework

- pipenv install djangorestframework

### API Actions

- [x] List Rooms
- [x] See Room
- [x] Create Room
- [ ] Edit Room
- [ ] Delete Room
- [ ] Filter Rooms
- [ ] Add Room to Favourites
- [ ] Search By Coords
- [ ] Login
- [ ] Create Account
- [ ] See Favs
- [ ] See Profile
- [ ] Edit Profile
