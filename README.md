# Continous Reforestation Action

[<img src="logo.svg" align="right" width="250">](https://github.com/protontypes/continuous-reforestation)
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/protontypes/continuous-reforestation/actions)
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Integration%20Test/badge.svg)](https://github.com/protontypes/continuous-reforestation/actions) <br>
This is a template for creating GitHub actions and contains a small Python application which will be built into a minimal [Container Action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-a-docker-container-action). Our final container from this template is ~50MB, yours may be a little bigger once you add some code. If you want something smaller check out my [go-container-action template](https://github.com/jacobtomlinson/go-container-action/actions).

In `main.py` you will find a small example of accessing Action inputs and returning Action outputs. For more information on communicating with the workflow see the [development tools for GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/development-tools-for-github-actions).

> 🏁 To get started, click the `Use this template` button on this repository [which will create a new repository based on this template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/).

## Use cases

* Have a scheduled tree-plant (i.e. once per week)
* plant trees on pull requests (and/or push, ...)
* plant trees on linter fails (as self-motivation)
  * or on sucess ;)
* Plant tree for first ever contribution
* on release
* on milestone
* on closed issue (or opened, ...)

See more possible trigger events [here](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).

## Usage

Describe how to use your action here.

### Example workflow

```yaml
name: Integration Test
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      
      - uses: protontypes/continuous-reforestation@main
        with:
        # Enter your API variables below
            enterpriseid: "cd7cedcd"
            user: ${{ github.actor }}
            treecount: 10
            projectid: "91919191"
            production: "false"

      - name: Response of digitalhumani.com RaaS API
        run: |
            echo "${{ steps.selftest.outputs.response }}"
```
---

### Inputs

| Input            | Description                           |
|------------------|---------------------------------------|
| `treecount`      | Numbers of trees you want to plant.   |
| `projectid`      | An example optional input             |
| `user`           | The user name you want to use to plant trees. Default is your GitHub user name.   |
| `enterpriseId`   | Is a secret ptional input             |
| `authSecret`     | An example optional input             |
| `production`     | An example optional input             |

### Outputs

| Output               | Description                           |
|----------------------|---------------------------------------|
| `response`           | JSON response of the RaaS API plant   |
