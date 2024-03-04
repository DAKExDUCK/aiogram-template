import dotenv

from modules.utils.config_utils import get_from_env


dotenv.load_dotenv()

TOKEN = get_from_env("TOKEN")

