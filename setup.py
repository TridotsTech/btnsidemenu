from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in btn_side_menu_custom_app/__init__.py
from btn_side_menu_custom_app import __version__ as version

setup(
	name="btn_side_menu_custom_app",
	version=version,
	description="Btn Side Menu Custom App",
	author="tridotstech",
	author_email="info@tridotstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
