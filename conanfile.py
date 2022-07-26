from conans import ConanFile, CMake

class Libsearpc(ConanFile):
    
    name = "libsearpc"
    version = "3.2-latest"
    license = ("Apache-2.0")
    author = "Barış Çelik bariscelikweb@gmail.com"
    url = "https://github.com/bariscelik/libsearpc"
    description = "Searpc is a simple C language RPC framework based on GObject system. Searpc handles the serialization/deserialization part of RPC, the transport part is left to users."
    topics = ("rpc", "serialization", "deserialization")
    settings = "os", "compiler", "build_type", "arch"
    requires = "jansson/2.14", "glib/2.72.1"
    generators = "cmake", "gcc", "txt"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True, "jansson:shared": True, "glib:shared": True}
    scm = {
        "type": "git",
        "subfolder": "libsearpc",
        "url": "https://github.com/haiwen/libsearpc.git",
        "revision": "v3.2-latest",
    }

    # copy cmake source files into libsearpc
    exports_sources = "libsearpc/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED"] = self.options.shared
        cmake.configure(source_folder="libsearpc")
        cmake.build()

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["searpc"]


