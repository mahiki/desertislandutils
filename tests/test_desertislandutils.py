from desertislandutils import __version__


def test_version():
    # I don't know why I'm testing this but at least the import worked in pytest
    assert __version__ == '0.3.0'
