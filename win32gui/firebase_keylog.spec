# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['firebase_keylog.py'],
             pathex=['C:\\Users\\dangk\\Documents\\GitHub\\cpsc329_Unessay\\win32gui'],
             binaries=[],
             datas=[],
             hiddenimports=['requests', 'pywin32', 'win32gui', 'keyboard', 'python-firebase'],
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
          name='firebase_keylog',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
