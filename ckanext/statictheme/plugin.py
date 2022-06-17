import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


#trying =  data_dict.update(data_dict.setdefault('type','repository'))

def repositories_present(data_dict = None):

    org =  toolkit.get_action('organization_list')(
       data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})
    return org

def repository_show(data_dict=None):
    repo_name = repositories_present()
    packages_of_repo = toolkit.get_action('organization_show')(
        data_dict = {'id': 'massbank'}
    )
    return packages_of_repo


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
                'repository_show': repository_show}