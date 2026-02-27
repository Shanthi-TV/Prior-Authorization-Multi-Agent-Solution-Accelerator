# Next Steps after `azd init`

## Table of Contents

1. [Next Steps](#next-steps)
2. [What was added](#what-was-added)
3. [Billing](#billing)
4. [Troubleshooting](#troubleshooting)

## Next Steps

### Provision infrastructure and deploy application code

Run `azd up` to provision your infrastructure and deploy to Azure
(or run `azd provision` then `azd deploy` to accomplish the tasks separately).
Visit the service endpoints listed to see your application up-and-running!

To troubleshoot any issues, see [troubleshooting](#troubleshooting).

### Configure CI/CD pipeline

Run `azd pipeline config` to configure the deployment pipeline to connect securely to Azure.

- Deploying with `GitHub Actions`: Select `GitHub` when prompted for a provider. If your project lacks the `azure-dev.yml` file, accept the prompt to add it and proceed with pipeline configuration.

- Deploying with `Azure DevOps Pipeline`: Select `Azure DevOps` when prompted for a provider. If your project lacks the `azure-dev.yml` file, accept the prompt to add it and proceed with pipeline configuration.

## What was added

### Infrastructure configuration

To describe the infrastructure and application, `azure.yaml` along with Infrastructure as Code files using Bicep were added with the following directory structure:

```yaml
- azure.yaml        # azd project configuration
- infra/             # Infrastructure-as-code Bicep files
  - main.bicep       # Subscription level resources
  - modules/         # Library modules
    - container-registry.bicep
    - monitoring.bicep
    - container-apps-env.bicep
    - container-app.bicep
```

The resources declared in `main.bicep` are provisioned when running `azd up` or `azd provision`. This includes:

- Azure Container Registry to store container images.
- Azure Log Analytics workspace and Application Insights for monitoring.
- Azure Container Apps Environment for hosting the services.
- Azure Container Apps for the `backend` and `frontend` services.

More information about [Bicep](https://aka.ms/bicep) language.

### Build from source (Dockerfile)

This project includes Dockerfiles for both the backend and frontend services. When running `azd up`, the Docker images are built and pushed to Azure Container Registry, then deployed to Azure Container Apps.

To produce and run the Docker images locally:

1. Run `docker compose build` to build the images.
2. Run `docker compose up` to start the services locally.

## Billing

Visit the *Cost Management + Billing* page in Azure Portal to track current spend. For more information about how you're billed, and how you can monitor the costs incurred in your Azure subscriptions, visit [billing overview](https://learn.microsoft.com/azure/developer/intro/azure-developer-billing).

## Troubleshooting

Q: I visited the service endpoint listed, and I'm seeing a blank page, a generic welcome page, or an error page.

A: Your service may have failed to start, or it may be missing some configuration settings. To investigate further:

1. Run `azd show`. Click on the link under "View in Azure Portal" to open the resource group in Azure Portal.
2. Navigate to the specific Container App service that is failing to deploy.
3. Click on the failing revision under "Revisions with Issues".
4. Review "Status details" for more information about the type of failure.
5. Observe the log outputs from Console log stream and System log stream to identify any errors.
6. If logs are written to disk, use *Console* in the navigation to connect to a shell within the running container.

For more troubleshooting information, visit [Container Apps troubleshooting](https://learn.microsoft.com/azure/container-apps/troubleshooting).

### Additional information

For additional information about setting up your `azd` project, visit our official [docs](https://learn.microsoft.com/azure/developer/azure-developer-cli/make-azd-compatible?pivots=azd-convert).
