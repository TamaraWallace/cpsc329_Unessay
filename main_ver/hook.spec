# -*- mode: python -*-

block_cipher = None


a = Analysis(['hook.py'],
             pathex=['C:\\Users\\alexa\\OneDrive\\Desktop\\CPSC 329\\Virus\\Unessay3\\cpsc329_Unessay-main\\main_ver\\Hook Stuff'],
             binaries=[],
             datas=[],
             hiddenimports=['requests', 'keyboard', 'python-firebase'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hook',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
