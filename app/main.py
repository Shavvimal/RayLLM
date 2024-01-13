from ray import serve
from ray.serve.handle import DeploymentHandle
from fastapi import FastAPI
from pydantic import BaseModel
from app.flan_t5 import FlanT5


class Prompt(BaseModel):
    prompt: str


# Define a FastAPI app & wrap it in a deployment with a route handler.
# Define a FastAPI app & wrap it in a deployment with a route handler.
app = FastAPI(
    title="Test LLM API",
    description="LLM API Demo",
    version="0.1.0"
)


@serve.deployment
@serve.ingress(app)
class API:
    def __init__(
            self,
            flan_t5: DeploymentHandle = None,
    ):
        self.flan_t5: DeploymentHandle = flan_t5.options(
            use_new_handle_api=True)

    @app.get("/")
    async def root(self):
        return "Welcome to the LLM API"

    @app.post("/flan-t5")
    async def llm(self, request: Prompt) -> str:
        prompt = request.prompt
        output = await self.flan_t5.generate.remote(prompt)
        return output


app = API.bind(FlanT5.bind())
