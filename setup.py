from setuptools import setup
setup(
    name="armaan-transfer",
    version="0.1.0",
    packages=["quicktransfer"],
    package_dir={"": "src"},
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": ["armaan-transfer=quicktransfer.transfer:main"]
    },
)
