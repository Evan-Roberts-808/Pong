# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pong.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/best.pickle', 'assets'),
        ('assets/config.txt', 'assets'),
        ('assets/entities.py', 'assets'),
        ('assets/game.py', 'assets'),
        ('assets/one_player.py', 'assets'),
        ('assets/two_player.py', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
