import httpx
from enum import Enum

SIEU_NHAN_API_BASE = 'https://script.google.com/macros/s/AKfycbyGg3Wk3hWnLTGw_PLkNTFqAhpdln-pg9tkJlBGLn8MafiElQsi89QwtEQP2GfFMBxQ/exec'

class SieuNhanTools(str, Enum):
    GET_SIEU_NHAN = 'get_sieu_nhan'

async def get_sieu_nhan():
    """
    Get a random superhero from the API.
    """
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(SIEU_NHAN_API_BASE)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data
        except httpx.RequestError as e:
            print(f"An error occurred while requesting the API: {e}")
            return None


async def get_sieu_nhan_tools() -> str:
    """
    Get a random superhero from the API and format it for display.
    """
    data = await get_sieu_nhan()
    if data:
        image_url = data.get('image')

        # Format the output
        output = f"{image_url}"
        return output
    else:
        return "Failed to retrieve superhero data."
