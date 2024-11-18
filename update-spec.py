#
# Copyright 2019-Present Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import datetime

import requests
from yaml import dump as yaml_dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

OSS_INDEX_SPEC_PATH = 'https://ossindex.sonatype.org/swagger.json'
OSS_INDEX_VERSION_PATH = 'https://ossindex.sonatype.org/api/v3/version'

json_spec_response_v2 = requests.get(OSS_INDEX_SPEC_PATH)
json_spec_v2 = json_spec_response_v2.json()

# We need to convert from Swagger 2.0 to OpenAPI 3
json_spec_response = requests.post('https://converter.swagger.io/api/convert', json=json_spec_v2)
json_spec = json_spec_response.json()

# Get API Version from https://ossindex.sonatype.org/api/v3/version
api_version_response = requests.get(OSS_INDEX_VERSION_PATH)
api_version = api_version_response.json()

# Has to be of the form X.Y.Z - so we go with:
# X == YEAR
# Y == DAY OF YEAR
# Z == BugFix
OSS_INDEX_API_VERSION = datetime.datetime.now().strftime('%Y.%j')

# Update OpenAPI Info Block
print('Updating `info`')
json_spec['info'] = {
    'title': 'Sonatype OSS Index',
    'description': 'This documents the available APIs into [Sonatype OSS Index]'
                   '(https://ossindex.sonatype.org/) - API Version: ' + api_version.get('version') +
                   ' (' + api_version.get('buildTag') + ').',
    'contact': {
        'name': 'Sonatype Community Maintainers',
        'url': 'https://github.com/sonatype-nexus-community'
    },
    'license': {
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
    },
    'termsOfService': 'https://ossindex.sonatype.org/tos',
    'version': OSS_INDEX_API_VERSION
}

print('Injecting correct `servers`')
json_spec['servers'] = [
    {
        'url': 'https://ossindex.sonatype.org'
    }
]

# Fix Response Schemas
vuln_response = {
    'application/json': {
        'schema': {
            'type': 'array',
            'items': {
                '$ref': '#/components/schemas/ComponentReport'
            }
        }
    },
    'application/vnd.ossindex.component-report-request.v1+json': {
        'schema': {
            'type': 'array',
            'items': {
                '$ref': '#/components/schemas/ComponentReport'
            }
        }
    }
}
json_spec['paths']['/api/v3/component-report']['post']['responses']['200']['content'] = vuln_response
json_spec['paths']['/api/v3/authorized/component-report']['post']['responses']['200']['content'] = vuln_response

# Add `securitySchemes` under `components`
if 'components' in json_spec and 'securitySchemes' in json_spec['components'] and 'basicAuth' not in \
        json_spec['components']['securitySchemes']:
    print('Adding `basicAuth` to `securitySchemes`...')
    json_spec['components']['securitySchemes']['basicAuth'] = {
        'type': 'http',
        'scheme': 'basic'
    }

with open('./spec/openapi.yaml', 'w') as output_yaml_specfile:
    output_yaml_specfile.write(yaml_dump(json_spec))
