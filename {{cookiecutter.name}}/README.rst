{{cookiecutter.name}}
#####################

{{cookiecutter.description}}


Develop
-------

    python setup.py develop


Build
-----

    python setup.py sdist


Deploy
------

    pip install dist/{{cookiecutter.name}}-<version>.zip


Use
---

Install the package to a virtualenv or some other location and add it to
the sys.path of your 3ds Max installation. Then just do::

    import {{cookiecutter.name}}
    {{cookiecutter.name}}.init()


Test
----

You will need pytest.

    py.test tests -v