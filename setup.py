from setuptools import setup

setup(
    name="matrix_synapse_rest_auth_provider",
    version="0.0.1",
    py_modules=['matrix_synapse_rest_auth_provider'],
    description="Rest auth provider for Matrix Synapse",
    include_package_data=False,
    zip_safe=True,
    install_requires=["twisted", "requests"],
)
