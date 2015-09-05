from types import ModuleType


def test_import():
    import {{cookiecutter.name}}
    assert isinstance({{cookiecutter.name}}, ModuleType)