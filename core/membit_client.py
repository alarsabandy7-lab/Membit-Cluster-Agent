import aiohttp
import os

API_KEY = os.getenv("MEMBIT_API_KEY")

async def fetch_clusters(keyword):
    url = f"https://api.membit.io/search?query={keyword}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            if res.status != 200:
                return None
            data = await res.json()
            return data.get("clusters", [])
