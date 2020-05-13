import re

version = '(v?(\d+ \. )+(\d+)( [-\.] \S+)?( . \d+)?)'
package_name = '(\w+( (- )?\w+)*)'
filename = '((. )?\S+( [.-] [a-zA-Z]+)*( \. (txt|java|py|properties|md|html|png|xml|jpg|bal|yaml|yml|sh|clj|js|gradle|json|h|c|cpp|rst|markdown|adoc)))'

# Simple file update
update_file_pattern1 = re.compile(f'^updated? ({filename}|((. )?gitignore)|(readme)|(changelog)|(submodule))( \[ ci skip \])?$')
update_file_pattern2 = re.compile('zws - macpro . local ')

makefile_pattern = re.compile('^modify (makefile|dockerfile)$')
simple_delete_pattern = re.compile('^delete (. )?(\S+) . \w+$')
simple_create_pattern1 = re.compile('^created? (. )?(\S+)( . \w+)?$')
simple_create_pattern2 = re.compile(f'^add(ed)? {filename}$')

# Simple add pattern
simple_add_pattern = re.compile('^add(ed)? \S+$')

# Versioning
prepare_release_pattern1 = re.compile('^prepare (for )?(version|release|(next development (version|iteration)))')
prepare_release_pattern2 = re.compile(f'^prepare for {version}$')
prepare_release_pattern3 = re.compile('next development version')

prepare_release_pattern4 = re.compile(f'^{version}( release)?$')
prepare_release_pattern5 = re.compile(f'^release ({package_name} )?{version}$')
prepare_release_pattern6 = re.compile('^\[ maven - release - plugin \] prepare ')
prepare_release_pattern7 = re.compile(f'^upgrade[sd]? to {version}$')

prepare_release_pattern8 = re.compile(f'^\[ artifactory - release \] (next development version|release version)')
prepare_release_pattern9 = re.compile(f'^\[ gradle release plugin \] - new version commit')
prepare_release_pattern10 = re.compile(f'^\[ jboss - fuse .*] updating perfectus - build number to new build')
prepare_release_pattern11 = re.compile(f'^version {version}')
prepare_release_pattern12 = re.compile(f'^updated? version to {version}')
prepare_release_pattern13 = re.compile(f'^commit for {version}')
prepare_release_pattern14 = re.compile(f'^{version} \[ ci skip \]?$')

# Versioning
bump_version_pattern1 = re.compile('^bump(ed)? (to |version to |maven )')
bump_version_pattern2 = re.compile(f'^upgrade[d]? to {package_name} {version}$')
bump_version_pattern3 = re.compile(f'^upgrade[d]? {package_name} to {version}$')

bump_version_pattern4 = re.compile(f'^upgrade[d]? gradle plugin to {version}$')
bump_version_pattern5 = re.compile(f'^bump {package_name} (from {version} )?to {version}')
bump_version_pattern6 = re.compile(f'^version bump to {version}')
bump_version_pattern7 = re.compile(f'^\[ pom ] update {package_name} to')
bump_version_pattern8 = re.compile(f'^update[d]? {package_name} to {version}$')
bump_version_pattern9 = re.compile(f'^update[d]? to {package_name} {version}$')
bump_version_pattern10 = re.compile(f'^update[d]? {package_name} from {version} to {version}$')
bump_version_pattern11 = re.compile(f'^use {package_name} {version}$')
bump_version_pattern12 = re.compile(f'^(upgrade|update)d? {package_name} {version}$')


# Bot pattern
bot_pattern1 = re.compile('^(new version commit )|(pre tag commit )')
bot_pattern2 = re.compile(r'(zw \. 163 \. com)|(\( poeditor \. com \))')
bot_pattern3 = re.compile('^translated using weblate')
bot_pattern4 = re.compile('^lines authored by')
