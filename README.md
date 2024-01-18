# Deploying a Distributed Ray Python Server with Kubernetes, EKS & KubeRay to serve our own LLM

For Ray Serve, it is recommended in the [docs](https://docs.ray.io/en/latest/serve/production-guide/index.html) to deploy it in production on Kubernetes, with the recommended practice to use the [**RayService**](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayservice-quick-start.html#kuberay-rayservice-quickstart) controller that’s provided as part of [**KubeRay**](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html#kuberay-quickstart).

This integration offers the scalability and user experience of Ray Serve with the operational benefits of Kubernetes, including the ability to integrate with existing Kubernetes-based applications. RayService simplifies production deployment by managing health checks, status reporting, failure recovery, and updates for you.

This repo is intended to go alongside my YouTube video on the same topic:

[![Deploying a Distributed Ray Python Server with Kubernetes, EKS & KubeRay to serve our own LLM](https://img.youtube.com/vi/GEuM9rXtmkk/0.jpg)](https://www.youtube.com/watch?v=GEuM9rXtmkk)

## Getting started

Install ray:

```bash
pip install -U "ray[default, serve]"
```

Aswell as the other dependencies:

```bash
pip install -r requirements.txt
```

This is repo with minimal code to test ray deployment of a Serve deployment integrated with FastAPI.

1. Test a local `ray serve` deployment
   - `serve run app.main:app`
2. Serve Deployment Locally
   - `serve build app.main:app -o config/serve-deployment.yaml`
   - Start a local Ray cluster: `ray start --head`
   - Start the application: `serve deploy aws/serve-deployment.yaml`
   - Stop the application: `serve shutdown`
   - Stop the local Ray cluster: `ray stop`
3. Push to dockerHub:
   - `docker build . -t shavvimal/ray_llm:latest`
   - `docker image push shavvimal/ray_llm:latest`
4. Deploy on Kubernetes Locally
5. Deploy on Kubernetes on AWS

## Notes

See my [wiki](https://wiki.shav.dev/cloud-mlops/deployment/deploying-ray) for more details on the deployment process, including Log Persistence, Autoscaling, and more.
