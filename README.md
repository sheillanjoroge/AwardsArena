# AwardsArena

Platform for submitting projects and other like minded fellows can rate and give them feedback on the same.

#### By **Sheilla Njoroge**

## Description

A user can:
* View sites submitted by other users.
* Rate other people's projects (Based on 1. Design 2.Usability 3. Content).
* Submit their own projects.

## Setup/Installation Requirements

### Requirements
* Postgresql -> See https://www.postgresql.org/download/ to download for your platform of choice.

### Setup
* Clone the repo `git clone https://github.com/sheillanjoroge/AwardsArena.git`
* Move into the directory `cd Desiiigner`
* Create a virtual environment `python -m venv virtual`
* Install all dependencies with `pip install -r requirements.txt`
* Create `.env` file and add your environment variables.
* Make migrations for the database `python manage.py migrate`
* If everything else is good. Run the application. `python manage.py runserver`

### Testing

To run tests `python manage.py test`\
For test coverage run `coverage run manage.py test`\
To view test coverage on the browser. `coverage html` then navigate the coverage folder generated and open `index.html` on the browser.\

## Known Bugs

There are no known bugs atm. Get in touch if you discover any.
## Technologies Used

* HTML
* CSS
* Bootstrap
* Python
* Django
* Heroku
* Postgresql

## Support and contact details

Reach out to me over email sheillan.njoroge@gmail.com

### MIT License

Copyright (c) 2020 AwardsArena

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Copyright (c) {2020} **Sheilla Njoroge**