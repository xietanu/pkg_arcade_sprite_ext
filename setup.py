"""Setup file for package"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arcade_sprite_ext",
    version="0.3.0",
    author="Matt Sutton",
    author_email="sutton.matt.p@gmail.com",
    description="A python package extending the functionality of sprites in the arcade package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xietanu/pkg_arcade_sprite_ext",
    project_urls={
        "Bug Tracker": "https://github.com/xietanu/pkg_arcade_sprite_ext/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["arcade>=2.6.10"],
)
