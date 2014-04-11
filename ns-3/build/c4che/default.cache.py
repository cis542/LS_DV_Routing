AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
CC = ['/usr/bin/gcc']
CCDEFINES = ['NDEBUG']
CCDEFINES_ST = '-D%s'
CCFLAGS = ['-O0', '-g0']
CCFLAGS_DEBUG = ['-g']
CCFLAGS_MACBUNDLE = ['-fPIC']
CCFLAGS_RELEASE = ['-O2']
CCLNK_SRC_F = ''
CCLNK_TGT_F = ['-o', '']
CC_NAME = 'gcc'
CC_SRC_F = ''
CC_TGT_F = ['-c', '-o', '']
CC_VERSION = ('4', '6', '3')
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPP = '/usr/bin/cpp'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = ['NDEBUG']
CXXDEFINES_ST = '-D%s'
CXXFLAGS = ['-O0', '-g0']
CXXFLAGS_DEBUG = ['-g']
CXXFLAGS_RELEASE = ['-O2']
CXXLNK_SRC_F = ''
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = ''
CXX_TGT_F = ['-c', '-o', '']
DEST_BINFMT = 'elf'
DEST_CPU = 'x86'
DEST_OS = 'linux'
FULLSTATIC_MARKER = '-static'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
NS3_ACTIVE_VARIANT = 'debug'
NS3_BUILDDIR = '/home/lanlan/ns-3/build'
NS3_OPTIONAL_FEATURES = []
PKG_CONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr/local'
RANLIB = '/usr/bin/ranlib'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STATICLIBPATH_ST = '-L%s'
STATICLIB_MARKER = '-Wl,-Bstatic'
STATICLIB_ST = '-l%s'
macbundle_PATTERN = '%s.bundle'
program_PATTERN = '%s'
shlib_CCFLAGS = ['-fPIC', '-DPIC']
shlib_CXXFLAGS = ['-fPIC', '-DPIC']
shlib_LINKFLAGS = ['-shared']
shlib_PATTERN = 'lib%s.so'
staticlib_LINKFLAGS = ['-Wl,-Bstatic']
staticlib_PATTERN = 'lib%s.a'
