from __future__ import annotations

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.statictheme import views
from ckanext.statictheme import helpers

from flask import Blueprint, render_template, session , request, abort


class StaticthemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)

    # IFacets
    def _facets(self, facets_dict, package_type):
        if 'groups' in facets_dict:
            del facets_dict['groups']
            # del facets_dict['tags']

        return facets_dict

    def dataset_facets(self, facets_dict, package_type):

        if package_type == 'molecule_view':
            facets_dict = {'organization': 'Repositories',
                           'measurement_technique': 'Measurement Technique',
                           'tags': 'Tags',
                           'license_id': 'License'}
        else:
            facets_dict = {'organization': 'Repositories',
                           'measurement_technique': 'Measurement Technique',
                           'tags': 'Tags',
                           'license_id': 'License'}
        return self._facets(facets_dict, package_type)

    def group_facets(self, facets_dict, group_type, package_type):
        return self._facets(facets_dict, package_type)

    def organization_facets(self, facets_dict, organization_type,
                            package_type):
        return self._facets(facets_dict, package_type)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'ckanext-statictheme')


    # ITemplateHelpers
    def get_helpers(self):
        return {
            'repositories_dataset_present_count': helpers.repositories_dataset_present_count
            # 'repositories_present': repositories_present,
            # 'dataset_count':  dataset_count,
        }

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()

    # IPackageController
    def before_search(self, search_params):
        if "+dataset_type:molecule" in search_params["fq"]:
            search_params['sort'] = 'title_string asc'
        return search_params
