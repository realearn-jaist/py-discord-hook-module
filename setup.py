from setuptools import setup, find_packages

requirements = ['discord.py']

setup(
      author="Chavakan Yimmark",
      author_email='chavakan.yim@gmail.com',
      name='discordHook',
      description='Discord webhook module for convenient use',
      packages=['discordHook'],
      package_data={"discordHook": ["savedURL.yaml", "config.cfg"]},
      python_requires='>=3.7',
      install_requires=requirements,
      url='https://github.com/realearn-jaist/py-discord-hook-module',
      version='1.0.0',
      zip_safe=False
)