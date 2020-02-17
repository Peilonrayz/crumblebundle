import enum
from pprint import pprint

from .item_values import value, item_value, option, multiple
from .dependency import dependency


class TagType(enum.Enum):
    LANGUAGE = 'language'
    FEATURE = 'feature'


dependency.tags.extend([
    ('python', TagType.LANGUAGE),
    ('javascript', TagType.LANGUAGE),
    ('cli', TagType.FEATURE),
    ('web', TagType.FEATURE)
])

value('package:meta.author_name', 'package.user.name', 'John Doe')
value('package:meta.author_email', 'package.user.email', 'john.doe@example.com')
value('package:meta.name', 'package.name', 'example-project')
value('package:meta.version', 'package.version', '0.0.0')
multiple('package:meta.license', 'package.license', ['none', 'mit', 'cc by-sa'])
value('package:meta.release_date', 'package.release_date', 'today')
value('package:meta.year', 'package.year', "{% now 'utc', '%Y' %}", extensions=['jinja2_time.TimeExtension'])
value('package:meta.description', 'package.description', 'a CrumbleBundle example project')


@item_value('package:hosts.github')
def package_host_github(input):
    return {
        'package': {
            'host': {
                'name': 'github',
                'user_name': input.value('Github Username', 'package.host.user_name', 'jhon_doe'),
                'repo_name': input.value('Github Repo Name', 'package.host.repo_name', "{{ cookiecutter.package.name|lower|replace(' ','-') }}")
            }
        }
    }


config = {
    'package': {
        'user': {
            'name': 'Peilonrayz',
            'email': 'pelionrayz@gmail.com'
        },
        'host': {
            'user_name': "{{ cookiecutter.package.user.name|lower|replace(' ', '_') }}"
        }
    }
}


if __name__ == '__main__':
    # pprint(dependency.fns)
    dep = dependency.build(config)
    # pprint(dep.fns)
    inst = dep.run()
    pprint(inst.cookiecutter)

