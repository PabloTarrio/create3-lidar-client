__all__ = ["ScanClient", "ScanClientConfig"]
__version__ = "0.1.0"


def __getattr__(name: str):
    if name in ("ScanClient", "ScanClientConfig"):
        try:
            from .scan_client import ScanClient, ScanClientConfig
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "ROS 2 Python packages not found (e.g., rclpy). "
                "Install ROS 2 and source the environment before using ScanClient."
            ) from e
        return {"ScanClient": ScanClient, "ScanClientConfig": ScanClientConfig}[name]
    raise AttributeError(name)
