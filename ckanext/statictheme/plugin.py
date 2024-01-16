import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def repositories_present():
    """ Datasets present in the repositories list. """
    org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})
    return org


def repositories_dataset_count():
    """Number of repositories in CKAN organizations &
    Number of datasets in the repositories list. """
    each_repo_count = []
    list_org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})
    count_to_display_repo = len(list_org)

    for package_count in list_org:
        each_repo_count.append(package_count['package_count'])

    count_to_display_dataset = sum(each_repo_count)

    return count_to_display_repo,count_to_display_dataset


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
                'repositories_dataset_count': repositories_dataset_count, }
                # 'dataset_count':  dataset_count,}
