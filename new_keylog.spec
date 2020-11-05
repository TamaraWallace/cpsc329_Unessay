# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['new_keylog.py'],
             pathex=['C:\\Users\\dangk\\Documents\\GitHub\\cpsc329_Unessay'],
             binaries=[],
             datas=[],
             hiddenimports=['requests', 'keyboard'],
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
          name='new_keylog',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
