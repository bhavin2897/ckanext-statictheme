# encoding: utf-8

from flask import Blueprint, redirect, url_for, render_template

from ckan.plugins.toolkit import c, render, request
import ckan.lib.helpers as h


from logging import getLogger

logger = getLogger(__name__)

static_theme = Blueprint(u'statictheme', __name__)


@static_theme.route(u'/help')
def help():
    return render_template('help.html')

@static_theme.route(u'/imprint')
def imprint():
    return render_template('imprint.html')

@static_theme.route(u'/data_protection')
def dataprotection():
    return render_template('data_protection.html')

def get_blueprints():
    return [static_theme]