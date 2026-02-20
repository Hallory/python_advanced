from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    app_name: str = "community-pulse"
    debug: bool = False

    mysql_host: SecretStr = SecretStr("localhost")
    mysql_port: int = 3306
    mysql_user: SecretStr = SecretStr("root")
    mysql_password: SecretStr = SecretStr("")
    mysql_database: str = "community_pulse"
    mysql_pool_size: int = 5
    mysql_pool_timeout: int = 30

    api_prefix: str = "/api"
    api_version: str = "v1"
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    @property
    def database_url(self) -> str:
        user = (self.mysql_user.get_secret_value() or "root")
        password = (self.mysql_password.get_secret_value() or "")
        host = (self.mysql_host.get_secret_value() or "localhost")
        port = self.mysql_port or 3306
        database = self.mysql_database or "community_pulse"

        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        
    def get_flask_config(self)-> dict[str, any]:
        return {
            "DEBUG": self.debug,
            "SQLALCHEMY_DATABASE_URI": self.database_url,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "SQLALCHEMY_POOL_SIZE": self.mysql_pool_size,
            "SQLALCHEMY_POOL_TIMEOUT": self.mysql_pool_timeout
        }
        

settings = Settings()