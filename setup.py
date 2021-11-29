from setuptools import setup

setup(
    name="rename",
    version='0.0.1',
    py_modules=["rename"],
    entry_points={"console_scripts": ["rename=rename:main"]},
)
