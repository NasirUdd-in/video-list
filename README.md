# framework: django
# database: sqlite
# full problem solved

## http://nasir96.pythonanywhere.com/admin
## admin login
   username: admin
   password: admin

1. User can login

http://nasir96.pythonanywhere.com/login/

example user
username: test1
password: test1

2. User can add a movie

http://nasir96.pythonanywhere.com/add-movies/

3. User can view a list of all movies

http://nasir96.pythonanywhere.com/all-ratings/

4. User can rate a movie

http://nasir96.pythonanywhere.com/ratings/


5. User search up a specific movie and see it’s details along with the average rating of a movie

http://nasir96.pythonanywhere.com/?name=inception


#run on local machine by using below docker cmd

docker-compose up

