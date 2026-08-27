# Nihongo Dojo (Django version)

The same Japanese learning app as the Flask version, rebuilt with Django.

## Features
- Hiragana and Katakana reference charts (base + voiced sounds), hover a
  cell to reveal its romanization
- Vocabulary flashcards (~50 JLPT N5 words) with category filters, click
  to flip
- A server-generated multiple-choice quiz (hiragana / katakana / vocabulary)
  with a running score, stored in Django's session

## Setup and run

```bash
pip3 install -r requirements.txt
python3 manage.py migrate     # creates db.sqlite3 (needed for session storage)
python3 manage.py runserver
```

Then open http://127.0.0.1:8000 in your browser.

## Project layout
```
manage.py                  Django's command-line utility
nihongo_project/           Project settings and root URL config
dojo/                       The app
  data.py                   Kana tables and vocabulary data (same as Flask version)
  views.py                  Route handlers and quiz logic
  urls.py                   App-level URL routes
  templates/dojo/           HTML templates
  static/dojo/css/style.css Styling
```

## Notes on the Django-specific bits
- Score and current question are stored in `request.session`, Django's
  built-in per-visitor session store (backed by the `db.sqlite3` file
  created by `migrate`).
- Forms use `{% csrf_token %}`, which Django requires on every POST form
  for security. Flask doesn't enforce this by default, which is the main
  template difference between the two versions.
- `DEBUG = True` and a placeholder `SECRET_KEY` are set in
  `nihongo_project/settings.py` for local development only — change both
  before deploying anywhere public.

