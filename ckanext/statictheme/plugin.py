from __future__ import annotations

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.statictheme import blueprints

from flask import Blueprint, render_template, session , request, abort


def repositories_dataset_present_count():
    """Number of repositories in CKAN organizations &
    Number of datasets in the repositories list. """
    each_repo_count = []

    list_org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})

    org = list_org
    count_to_display_repo = len(list_org)

    for package_count in list_org:
        each_repo_count.append(package_count['package_count'])

    count_to_display_dataset = sum(each_repo_count)

    return org, count_to_display_repo, count_to_display_dataset


class StaticthemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IFacets)

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
        #toolkit.add_resource('public/base', 'statictheme')


    # ITemplate Helpers
    def get_helpers(self):
        return {  # 'repositories_present': repositories_present,
            'repositories_dataset_present_count': repositories_dataset_present_count, }
        # 'dataset_count':  dataset_count,}

    # IBlueprint
    def get_blueprint(self):
        return blueprints.static_theme