# Continous Reforestation Action


This is a GitHub actions for planting trees within your development workflow. It uses the Reforestation as a Service (RaaS) API developed by [DigitalHumani](https://digitalhumani.com/).
It provides simple and easy to use API to help connect websites and mobile applications to trusted reforestation organizations to have trees planted, or in this case, have them planted by GitHub events.

Planting trees is an easy way to make a small difference in the fight against climate change. Every tree helps in capturing CO2 is long as it grows. Automating the process gives you total control of where, when and how much you want to contribute while saving you the fuss of doing the whole process manually. By using the Raas API, you or your company can plant trees in a transparent way. 

Below you find inspiration for use cases and an example of how to integrate it into your workflows.


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
