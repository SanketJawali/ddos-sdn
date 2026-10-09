from os_ken.base import app_manager

from controller import SimpleController


if __name__ == "__main__":
    app_manager.AppManager.run_apps(
        ["controller"]
    )
