# conan-libsearpc
Conan package for searpc library.

## Create package

Create conan package from conanfile.py and save into local cache:

```
conan create .
```

## Add remote

Add your package registry server url as remote:

```
conan remote add <remote_name> <url>
```

## Upload to remote

Upload local changes/builds to remote:

```
conan upload libsearpc/3.2-latest -r <remote_name> --all
```