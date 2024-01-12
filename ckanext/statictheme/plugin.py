import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def repositories_present():
    org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})

    return org


def repositories_count():
    list_org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})

    count_to_display = len(list_org)

    return count_to_display


def dataset_count():
    package_list = toolkit.get_action('package_list')({},{})

    count_to_display = len(package_list)

    return count_to_display


class StaticthemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'statictheme')

    def get_helpers(self):
        return {'repositories_present': repositories_present,
                'repositories_count': repositories_count,
                'dataset_count':  dataset_count,}
