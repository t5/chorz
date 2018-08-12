# Chorz 

A web-based chore manager for people living together. I was motivated to replace the paper chore board, which had to be generated weekly, for seven housemates over the summer. Chores can be created, assigned to users and rotated on a customizable basis. Users will be able to mark if and when a particular chore has been completed. 

<p align="center"><img width=50% src="https://raw.githubusercontent.com/t5/chorz/master/screenshot.png" alt="screenshot"></p>

## Demo

View the **[Demo](https://chorz-manager.herokuapp.com/)**.

Test out the functionalities using any of the demo 'housemates':

**Username**: `alexis OR brad OR carol ...` 

**Password**: `testtest123`

## Installation

### Prerequisites

You will first need to install Python >= 3.6.4 and PIP. Then install Django:

```
pip install Django
```

### Running on localhost 

```
python manage.py collectstatic
python manage.py runserver
```

Navigate to http://localhost:8000 to view the site.

## Built With

* [Django](https://www.djangoproject.com/) - Web framework 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
