# -*- coding: utf-8 -*-
"""
"""
from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

from elixir import *
import wtforms

DATABASE = 'contact.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

metadata.bind = "sqlite:///contact.db"
metadata.bind.echo = True


class Contact(Entity):
    name = Field(Unicode(30))
    email = Field(Integer)
    message = Field(UnicodeText)

    def __repr__(self):
        return '<Contact "%s" (%d)>' % (self.name, self.email)


setup_all()
create_all()


class ContactForm(wtforms.Form):
    name = wtforms.TextField('Your Name', [wtforms.validators.Required(), wtforms.validators.Length(min=4, max=64)])
    email = wtforms.TextField('Your Email', [wtforms.validators.Required(), wtforms.validators.Email(), wtforms.validators.Length(min=4, max=64)])
    message = wtforms.TextAreaField('Your Message', [wtforms.validators.Required()])


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET','POST'])
def show_form():
    form = ContactForm(request.form)
    if form.validate():
        flash('New entry was successfully posted')
        return redirect(url_for('thanks'))
    return render_template('form.html', form=form)


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run()