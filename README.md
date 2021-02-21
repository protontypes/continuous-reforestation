# Continous Reforestation Action

[<img src="logo.svg" align="right" width="250">](https://github.com/protontypes/continuous-reforestation)
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/protontypes/continuous-reforestation/actions)
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Integration%20Test/badge.svg)](https://github.com/protontypes/continuous-reforestation/actions) <br>

This is a GitHub actions for planting trees within your development workflow. It uses the Reforestation as a Service (RaaS) API developed by [DigitalHumani](https://digitalhumani.com/).
It provides simple and easy to use API to help connect websites and mobile applications to trusted reforestation organizations to have trees planted, or in this case, have them planted by GitHub events.

Planting trees is an easy way to make a small difference in the fight against climate change. Every tree helps in capturing CO2 is long as it grows. Automating the process gives you total control of where, when and how much you want to contribute while saving you the fuss of doing the whole process manually. By using the Raas API, you or your company can plant trees in a transparent way. 

Below you find inspiration for use cases and an example of how to integrate it into your workflows.

> 🏁 To get started, click the `Use this template` button on this repository [which will create a new repository based on this template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/).

## Use cases

* Have a scheduled tree-plant (i.e. once per week)
* Plant trees on pull requests (and/or push, ...)
* Plant trees on linter fails or sucesses (as self-motivation)
* Plant tree for first ever contribution
* Or on a new release, or milestone, or closed issue

See more possible trigger events [here](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).

## Usage

To get started, you need an account with DigitalHumani RaaS. Since they are currently in the early stages, you have to contact them to get an account. Send them an email [here](https://digitalhumani.com/#contact).

When your workflow is integrated on your repository, you need to change the API variables in the `.github/workflow/integration.yaml`.

To see a list of all possible projects check the list [here](https://digitalhumani.com/docs/#appendixlist-of-projects).

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
            enterpriseid: "<your enterpriseid>"
            user: ${{ github.actor }}
            treecount: 10
            projectid: "<the project for planting the trees>"
            production: "false"

      - name: Response of digitalhumani.com RaaS API
        run: |
            echo "${{ steps.selftest.outputs.response }}"
```
---

### Inputs

| Input            | Description                           |
|------------------|---------------------------------------|
| `enterpriseid`   | Id of your enterprise.                |
| `user`           | End user by whom the trees were planted. Default is your GitHub user name. |
| `projectid`      | Id of the reforestation project for where you want the trees to be planted.    |
| `treeCount`      | Number of trees requested to plant.   |
| `production`     | Use sandbox or production API         |

### Outputs

| Output           | Description                           |
|------------------|---------------------------------------|
| `response`       | JSON response of the RaaS API plant   |
