from setuptools import find_packages, setup
from setuptools.command.develop import develop
import os
from glob import glob

package_name = 'semantic_sensor'


class ColconDevelopCommand(develop):
    """Compatibility wrapper for colcon's legacy setuptools develop flags."""

    user_options = develop.user_options + [
        ("editable", None, "Ignored compatibility flag from colcon."),
        ("build-directory=", None, "Ignored compatibility flag from colcon."),
        ("script-dir=", None, "Legacy setuptools develop option used by setup.cfg."),
    ]
    boolean_options = list(getattr(develop, "boolean_options", [])) + ["editable"]

    def initialize_options(self):
        super().initialize_options()
        self.editable = False
        self.build_directory = None
        self.script_dir = None

setup(
    name=package_name,
    version='2.1.0',
    packages=find_packages(include=[package_name, package_name + ".*"]),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lorenzo Terenzi',
    maintainer_email='lorenzoterenzi96@gmail.com',
    description='Semantic image and semantic pointcloud publishers for elevation_mapping_cupy',
    license='MIT',
    entry_points={
        'console_scripts': [
            'pointcloud_node = semantic_sensor.pointcloud_node:main',
            'image_node = semantic_sensor.image_node:main',
        ],
    },
    cmdclass={"develop": ColconDevelopCommand},
)
