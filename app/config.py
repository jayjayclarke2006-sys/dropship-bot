from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///products.db"
    check_interval_minutes: int = 60
    min_margin: float = 0.25
    min_score: float = 0.45

    seller_id: str = ""
    marketplace_id: str = "A1F83G8C2ARO7P"

    amazon_lwa_client_id: str = ""
    amazon_lwa_client_secret: str = ""
    amazon_refresh_token: str = ""
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_role_arn: str = ""

    supplier_api_base_url: str = ""
    supplier_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
