module = Extension('aspell',
    libraries = ['aspell'],
    library_dirs = ['/usr/local/lib/'],
    include_dirs = ['/opt/local/include'],
    sources = ['aspell.c']
)
