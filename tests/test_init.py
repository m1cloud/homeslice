import homeslice

def test_returns_version():
    assert(homeslice.version().startswith('Homeslice '))

