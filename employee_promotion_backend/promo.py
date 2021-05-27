from employee_promotion_backend.models.models import Employee
import flask
from flask import Flask, request, jsonify, render_template
from flask import current_app

import os
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token,  get_current_user, get_jti, get_raw_jwt
import logging as log

from werkzeug.exceptions import InternalServerError
from flask_restful import reqparse, Resource, Api, abort
from .models.models import *
from threading import Thread
import bcrypt
import datetime
import random
import string
from flask_mail import Mail, Message
import re
from functools import wraps
from flask_cors import cross_origin
from datetime import date
from .templates import *

app = Flask(__name__)

def send_async_email(app, msg):
    app.app_context().push()
    with app.app_context():
        try:
            mail = Mail(app)
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.recipients = recipients
    msg.body = text_body
    msg.html = html_body
    app = current_app._get_current_object()
    Thread(target=send_async_email, args=(app, msg)).start()

def promo(employee : Employee):
    statut =  employee.grade
    grade_seniority = employee.grade_seniority
    grade = employee.degree
    #today = date.today()
    #seniority = today.year - employee.entry_date.year - ((today.month, today.day) < (employee.entry_date.month, employee.entry_date.day))

    if statut=="redacteur" or "adjoint administratif" or "adjoint technique" or "technicien":
        if grade_seniority>=10 :
            send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                       sender='redaabdou49@gmail.com',
                       recipients=[employee.email],
                       text_body=render_template('promo.txt',employee = employee),
                       html_body=render_template('promo.html',employee = employee)
                       ) 
    
    if statut=="ingénieur d'état":
        if grade=="1" :
            if grade_seniority>=5 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )
        else:
            if grade_seniority>=6 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )
    
    if statut=="ingénieur en chef":
        if grade=="1" :
            if grade_seniority>=6 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )
    
    if statut=="architecte":
            if grade_seniority>=6 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )
    
    if statut=="professeur de formation":
        if grade=="3" :
            if grade_seniority>=10 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )
        else:
            if grade_seniority>=5 :
                send_email("Possibilité d'une promotion pour le fonctionnaire {0} {1}".format(employee.last_name,employee.first_name),
                        sender='redaabdou49@gmail.com',
                        recipients=[employee.email],
                        text_body=render_template('promo.txt',employee = employee),
                        html_body=render_template('promo.html',employee = employee)
                        )