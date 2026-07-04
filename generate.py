from utils import run_command


def generate_api(package_name: str, swagger_url: str, templates: str | None = None) -> None:
    command = [
        "java", "-jar", "openapi-generator-cli-7.23.0.jar",
        "generate","-i",swagger_url,
        "-g", "python",
        "-o", package_name,
        "--library", "asyncio",
        "--package-name", package_name,
        "--skip-validate-spec",
    ]
    if templates:
        command.extend(["-t", templates,])
    run_command(command)

generate_api(package_name="register_service",
             swagger_url="http://185.185.143.231:8085/register/openapi.json",
)
