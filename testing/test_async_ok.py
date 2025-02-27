import sys
from pathlib import Path
import asyncio

sys.path.append(str(Path(__file__).parent.parent))

import g4f
from g4f.Provider import AsyncProvider
from testing.test_providers import get_providers
from  testing.log_time import log_time_async

async def create_async(provider: AsyncProvider):
    model = g4f.models.gpt_35_turbo.name if provider.supports_gpt_35_turbo else g4f.models.default.name
    try:
        response =  await log_time_async(
            provider.create_async,
            model=model,
            messages=[{"role": "user", "content": "write a long story"}],
            stream=True,
        )
        assert type(response) is str
        assert len(response) > 0
        return response
    except Exception as e:
        return e



async def run_async():
    _providers: list[AsyncProvider] = [
        _provider
        for _provider in get_providers()
        if _provider.working and hasattr(_provider, "create_async")
    ]
    tasks = [create_async(_provider) for _provider in _providers]
    for idx, task in enumerate(asyncio.as_completed(tasks)):
        response = await task
        print(f"{_providers[idx].__name__}: {response}")


print("Total:", asyncio.run(log_time_async(run_async)))

