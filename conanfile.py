from conans import ConanFile, CMake
import os

def get_requires():
    requires = [ "qt/6.0.4" ]
    return requires

class TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = get_requires()
    generators = "cmake", "virtualrunenv", "cmake_find_package", "cmake_find_package_multi"
    default_options = {"qt:qtdeclarative": True,
                       "qt:qtquickcontrols2": True,
                       "qt:qtsvg": True,
                       "qt:qttools": True,
                       "qt:qttranslations": True,
                       "qt:with_harfbuzz": False,
                       "qt:opengl": "dynamic"}

    def config_options(self):
       if self.settings.os == "Macos":
           del self.options["qt"].opengl


