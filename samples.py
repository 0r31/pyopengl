#! /usr/bin/env python
"""Downloads project source checkouts for integration as samples"""
import os

class CVSSource( object ):
    def __init__( self, root, project=None, dirname=None ):
        self.root = root 
        self.project = project 
        if dirname is None:
            dirname = project
        self.dirname = dirname 
    @property
    def checkout_command( self ):
        assert self.project 
        assert self.root 
        assert self.dirname
        return 'cvs -d%s co -d%s %s'%(
            self.root, self.dirname, self.project, 
        )
    @property 
    def update_command( self ):
        return 'cvs up -C'
    def checkout( self ):
        command = self.checkout_command
        print command
        os.system(
            command
        )
    def update( self ):
        if os.path.exists( self.dirname ):
            cwd = os.getcwd()
            try:
                os.chdir( self.dirname )
                command = self.update_command
                print command
                os.system( command )
            finally:
                os.chdir( cwd )
        else:
            self.checkout()
class SVNSource( CVSSource ):
    @property
    def checkout_command( self ):
        assert self.root 
        assert self.dirname
        return 'svn co %s %s'%(
            self.root, self.dirname,
        )
    @property 
    def update_command( self ):
        return 'svn up'

class BZRSource( CVSSource ):
    @property
    def checkout_command( self ):
        assert self.root 
        assert self.dirname
        return 'bzr checkout --lightweight %s %s'%(
            self.root, self.dirname,
        )
    @property 
    def update_command( self ):
        return 'bzr update'

class HgSource( CVSSource ):
    @property 
    def checkout_command( self ):
        assert self.root 
        assert self.dirname 
        return 'hg clone %s %s'%(
            self.root, self.dirname,
        )
    @property
    def update_command( self ):
        """Note: requires enabling the fetch extension (sigh)"""
        return 'hg fetch'

class GITSource( CVSSource ):
    @property
    def checkout_command( self ):
        assert self.root 
        assert self.dirname
        return 'git clone %s %s'%(
            self.root, self.dirname,
        )
    @property 
    def update_command( self ):
        return 'git pull'


checkouts = [
#	CVSSource(
#		':pserver:anonymous@pyopengl.cvs.sourceforge.net:/cvsroot/pyopengl',
#		'OpenGLContext',
#	),
    BZRSource(
        'lp:~mcfletch/openglcontext/trunk',
        'OpenGLContext',
    ),
#	CVSSource(
#		':pserver:anonymous@pyopengl.cvs.sourceforge.net:/cvsroot/pyopengl',
#		'Demo/PyOpenGL-Demo',
#		'PyOpenGL-Demo',
#	),
    BZRSource(
        'lp:~mcfletch/pyopengl-demo/trunk',
        'PyOpenGL-Demo',
    ),
    
    CVSSource(
        ':pserver:anonymous@glinter.cvs.sourceforge.net:/cvsroot/glinter',
        'Glinter',
    ),
    CVSSource(
        ':pserver:anonymous@pymmlib.cvs.sourceforge.net:/cvsroot/pymmlib',
        'pymmlib',
    ),
    CVSSource(
        ':pserver:anonymous@pybzedit.cvs.sourceforge.net:/cvsroot/pybzedit',
        'pybzedit',
    ),
    CVSSource(
        ':pserver:anonymous@pyui.cvs.sourceforge.net:/cvsroot/pyui',
        'PyUIcvs',
        'pyui',
    ),
    CVSSource(
        ':pserver:anonymous@pyui2.cvs.sourceforge.net:/cvsroot/pyui2',
        'pyui2',
        'pyui2',
    ),
    SVNSource(
        'http://pymmlib.svn.sourceforge.net/viewvc/pymmlib/trunk/pymmlib/',
        dirname = 'pymmlib',
    ),
#    SVNSource(
#        'http://visionegg.org/svn/trunk/visionegg',
#        dirname = 'visionegg',
#    ),
    GITSource(
        'git://github.com/visionegg/visionegg.git',
        dirname = 'visionegg',
    ),
    GITSource(
        'git://github.com/tito/pymt.git',
        dirname = 'pymt',
    ),
    SVNSource(
        'http://svn.gnome.org/svn/gnome-games/trunk/glchess',
        dirname = 'glchess',
    ),
    SVNSource(
        'https://kamaelia.svn.sourceforge.net/svnroot/kamaelia/trunk',
        dirname = 'kamaelia',
    ),
    SVNSource(
        'http://pyggel.googlecode.com/svn/trunk',
        dirname = 'pyggel',
    ),
    SVNSource(
        'http://pygl2d.googlecode.com/svn/trunk',
        dirname = 'pygl2d',
    ),
    BZRSource(
        'lp:~bebraw/scocca/devel',
        dirname = 'scocca',
    ),
    HgSource(
        'https://bitbucket.org/tartley/gltutpy',
        dirname = 'gltutpy',
    ),
    HgSource(
        'https://bitbucket.org/tartley/algorithmic-generation-of-geometry',
        dirname = 'agog',
    ),
    HgSource(
        'https://bitbucket.org/tartley/gloopy',
        dirname = 'gloopy',
    ),
    HgSource(
        'https://code.google.com/p/visvis/',
        dirname = 'visvis',
    ),
    # pymol # not pyopengl AFAICS
    # {LGPL} mirra # no online view of code AFAICS
    # soccerbots http://soccerbots.googlecode.com/svn/
    # enough http://enough.googlecode.com/svn/ trunk/
    # flyback http://flyback.googlecode.com/svn/ trunk/
    # threeDS
    # pyODE (examples)
    # Dice3DS (BSD) 
    # KeyJnote (GPL)
    # PyGauntlet (GPL) http://pygauntlet.googlecode.com/svn
    # LPhoto (GPL) lphoto_2.0.42-0.0.0.45.lindows0.1.tar.gz
    # http://crystaltowers.googlecode.com/svn/ trunk/
    ### beryl-mesa-0.1.4.tar.bz2
    ### Mesa source distribution mesa/glapi 
    
]

if __name__ == "__main__":
    os.chdir( '.samples' )
    for checkout in checkouts:
        print 'Project:', checkout.dirname
        checkout.update()
    
