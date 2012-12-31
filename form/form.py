# -*- coding: utf-8 -*-
"""
"""
from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack, jsonify

from crossdomain import crossdomain

from elixir import *
import wtforms

DATABASE = 'contact.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
BASE_SITE = 'http://localhost:8000'

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
@crossdomain(origin='*')
def show_form():
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate():
            flash('New entry was successfully posted')
            Contact(name=form.name.data, email=form.email.data, message=form.message.data)
            session.commit()
            return redirect(url_for('thanks'))
        else:
            return jsonify(**form.errors), 400

    return render_template('form.html', form=form)


@app.route('/thanks')
@crossdomain(origin='*')
def thanks():
    return jsonify(message='Thanks for your message, we will get back to you ASAP.')


if __name__ == '__main__':
    app.run()