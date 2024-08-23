import ckan.lib.helpers as h
import ckan.plugins.toolkit as toolkit
import ckan.plugins as plugins


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