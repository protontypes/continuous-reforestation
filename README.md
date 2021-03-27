# Continuous Reforestation
**Make tree planting a part of your daily workflow. :deciduous_tree:** 

[<img src="logo.svg" align="right" width="250">](https://github.com/protontypes/continuous-reforestation)
A GitHub Action for planting trees within your development workflow using the Reforestation as a Service (RaaS) API developed by [DigitalHumani](https://digitalhumani.com/). 

Planting trees is an easy way to make a difference in the fight against climate change. Every tree helps to bind CO2 as long as it grows and creates living space for wildlife. Automating the process gives you total control of where, when and how much you want to contribute while saving you the fuss of doing the whole process manually. By using the RaaS API, you or your project can plant trees in a transparent way by exposing the API calls and related statistics. The RaaS API is completely free of charge. You only pay for the trees (1 $ each) directly to the reforestation organization. Find more information on this project read our [blog post](https://protontypes.eu/blog/2021/03/25/continuous-reforestation/). <br>  <br>
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/protontypes/continuous-reforestation/actions)
[![Actions Status](https://github.com/protontypes/continuous-reforestation/workflows/Integration%20Test/badge.svg)](https://github.com/protontypes/continuous-reforestation/actions)
[![](https://badgen.net/badge/icon/Community%20Chat/green?icon=gitter&label)](https://gitter.im/protontypes/community)

## Use cases
Plant trees on ...
* pull requests (and/or push, ...).
* failed or successful tests.
* the very first contribution to an open source project.
* a new release, a milestone, or a closed issue.
* a scheduled event (i.e. once per week).
* the carbon footprint of your digital products after deployment.

See more possible trigger events [here](https://docs.github.com/en/actions/reference/events-that-trigger-workflows).

## Usage

1. 🏁 To get started, you need an account with DigitalHumani RaaS. Since they are currently in the early stages, you have to contact them to get an account. Send them an email [here](https://digitalhumani.com/#contact). You also receive the API key value corresponding for your enterprise ID. This is your secret authentication key. **Do not add your API key to your workfile yaml file**.

2. ✂️ Copy the example worflow to `<your_git_repository>/.github/workflow/integration.yaml` and change the variables in the workflow to your data. Set the `production` variable to `false` to test your implementation within the sandboxed development API. Push your script to GitHub and check the GitHub Action tab of your project. If you use GitHub Action for the first time, activate it when prompted.

3. 📈 An open dashboard is provided to ensure a high level of transparency. This is currently under development and will show additional details. For this purpose visit:
``
https://digitalhumani.com/dashboard/<enterpriseid>
``

4. 🗝️ Add your authentication key as a secret in your repository `Settings` -> `Secrets` -> `New Repository Secret`: Name: `RAASKEY`, Value: `<your API key>`. You can also add it as an organization wide secret in the setting of your organization.

5. 🌱 Verify the number of trees planted in the dashboard development statistics. Set the `production` variable to `true` and push this commit. You now have left the development environment and started planting trees. From now on every configured trigger will continuously request to plant trees. At the end of each month you will be asked to confirm your requested amount of trees.

To see a list of all supported reforestation projects and more details on the RaaS API read the [documentation of DigitalHumani](https://digitalhumani.com/docs/#appendixlist-of-projects).

**Disclaimer:** Even though this workflow automates the request to plant trees, the planting process itself remains manual labour by the reforestation organisations. They are also the people who write your invoice. Due to the amount of work it requires to write these invoices, DigitalHumani accumulates your plant requests until you reach a certain number, depending on your chosen reforestation project, before issuing the order. Below are the least required amounts to receive a monthly invoice and actually plant trees. If you plant more, don't mind this disclaimer.

| Reforestation project | Necessary number of requested trees |
| --------------------- | ----------------------------------- |
| Chase Africa | 20 |
| Conserve Natural Forests | 20 |
| OneTreePlanted | 1 |
| Sustainable Harvest International | 50 |
| TIST | 20 | 

### Example workflows

```yaml
name: Plant a tree on a successful merged pull request to your main branch
on: 
  pull_request_target:
    branches:
      - main
    types:
      - closed
jobs:
  planttrees:
    runs-on: ubuntu-latest
    steps:
      - name: Plant a Tree
        if: github.event.pull_request.merged == true
        id: planttrees
        uses: protontypes/continuous-reforestation@main
        with:
        # Enter your API variables below
            apikey: ${{ secrets.raaskey }}
            enterpriseid: "<your_enterprise_ID>"
            user: ${{ github.actor }}
            treecount: 1
            projectid: "14442771" # This projectid can be used to have your trees planted where they are needed the most.
            production: "true"

      - name: Response of digitalhumani.com RaaS API
        run: |
            echo "${{ steps.planttrees.outputs.response }}"
```

```yaml
name: Plant a tree on every push to main
on:
  push:
    branches:
      - main
jobs:
  planttrees:
    runs-on: ubuntu-latest
    steps:
      - name: Plant a Tree
        id: planttrees
        uses: protontypes/continuous-reforestation@main
        with:
        # Enter your API variables below
            apikey: ${{ secrets.raaskey }}
            enterpriseid: "<your_enterprise_ID"
            user: ${{ github.actor }}
            treecount: 1
            projectid: "14442771" # This projectid can be used to have your trees planted where they are needed the most, so this is a great ID to use by default when making the API call. 
            production: "true"

      - name: Response of digitalhumani.com RaaS API
        run: |
            echo "${{ steps.planttrees.outputs.response }}"
```
---
### Inputs

| Input            | Description                           |
|------------------|---------------------------------------|
| `apikey`         | Your API secret key to the digitalhumani.com RaaS API. |
| `enterpriseid`   | ID of your enterprise.                |
| `user`           | End user by whom the trees were planted. Default is your GitHub user name. |
| `projectid`      | ID of the reforestation project for where you want the trees to be planted.    |
| `treecount`      | Number of trees requested to plant per API call as integer. Every tree will create costs of $1 per tree. |
| `production`     | Set `true` for the production API or false for the development API. |

### Outputs

| Output           | Description                           |
|------------------|---------------------------------------|
| `response`       | JSON response of the RaaS API |
