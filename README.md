<!--

    Copyright 2019-Present Sonatype Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->

# OSS Index API Client(s)

[![CI](https://github.com/sonatype-nexus-community/ossindex-api-client/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/sonatype-nexus-community/ossindex-api-client/actions/workflows/build.yaml)
[![GitHub license](https://img.shields.io/github/license/sonatype-nexus-community/ossindex-api-client)](https://github.com/sonatype-nexus-community/ossindex-api-client/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/sonatype-nexus-community/ossindex-api-client)](https://github.com/sonatype-nexus-community/ossindex-api-client/issues)
[![GitHub forks](https://img.shields.io/github/forks/sonatype-nexus-community/ossindex-api-client)](https://github.com/sonatype-nexus-community/ossindex-api-client/network)
[![GitHub stars](https://img.shields.io/github/stars/sonatype-nexus-community/ossindex-api-client)](https://github.com/sonatype-nexus-community/ossindex-api-client/stargazers)

----

This repository produces generated API Clients in various languages and frameworks for use by Customers, other projects and interested parties.

## Supported Languages & Frameworks

| Language / Framework | Since | Public Package Link |
| -------------------- | ---------------------- | ------------------- |
| Go | 2025-01-15 | [![go.dev reference](https://img.shields.io/badge/dynamic/json?color=blue&label=tag&query=name&url=https://api.razonyang.com/v1/github/tag/sonatype-nexus-community/ossindex-api-client-go)](https://pkg.go.dev/github.com/sonatype-nexus-community/ossindex-api-client-go) |
| Python | 2024-11-15 | [![PyPI - Version](https://img.shields.io/pypi/v/ossindex-api-client)](https://pypi.org/project/ossindex-api-client/) | 
| Typescript (fetch)   | 2023-05-22 | [![npm](https://img.shields.io/npm/v/%40sonatype%2Fossindex-api-client)](https://www.npmjs.com/package/@sonatype/ossindex-api-client) |

## Known Issues

### APIs Excluded from Generation

*None*

## Getting the latest OpenAPI Schema

Create a Python Virtual Environment with Poetry and then run:

```
poetry install
python update-spec.py
```

This will download the current Swagger 2.0 specification, convert to OpenAPI 3, add a few tweaks and put it into the `spec` folder.

## Generation of API Clients

```
docker run --rm -v "$(PWD):/local" openapitools/openapi-generator-cli batch --clean /local/typescript.yaml

docker run --rm -v "$(PWD):/local" openapitools/openapi-generator-cli generate -i /local/spec/openapi.yaml -g typescript-fetch -o /local/out/test -c /local/openapi-config.yaml -v > out.log
```

## Releasing

We use [semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) to generate releases from commits to the `main` branch.

For example, to perform a "patch" release, add a commit to `main` with a comment like below. The `fix: ` prefix matters.

```
fix: the problem resolved goes here
```

## The Fine Print

Remember:

It is worth noting that this is **NOT SUPPORTED** by Sonatype, and is a contribution of ours to the open source
community (read: you!)

* Use this contribution at the risk tolerance that you have
* Do NOT file Sonatype support tickets related to `ossindex-api-client`
* DO file issues here on GitHub, so that the community can pitch in

Phew, that was easier than I thought. Last but not least of all - have fun!