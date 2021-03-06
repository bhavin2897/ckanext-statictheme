import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

''' To display repository's dataset on the home page'''
def repositories_present(data_dict = None):

    org =  toolkit.get_action('organization_list')(
       data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})
    return org


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
        return {'repositories_present': repositories_present}